import shutil
import os
import tkinter as tk
from tkinter import messagebox

def copy_to_backup():
    src = r'C:\Users\Alex\AppData\Local\SRSBot\Bot_Items'
    dst = r'C:\Users\Alex\Desktop\Items backup'
    try:
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        messagebox.showinfo("Success", "Files copied to backup successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy files: {e}")

def copy_to_original():
    src = r'C:\Users\Alex\Desktop\Items backup'
    dst = r'C:\Users\Alex\AppData\Local\SRSBot\Bot_Items'
    try:
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        messagebox.showinfo("Success", "Files copied to original location successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy files: {e}")

root = tk.Tk()
root.title("File Copier")

frame = tk.Frame(root)
frame.pack(pady=20)

copy_to_backup_btn = tk.Button(frame, text="Copy to Backup", command=copy_to_backup)
copy_to_backup_btn.pack(side=tk.LEFT, padx=10)

copy_to_original_btn = tk.Button(frame, text="Copy to Original", command=copy_to_original)
copy_to_original_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()