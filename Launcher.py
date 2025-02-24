import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import logging
import pyperclip  # Import pyperclip to copy text to clipboard
import requests
import time

# Define the directory to store the text files
bot_items_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'SRSBot', 'Bot_Items')
os.makedirs(bot_items_dir, exist_ok=True)

# Define file paths
token_file = os.path.join(bot_items_dir, 'token.txt')
channel_file = os.path.join(bot_items_dir, 'channel.txt')
roles_file = os.path.join(bot_items_dir, 'roles.txt')
log_file = 'Z:\\Testing Logs\\Launcher_Logs.log'

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_file(url, dest):
    response = requests.get(url)
    response.raise_for_status()
    with open(dest, 'wb') as f:
        f.write(response.content)

def read_data():
    try:
        if os.path.exists(token_file):
            with open(token_file, 'r') as f:
                token_entry.insert(0, f.read().strip())
        if os.path.exists(channel_file):
            with open(channel_file, 'r') as f:
                channel_entry.insert(0, f.read().strip())
        if os.path.exists(roles_file):
            with open(roles_file, 'r') as f:
                roles = f.readlines()
                if len(roles) > 0:
                    p_ver_entry.insert(0, roles[0].strip())
                if len(roles) > 1:
                    verified_entry.insert(0, roles[1].strip())
        logging.info("Data read successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read data: {e}")
        logging.error(f"Failed to read data: {e}")

def write_data():
    bot_token = token_entry.get()
    welcome_channel = channel_entry.get()
    p_ver_role = p_ver_entry.get()
    verified_role = verified_entry.get()

    try:
        with open(token_file, 'w') as f:
            f.write(bot_token)
        with open(channel_file, 'w') as f:
            f.write(welcome_channel)
        with open(roles_file, 'w') as f:
            f.write(f"{p_ver_role}\n{verified_role}")

        messagebox.showinfo("Success", "Data written successfully!")
        logging.info("Data written successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write data: {e}")
        logging.error(f"Failed to write data: {e}")

def start_bot():
    try:
        srsbot_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'SRSBot', 'bot_files')
        activate_script = os.path.join(srsbot_dir, 'srsenv', 'Scripts', 'activate.bat')
        verifier_script = os.path.join(srsbot_dir, 'Verifier.py')

        # Command to start the bot
        command = f'python {verifier_script}'

        # Log the command for debugging purposes
        logging.debug(f"Command to start bot: {command}")

        # Copy the command to the clipboard
        pyperclip.copy(command)

        # Show a message box with instructions
        messagebox.showinfo("Info", "The command to start the bot has been copied to your clipboard. Please click anywhere in the open terminal window, paste the command, and hit Enter.")

        # Start the virtual environment
        subprocess.run(['powershell', '-Command', f'Start-Process cmd -ArgumentList \'/k cd /d {srsbot_dir} && call {activate_script}\' -Verb RunAs'])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start the bot: {e}")
        logging.error(f"Failed to start the bot: {e}")

def package_manager():
    try:
        updater_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'SRSBot', 'Updater')
        os.makedirs(updater_dir, exist_ok=True)

        # Fetch and update package manager files from GitHub
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/dist/package_manager.exe', os.path.join(updater_dir, 'package_manager.exe'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/package_manager.spec', os.path.join(updater_dir, 'package_manager.spec'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/package_manager.py', os.path.join(updater_dir, 'package_manager.py'))

        logging.info("Package manager files fetched and updated successfully.")

        # Wait a moment before launching the package manager
        time.sleep(2)

        package_manager_path = os.path.join(updater_dir, 'package_manager.exe')
        # Run the package manager with administrative privileges
        subprocess.run(['powershell', '-Command', f'Start-Process "{package_manager_path}" -Verb RunAs'])
        logging.info("Opened the package manager with elevated permissions.")

        # Close the launcher
        root.quit()
        logging.info("Launcher closed.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update and open the package manager: {e}")
        logging.error(f"Failed to update and open the package manager: {e}")

def quit_app():
    root.quit()
    logging.info("Application closed.")

# Create the main window
root = tk.Tk()
root.title("SRSBot Launcher")

# Create and place the labels and entry fields
tk.Label(root, text="Bot Token:").grid(row=0, column=0, padx=10, pady=5)
token_entry = tk.Entry(root, width=50)
token_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Welcome Channel:").grid(row=1, column=0, padx=10, pady=5)
channel_entry = tk.Entry(root, width=50)
channel_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Unverified User Role (P-Ver):").grid(row=2, column=0, padx=10, pady=5)
p_ver_entry = tk.Entry(root, width=50)
p_ver_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Verified Role:").grid(row=3, column=0, padx=10, pady=5)
verified_entry = tk.Entry(root, width=50)
verified_entry.grid(row=3, column=1, padx=10, pady=5)

# Create and place the buttons
tk.Button(root, text="Write Data", command=write_data).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Package Manager", command=package_manager).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Start Bot", command=start_bot).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Quit", command=quit_app).grid(row=5, column=1, padx=10, pady=10)

# Read the data from files and populate the entry fields
read_data()

# Run the main loop
root.mainloop()