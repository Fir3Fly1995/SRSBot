import tkinter as tk

def on_button_click(button_name):
    print(f"{button_name} button clicked")

# Create the main window
root = tk.Tk()
root.title("Button Window")

# Create buttons
button1 = tk.Button(root, text="Button 1", command=lambda: on_button_click("Button 1"))
button1.pack(pady=10)

button2 = tk.Button(root, text="Button 2", command=lambda: on_button_click("Button 2"))
button2.pack(pady=10)

button3 = tk.Button(root, text="Button 3", command=lambda: on_button_click("Button 3"))
button3.pack(pady=10)

button4 = tk.Button(root, text="Button 4", command=lambda: on_button_click("Button 4"))
button4.pack(pady=10)

# Run the application
root.mainloop()