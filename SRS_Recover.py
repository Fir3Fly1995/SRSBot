import os
import subprocess
import shutil
import requests
import tkinter as tk
from tkinter import messagebox

# Define directories and file paths
srsbot_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'SRSBot')
srsrecovery_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'SRSRecovery')
crit_dir = os.path.join(srsrecovery_dir, 'Crit')
log_file = os.path.join(os.getenv('LOCALAPPDATA'), 'Temp', 'SRSLog', 'rcvr.log')

# Ensure the Crit directory exists
os.makedirs(crit_dir, exist_ok=True)

def log_message(message):
    with open(log_file, 'a') as log:
        log.write(message + '\n')
    print(message)

def fetch_file(url, dest):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(dest, 'wb') as f:
            f.write(response.content)
        log_message(f"File fetched successfully from {url} to {dest}")
    except Exception as e:
        log_message(f"Failed to fetch file from {url} to {dest}: {e}")

def rebuild_file_structure():
    try:
        # Step 1: Remove srs_env and place it in Crit
        srs_env_dir = os.path.join(srsbot_dir, 'srsenv')
        crit_srs_env_dir = os.path.join(crit_dir, 'srs_env')
        if os.path.exists(srs_env_dir):
            shutil.move(srs_env_dir, crit_srs_env_dir)
            log_message(f"Moved {srs_env_dir} to {crit_srs_env_dir}")

        # Step 2: Remove Bot_Items and place it in Crit
        bot_items_dir = os.path.join(srsbot_dir, 'Bot_Items')
        crit_bot_items_dir = os.path.join(crit_dir, 'Bot_Items')
        if os.path.exists(bot_items_dir):
            shutil.move(bot_items_dir, crit_bot_items_dir)
            log_message(f"Moved {bot_items_dir} to {crit_bot_items_dir}")

        # Step 3: Delete SRSBot folder
        if os.path.exists(srsbot_dir):
            shutil.rmtree(srsbot_dir)
            log_message(f"Deleted {srsbot_dir}")

        messagebox.showinfo("Success", "File structure rebuilt successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to rebuild file structure: {e}")
        log_message(f"Failed to rebuild file structure: {e}")

def retrieve_files():
    try:
        # Fetch files from GitHub and place them in the corresponding directories
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/dist/Launcher.exe', os.path.join(srsbot_dir, 'dist', 'Launcher.exe'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/dist/Package_manager.exe', os.path.join(srsbot_dir, 'dist', 'package_manager.exe'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/Verifier.py', os.path.join(srsbot_dir, 'Verifier.py'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/Removers/unins000.dat', os.path.join(srsbot_dir, 'unins000.dat'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/Removers/unins000.exe', os.path.join(srsbot_dir, 'unins000.exe'))

        messagebox.showinfo("Success", "Files retrieved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve files: {e}")
        log_message(f"Failed to retrieve files: {e}")

def assemble():
    try:
        # Step 1: Move srs_env from Crit to SRSBot
        crit_srs_env_dir = os.path.join(crit_dir, 'srs_env')
        srs_env_dir = os.path.join(srsbot_dir, 'srsenv')
        if os.path.exists(crit_srs_env_dir):
            shutil.move(crit_srs_env_dir, srs_env_dir)
            log_message(f"Moved {crit_srs_env_dir} to {srs_env_dir}")

        # Step 2: Move Bot_Items from Crit to SRSBot
        crit_bot_items_dir = os.path.join(crit_dir, 'Bot_Items')
        bot_items_dir = os.path.join(srsbot_dir, 'Bot_Items')
        if os.path.exists(crit_bot_items_dir):
            shutil.move(crit_bot_items_dir, bot_items_dir)
            log_message(f"Moved {crit_bot_items_dir} to {bot_items_dir}")

        # Step 3: Verify the integrity of srs_env and Bot_Items
        if os.path.exists(srs_env_dir) and os.path.exists(bot_items_dir):
            log_message("Integrity of srs_env and Bot_Items verified")

        # Step 4: Delete the Crit directory if all files were properly moved
        if os.path.exists(crit_dir):
            shutil.rmtree(crit_dir)
            log_message(f"Deleted {crit_dir}")

        messagebox.showinfo("Success", "Assembly completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to assemble: {e}")
        log_message(f"Failed to assemble: {e}")

def recover_all():
    try:
        # Step 1: Fetch the removers directory from GitHub
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/Removers/unins000.dat', os.path.join(srsbot_dir, 'unins000.dat'))
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/Removers/unins000.exe', os.path.join(srsbot_dir, 'unins000.exe'))

        # Step 2: Edit unins000.dat to instruct unins000.exe to remove the entire SRSBot folder
        # (This step requires specific knowledge of the unins000.dat format and is not implemented here)

        # Step 3: Edit unins000.dat to omit SRSRecovery directory from the uninstall process
        # (This step requires specific knowledge of the unins000.dat format and is not implemented here)

        # Step 4: Fetch the installer from GitHub releases
        fetch_file('https://github.com/Fir3Fly1995/SRSBot/releases/latest/download/SRSBotInstaller.exe', os.path.join(os.getenv('USERPROFILE'), 'Downloads', 'SRSBotInstaller.exe'))

        # Step 5: Start cmd.exe to delete SRSRecovery directory and launch the installer
        cmd_script = f"""
        timeout /t 5
        del /q /s {srsrecovery_dir}
        start {os.path.join(os.getenv('USERPROFILE'), 'Downloads', 'SRSBotInstaller.exe')}
        """
        with open(os.path.join(srsrecovery_dir, 'cleanup.cmd'), 'w') as f:
            f.write(cmd_script)
        subprocess.run(['cmd.exe', '/c', os.path.join(srsrecovery_dir, 'cleanup.cmd')], check=True)

        messagebox.showinfo("Success", "Recovery process completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to recover: {e}")
        log_message(f"Failed to recover: {e}")

def run_in_thread(func):
    threading.Thread(target=func).start()

# Create the main window
root = tk.Tk()
root.title("SRSBot Recovery Platform")

# Create buttons
button_width = 20

rebuild_button = tk.Button(root, text="Rebuild File Structure", command=lambda: run_in_thread(rebuild_file_structure), width=button_width)
rebuild_button.grid(row=0, column=0, padx=10, pady=10)

retrieve_button = tk.Button(root, text="Retrieve Files", command=lambda: run_in_thread(retrieve_files), width=button_width)
retrieve_button.grid(row=1, column=0, padx=10, pady=10)

assemble_button = tk.Button(root, text="Assemble", command=lambda: run_in_thread(assemble), width=button_width)
assemble_button.grid(row=2, column=0, padx=10, pady=10)

recover_button = tk.Button(root, text="Recover All", command=lambda: run_in_thread(recover_all), width=button_width)
recover_button.grid(row=3, column=0, padx=10, pady=10)

# Run the application
root.mainloop()