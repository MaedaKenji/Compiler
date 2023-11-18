# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:20:20 2023

@author: agusf
"""

import tkinter as tk
# =============================================================================
# import subprocess
# import sys
# from tkinter import filedialog
# from tkinter.scrolledtext import ScrolledText
# from pygments.lexers import PythonLexer
# from pygments import highlight
# from pygments.formatters import get_formatter_by_name
# =============================================================================
from func import *

root = tk.Tk()
root.title("Python IDE")

# Create frane
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)


# Create Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)


# Create the code editor text widget
code_editor = tk.Text(frame, font=("Courier New", 12), bg="#121212", fg="white",)
code_editor.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


# Create a line numbers text widget
line_numbers = tk.Text(code_editor, width=4, padx=4, pady=4,
                       bg="#272822", fg="#75715E", state='disabled')
line_numbers.pack(side=tk.LEFT, fill=tk.Y)












# Start the Tkinter event loop
root.mainloop()
