import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import shutil
import requests

# Define directories and file paths
srsbot_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'SRSBot')
bot_files_dir = os.path.join(srsbot_dir, 'bot_files')
updater_dir = os.path.join(srsbot_dir, 'Updater')
bot_items_dir = os.path.join(srsbot_dir, 'Bot_Items')
saved_info_file = os.path.join(os.path.expanduser('~'), 'Desktop', 'Saved Bot Info.txt')

def fetch_file(url, dest):
    response = requests.get(url)
    response.raise_for_status()
    with open(dest, 'wb') as f:
        f.write(response.content)

def update_bot():
    try:
        # Fetch and update files from GitHub
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/Launcher.spec', os.path.join(bot_files_dir, 'Launcher.spec'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/Launcher.py', os.path.join(bot_files_dir, 'Launcher.py'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/dist/Launcher.exe', os.path.join(bot_files_dir, 'Launcher.exe'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/raw/main/Verifier.py', os.path.join(bot_files_dir, 'Verifier.py'))
        messagebox.showinfo("Success", "Bot updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update bot: {e}")

def uninstall_bot():
    try:
        # Save bot info to desktop
        with open(saved_info_file, 'w') as f:
            with open(os.path.join(bot_items_dir, 'token.txt'), 'r') as token_file:
                f.write(f"Discord Bot Token\n{token_file.read()}\n\n")
            with open(os.path.join(bot_items_dir, 'channel.txt'), 'r') as channel_file:
                f.write(f"Welcome Channel\n{channel_file.read()}\n\n")
            with open(os.path.join(bot_items_dir, 'roles.txt'), 'r') as roles_file:
                roles = roles_file.readlines()
                f.write(f"Pre-Verification Role\n{roles[0]}\n\n")
                f.write(f"Verified Role\n{roles[1]}\n\n")

        # Delete bot items
        shutil.rmtree(bot_items_dir)

        # Run uninstaller
        uninstaller = os.path.join(srsbot_dir, 'unins000.exe')
        subprocess.run([uninstaller], check=True)
        messagebox.showinfo("Success", "Bot uninstalled successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to uninstall bot: {e}")

def share_bot():
    # Implement the logic to bundle up the bot to share it with friends
    messagebox.showinfo("Info", "Share bot functionality is not yet implemented.")

def quit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("SRSBot Package Manager")

# Create a heading
heading = tk.Label(root, text="Welcome to the SRS Package Manager", font=("Helvetica", 16))
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Create buttons
update_button = tk.Button(root, text="Update Bot", command=update_bot, width=20)
update_button.grid(row=1, column=0, padx=10, pady=10)

install_button = tk.Button(root, text="Install Bot", command=lambda: messagebox.showinfo("Info", "Install functionality is not yet implemented."), width=20)
install_button.grid(row=2, column=0, padx=10, pady=10)

uninstall_button = tk.Button(root, text="Uninstall Bot", command=uninstall_bot, width=20)
uninstall_button.grid(row=1, column=1, padx=10, pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_app, width=20)
quit_button.grid(row=2, column=1, padx=10, pady=10)

# Run the application
root.mainloop()