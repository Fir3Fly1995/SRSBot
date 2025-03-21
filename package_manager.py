import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import shutil
import requests
import threading
import zipfile

# Define directories and file paths
srsbot_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'SRSBot')
bot_files_dir = os.path.join(srsbot_dir, 'bot_files')
updater_dir = os.path.join(srsbot_dir, 'Updater')
bot_items_dir = os.path.join(srsbot_dir, 'Bot_Items')
saved_info_file = os.path.join(os.path.expanduser('~'), 'Desktop', 'Saved Bot Info.txt')

def fetch_file(url, dest):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(dest, 'wb') as f:
            f.write(response.content)
        print(f"File fetched successfully from {url} to {dest}")
    except Exception as e:
        print(f"Failed to fetch file from {url} to {dest}: {e}")

def update_bot():
    try:
        # Fetch and update files from GitHub
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/dist/Launcher.exe', os.path.join(bot_files_dir, 'Launcher.exe'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/Verifier.py', os.path.join(bot_files_dir, 'Verifier.py'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/srsenv.zip', os.path.join(bot_files_dir, 'srsenv.zip'))

        # Unzip the srsenv.zip file
        with zipfile.ZipFile(os.path.join(bot_files_dir, 'srsenv.zip'), 'r') as zip_ref:
            zip_ref.extractall(bot_files_dir)
        print("srsenv.zip unzipped successfully")

        messagebox.showinfo("Success", "Bot updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update bot: {e}")
        print(f"Failed to update bot: {e}")

def uninstall_bot():
    try:
        # Step 1: Save bot info to desktop
        with open(saved_info_file, 'w') as f:
            with open(os.path.join(bot_items_dir, 'token.txt'), 'r') as token_file:
                f.write(f"Discord Bot Token\n{token_file.read()}\n\n")
            with open(os.path.join(bot_items_dir, 'channel.txt'), 'r') as channel_file:
                f.write(f"Welcome Channel\n{channel_file.read()}\n\n")
            with open(os.path.join(bot_items_dir, 'roles.txt'), 'r') as roles_file:
                roles = roles_file.readlines()
                f.write(f"Pre-Verification Role\n{roles[0]}\n\n")
                f.write(f"Verified Role\n{roles[1]}\n\n")

        # Step 2: Delete bot items
        shutil.rmtree(bot_items_dir)
        print("Bot items deleted")

        # Step 3: Run uninstaller
        uninstaller = os.path.join(srsbot_dir, 'unins000.exe')
        subprocess.run([uninstaller], check=True)
        print("Uninstaller run successfully")

        # Step 4: Close the package manager and launcher
        root.quit()
        print("Package manager and launcher closed")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to uninstall bot: {e}")
        print(f"Failed to uninstall bot: {e}")

def share_bot():
    # Implement the logic to bundle up the bot to share it with friends
    messagebox.showinfo("Info", "Share bot functionality is not yet implemented.")

def quit_app():
    root.quit()

def prompt_return_to_launcher():
    response = messagebox.askyesno("Return to Launcher", "Would you like to return to the launcher?")
    if response:
        launcher_path = os.path.join(bot_files_dir, 'Launcher.exe')
        subprocess.run(['powershell', '-Command', f'Start-Process "{launcher_path}" -Verb RunAs'])
        root.quit()

def run_in_thread(func):
    threading.Thread(target=func).start()

# Create the main window
root = tk.Tk()
root.title("SRSBot Package Manager")

# Create a heading
heading = tk.Label(root, text="Welcome to SRS Updater", font=("Helvetica", 16))
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Create buttons
button_width = 20

update_button = tk.Button(root, text="Update/Install Bot", command=lambda: run_in_thread(update_bot), width=button_width)
update_button.grid(row=1, column=0, padx=10, pady=10)

share_button = tk.Button(root, text="Share Bot", command=share_bot, width=button_width)
share_button.grid(row=2, column=0, padx=10, pady=10)

uninstall_button = tk.Button(root, text="Uninstall Bot", command=lambda: run_in_thread(uninstall_bot), width=button_width)
uninstall_button.grid(row=1, column=1, padx=10, pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_app, width=button_width)
quit_button.grid(row=2, column=1, padx=10, pady=10)

# Add a button to prompt the user to return to the launcher
return_button = tk.Button(root, text="Return to Launcher", command=prompt_return_to_launcher, width=button_width)
return_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()