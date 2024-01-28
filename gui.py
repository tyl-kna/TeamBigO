import tkinter as tk
from tkinter import filedialog, messagebox, font, PhotoImage
from PIL import Image, ImageTk

TBFILE = None
FILE1 = None
current_font_size = 14  # Default font size

# Function to clear the screen
def clear_screen():
  for widget in root.winfo_children():
      widget.destroy()


# Function to adjust the font size
def adjust_font_size(new_size):
    global current_font_size, text_box
    current_font_size = new_size
    text_font = font.Font(size=current_font_size)


def open_settings_page():
    # Clear the screen of existing widgets
    clear_screen()

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    home_button = tk.Button(root,
                            text="Home",
                            image=home_icon,
                            bd=0,
                            command=open_home_page)
    home_button.grid(row=0, column=0, sticky=tk.W, padx=3, pady=3)

    # Slider for font size
    font_size_slider = tk.Scale(
        root,
        from_=8,
        to=24,
        orient='horizontal',
        label='Font Size',
        command=lambda value: adjust_font_size(int(value)))
    font_size_slider.set(current_font_size)  # Set the default value
    font_size_slider.grid(row=1, column=0, sticky='ew', padx=3, pady=3)


def open_info_page():
    # Clear the screen of existing widgets
    clear_screen()

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    home_button = tk.Button(root,
                            text="Home",
                            image=home_icon,
                            bd=0,
                            command=open_home_page)
    home_button.grid(row=0, column=0, sticky=tk.W, padx=3, pady=3)

    info_label = tk.Label(root, text="Test info")
    info_label.grid(row=1, column=0, sticky="nsew")


def open_home_page():
    # Clear all existing widgets
    clear_screen()

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    def on_resize(event):
        # resize the background image to the size of label
        image = bgimg.resize((event.width, event.height))
        # update the image of the label
        l.image = ImageTk.PhotoImage(image)
        l.config(image=l.image)

    l = tk.Label(root)
    l.place(x=0, y=0, relwidth=1,
            relheight=1)  # make label l to fit the parent window always
    l.bind('<Configure>',
           on_resize)  # on_resize will be executed whenever label l is resized

    home_button = tk.Button(root,
                            text="Home",
                            image=home_icon,
                            bd=0,
                            command=open_home_page)
    home_button.grid(row=0, column=0, sticky=tk.W, padx=3, pady=3)

    setting_button = tk.Button(root,
                               text="Settings",
                               image=setting_icon,
                               bd=0,
                               command=open_settings_page)
    setting_button.grid(row=2, column=0, sticky=tk.W, padx=3, pady=3)

    info_button = tk.Button(root,
                            text="Info Page",
                            image=info_icon,
                            bd=0,
                            command=open_info_page)
    info_button.grid(row=1, column=0, sticky=tk.W, padx=3, pady=3)

    def clear_text_box():
        global TBFILE
        TBFILE = None
        text_box.delete("1.0", "end")
    clear_button = tk.Button(root, text="Clear", command=clear_text_box)
    clear_button.grid(row=2, column=0, sticky=tk.E, padx=360, pady=3)

    def calculate_big_O():
        global FILE1, TBFILE
        if FILE1 == None:
            messagebox.showerror(
                'Selection Error',
                'No file was selected, please select a file!')
            return
        with open(FILE1, 'r') as file:
            content = file.read()
            text_box.insert(tk.END, content)
            save_point(text_box)
        FILE1 = None

    calculate_button = tk.Button(root,
                                 text="Calculate",
                                 command=calculate_big_O)
    calculate_button.grid(row=2, column=0, sticky=tk.W, padx=335, pady=3)

    select_button = tk.Button(root,
                              text="Select Text File",
                              command=select_file)
    select_button.grid(row=1, column=0, pady=3)

    text_box = tk.Text(root,
                       wrap=tk.WORD,
                       font=font.Font(size=current_font_size))
    text_box.grid(row=5,
                  column=0,
                  columnspan=2,
                  sticky="nsew",
                  padx=3,
                  pady=100)

    scrollbar = tk.Scrollbar(root, command=text_box.yview)
    scrollbar.grid(row=5, column=2, sticky="nsew", padx=3, pady=100)

    text_box.config(yscrollcommand=scrollbar.set)

    load_point(text_box)

def select_file():
    global FILE1
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    FILE1 = file_path

def save_point(text_box):
  global TBFILE
  TBFILE = text_box.get("1.0", tk.END)

def load_point(text_box):
  if TBFILE != None:
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, TBFILE)

# Initialize main application window
root = tk.Tk()
root.title("Big O Calculator")
root.resizable(True, True)

#sets minimum size for window
root.minsize(825, 480)
# creating icons
home_icon = PhotoImage(file="home_icon.png")
info_icon = PhotoImage(file="info_icon.png")
setting_icon = PhotoImage(file="setting_icon.png")
bgimg = Image.open('HackMT_background.png')  # load the background image

root.grid_rowconfigure(5, weight=10)
root.grid_columnconfigure(0, weight=10)

open_home_page()

root.mainloop()
