import tkinter as tk
from tkinter import filedialog

# Function to open and display the selected text file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_box.delete(1.0, tk.END)  # Clear previous content
            text_box.insert(tk.END, content)  # Insert new content

# Create the main window
root = tk.Tk()
root.title("Text File Viewer")

# Create a button to open a text file
open_button = tk.Button(root, text="Open Text File", command=open_file)
open_button.pack()

# Create a text box to display the file content
text_box = tk.Text(root, wrap=tk.WORD)
text_box.pack()

# Start the main loop
root.mainloop()
