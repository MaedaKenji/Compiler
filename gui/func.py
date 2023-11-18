import tkinter as tk
import subprocess
from tkinter import filedialog
import os
# =============================================================================
# from tkinter.scrolledtext import ScrolledText
# from pygments.lexers import PythonLexer
# from pygments import highlight
# from pygments.formatters import get_formatter_by_name
# =============================================================================


def open_file(code_editor):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            code_editor.delete("1.0", tk.END)
            code_editor.insert(tk.END, content)


def save_file(code_editor):
    file_path = filedialog.asksaveasfilename(defaultextension='.py')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(code_editor.get('1.0', tk.END))

def compile_code():
    code = code_editor.get('1.0', tk.END)
    try:
        subprocess.run(["python", "-c", code], check=True,
                       capture_output=True, text=True)
        code_preview.delete('1.0', tk.END)
        code_preview.insert(tk.END, "Compilation successful!", 'success')
    except subprocess.CalledProcessError as e:
        code_preview.delete('1.0', tk.END)
        code_preview.insert(tk.END, f"Compilation error:\n{e.stderr}", 'error')


def button_click():
    print("Button clicked!")
    

def on_code_editor_scroll(*args,line_numbers, code_editor):
    # Synchronize the scrolling of the line numbers and code editor
    line_numbers.yview_moveto(code_editor.xview()[0])
    

def update_line_numbers(line_numbers, code_editor):
    line_numbers.config(state='normal')
    line_numbers.delete('1.0', tk.END)
    lines = code_editor.get('1.0', tk.END).split('\n')
    line_count = len(lines)
    for i in range(1, line_count):
        line_numbers.insert(tk.END, str(i) + '\n')
    line_numbers.config(state='disabled')
    

def read_file(file_name):
    file_path = file_name
    code = []

    try:
        with open(file_path, "r") as file:
            read = file.read()
            code.append(read)

    except FileNotFoundError:
        print("File tidak ditemukan.")

    except Exception as e:
        print("Terjadi kesalahan saat menjalankan kode:")
        print(e)
    return code


def count_spaces(string):
    count = 0
    for i in range(len(string)):
        if string[i] == " ":
            count += 1
            continue
        break  # Exit the loop once the first character is found
    return count
    
def save_temp_file(code_editor):
    file_path = "gui/temp.txt"
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except PermissionError:
        print("File sedang digunakan.")
        
    with open(file_path, 'w') as file:
        file.write(code_editor.get('1.0', tk.END))
    return file_path
