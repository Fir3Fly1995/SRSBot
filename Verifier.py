import discord
from discord.ext import commands
import random
import requests
from bs4 import BeautifulSoup
import asyncio
import os
import logging

# Set the bot token programmatically
BOT_TOKEN = "TOKEN_HERE"  # Replace with your actual bot token

intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content
bot = commands.Bot(command_prefix="!", intents=intents)  # Keep prefix for other commands if needed

verification_codes = {}
verification_messages = {}

# Configure logging
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    license_text = """GNU Affero General Public License (AGPL) with Non-Commercial Clause

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Additional Restriction: Non-Commercial Use Only

This software is licensed under the GNU Affero General Public License (AGPL)
with the following additional restriction:

Non-Commercial Use Only:
You may not use this software or any derivative works for commercial purposes.
Commercial purposes include, but are not limited to:
- Selling the software or any derivative works.
- Using the software in a paid service or product.
- Monetizing the software through advertisements, subscriptions, or any other means.

If you wish to use this software for commercial purposes, you must obtain
explicit permission from the original author(s).
"""
    print(license_text)
    print(f"{bot.user} is ready and online!")
    logging.info(f'{bot.user} has connected to Discord!')

    try:
        await bot.tree.sync()  # Sync slash commands globally
        logging.info("Successfully synced slash commands globally")
    except Exception as e:
        logging.error(f"Error syncing slash commands: {e}")

@bot.tree.command(name="verify", description="Verify your RSI profile.")
async def verify_command(interaction: discord.Interaction, rsi_username: str = None):
    await interaction.response.defer(ephemeral=True)  # Send an initial response to prevent timeout

    user_id = interaction.user.id

    if rsi_username is None:
        code = str(random.randint(100000, 999999))
        verification_codes[user_id] = code

        await interaction.followup.send(
            f"{interaction.user.mention}, please enter the below code into the short bio field of your RSI profile found [here](https://robertsspaceindustries.com/en/account/profile). Return and do `/verify {interaction.user.name}` to complete the process.\n\n\n`{code}`",
            ephemeral=True
        )
        logging.info(f'Generated verification code: {code} for user: {interaction.user}')

    else:
        if user_id in verification_codes:
            code = verification_codes[user_id]
            try:
                url = f"https://robertsspaceindustries.com/en/citizens/{rsi_username}"
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

                soup = BeautifulSoup(response.content, "html.parser")
                bio_element = soup.select_one("div.bio div.value")  # More specific CSS selector
                if bio_element:
                    bio_text = bio_element.text.strip()
                    if code in bio_text:
                        verified_role = discord.utils.get(interaction.guild.roles, name="Verified")  # Gets the role object
                        p_ver_role = discord.utils.get(interaction.guild.roles, name="P-Ver")  # Gets the "P-Ver" role object
                        if verified_role and p_ver_role:
                            await interaction.user.add_roles(verified_role)  # Gives the user the role
                            await interaction.user.edit(nick=rsi_username)  # Change the user's nickname to match their RSI profile name
                            logging.info(f'Attempted to change nickname for user {interaction.user} to {rsi_username}')

                            await interaction.followup.send(f"Your nickname has been updated to: {rsi_username}. You have been verified. You can safely go ahead and remove the code from your profile now if you want to. Welcome to the SRS, Citizen!\n\nHead to <#1328288918990356541> to get chatting!")

                            await asyncio.sleep(3)  # Wait for 3 seconds before removing the "P-Ver" role
                            await interaction.user.remove_roles(p_ver_role)  # Removes the "P-Ver" role
                            logging.info(f'Removed "P-Ver" role from user {interaction.user}')

                            # Commented out message deletion for redundancy
                            # await delete_messages_after(interaction, 1337856225022578719, delay=8)
                        else:
                            await interaction.followup.send("Error: 'Verified' or 'P-Ver' role not found on this server.")
                        del verification_codes[user_id]  # Remove the code after successful verification
                    else:
                        await interaction.followup.send("Code not found in your RSI bio. Please double-check.", ephemeral=True)  # Ephemeral for errors too
                else:
                    await interaction.followup.send("Could not find the bio section on your RSI profile. Please make sure your profile is public.", ephemeral=True)  # More informative message

            except requests.exceptions.RequestException as e:
                logging.error(f'Error checking RSI profile: {e}')
                await interaction.followup.send(f"Error checking RSI profile: {e}", ephemeral=True)
            except Exception as e:
                logging.error(f'An unexpected error occurred: {e}')
                await interaction.followup.send(f"An unexpected error occurred: {e}", ephemeral=True)
        else:
            await interaction.followup.send("Please initiate the verification process by typing `/verify` first.", ephemeral=True)

bot.run(BOT_TOKEN)
