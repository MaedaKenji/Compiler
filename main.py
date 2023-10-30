from func import *

file_path = "E:\Coding\Compiler\code2.txt"
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

# Memisahkan setiap baris kode
lines = code[0].split('\n')

# Memberikan label pada goto
label_line_numbers = {}

for line_number, line in enumerate(lines):
    line = line.strip()  

    if line.endswith(':'):
        label = line[:-1]
        label_line_numbers[label] = line_number
        continue


variables = {}
line_number = 0

# Memulai eksekusi kode
while line_number < len(lines):
    line = lines[line_number].strip()

    # Skip empty lines
    if not line:
        line_number += 1
        continue

    # Increment
    if '+=' in line:
        var, value = line.split('+=')
        
        if value.strip().isdigit():
            print(f"adalah {value.strip()}")
            print("is digit")

            variables[var.strip()] += int(value.strip())
        else:
            variables[var.strip()] += variables[value.strip()]
        line_number += 1
        continue

    # Assign
    if '=' in line:
        var, value = line.split('=')
        variables[var.strip()] = int(value.strip())
        line_number += 1
        continue

    # Print
    if line.startswith('print'):
        var = line.split('(')[1].split(')')[0].strip()
        print(variables[var])
        line_number += 1
        continue
    
    
    # If
    if line.startswith('if'):
        condition_split = line.split('if')[1].split(':')
        
        if len(condition_split) != 2:
            print("Invalid syntax. Exiting the program.")
            break

        condition = condition_split[0].strip()
        if eval(condition, variables):
            line_number += 1
            continue
        else:
            # Elif block
            elif_line_numbers = []
            for i, l in enumerate(lines[line_number + 1:]):
                if l.strip().startswith('elif'):
                    elif_line_numbers.append(line_number + i + 1)
                else:
                    break
            
            # Else block
            else_line_number = None
            for i, l in enumerate(lines[line_number + 1:]):
                if l.strip().startswith('else'):
                    else_line_number = line_number + i + 1
                    break
            
            # Mundur 1 indent
            end_line_number = None
            for i, l in enumerate(lines[line_number:]):
                spaces = count_spaces(l)
                
                for i, m in enumerate(lines[line_number + i:]):
                    if count_spaces(m) == spaces - 4:
                        end_line_number = line_number + i
                        break
                if end_line_number is not None:
                    break
                if end_line_number is None:
                    end_line_number = len(lines)+1
                    break
            line_number = end_line_number

    # Goto
    if line.startswith('goto'):
        label = line.split(' ')[1].strip()
        if label in label_line_numbers:
            line_number = label_line_numbers[label]
        else:
            print(f"Label '{label}' not found. Exiting the program.")
            break
        continue

    # End
    line_number += 1
    if variables['a'] == 9:
        pass