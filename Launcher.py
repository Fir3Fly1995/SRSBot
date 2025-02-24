import tkinter as tk
from tkinter import messagebox
import os
import subprocess

# Define the directory to store the text files
bot_items_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'SRSBot', 'Bot_Items')
os.makedirs(bot_items_dir, exist_ok=True)

# Define file paths
token_file = os.path.join(bot_items_dir, 'token.txt')
channel_file = os.path.join(bot_items_dir, 'channel.txt')
roles_file = os.path.join(bot_items_dir, 'roles.txt')

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
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write data: {e}")

def start_bot():
    try:
        srsbot_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'SRSBot', 'bot_files')
        activate_script = os.path.join(srsbot_dir, 'srsenv', 'Scripts', 'activate.bat')
        verifier_script = os.path.join(srsbot_dir, 'Verifier.py')

        # Command to run in the command prompt
        command = f'cmd /k "cd /d {srsbot_dir} && {activate_script} && python {verifier_script}"'

        # Run the command with administrative privileges
        subprocess.run(['powershell', '-Command', f'Start-Process cmd -ArgumentList \'/k {command}\' -Verb RunAs'])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start the bot: {e}")

def package_manager():
    # Implement the logic for the package manager
    messagebox.showinfo("Info", "Opening the package manager...")

def quit_app():
    root.quit()

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

# Run the main loop
root.mainloop()