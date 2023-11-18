import tkinter as tk
from func import *
import sys
sys.path.append('..')
from Compiler.func import output




root = tk.Tk()
root.title("Python IDE")

# Create a frame to hold the line numbers and code editor widgets
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a line numbers text widget
line_numbers = tk.Text(frame,width=4,bg="#272822", fg="#75715E", state='disabled', font=("Courier New", 12))
line_numbers.pack(side=tk.LEFT, fill=tk.Y)


# Create the code editor text widget
code_editor = tk.Text(frame, font=("Courier New", 12),
                      bg="#121212", fg="white")
code_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# Create Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file(code_editor))
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
# Create play button
play_logo = tk.PhotoImage(
    file="C:/Users/agusf/Downloads/Microsoft Edge/play0.png")
file_menu.add_command(label="Open", command= open_file(code_editor))


# Bind the <KeyRelease> event to the update_line_numbers function
code_editor.bind('<KeyRelease>', lambda event : update_line_numbers(line_numbers,code_editor))

root.mainloop()