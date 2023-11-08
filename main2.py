import re
from func import *

# Defining variables / declaring variables
variables = {}
for_dict = {}
function_names = []
is_first_func = True
is_first_for = True
for_label = None
while_label = None
line_number = 0
repeater = 0
operators = ['+', '-', '*', '/', '%', '==', '!=',
             '<', '>', '<=', '>=', '^', '**', 'and', 'or']
code = read_file("E:\Coding\Compiler\code2.txt")

# Memisahkan setiap baris kode
lines = code[0].split('\n')

# Memberikan label pada goto
label_line_numbers = {}
for i, line in enumerate(lines):
    line = line.strip()

    if line.endswith(':'):
        label = line[:-1]
        label_line_numbers[label] = i
        continue

# Memulai eksekusi kode
while line_number < len(lines):
    line = lines[line_number].strip()  # Line starts from index 0
    # Debugging purpose
    if line_number == 25:
        pass
    # End

    # Skip empty lines
    if not line:
        line_number += 1
        continue

    # Increment
    if '+=' in line:
        var, value = line.split('+=')

        if value.strip().isdigit():
            variables[var.strip()] += int(value.strip())
        elif (var2 := next((char for char in variables if value.strip())), None):
            input_string = value.replace(" ", "")
            parts = re.split('|'.join(re.escape(op)
                             for op in operators), input_string)
            digit = parts[1]
            variables[var.strip()] += variables[var2.strip()] + int(digit)
        else:
            variables[var.strip()] += variables[value.strip()]

        line_number += 1
        continue

    # Decrement
    if '-=' in line:
        var, value = line.split('-=')

        if value.strip().isdigit():
            variables[var.strip()] -= int(value.strip())
        elif (var2 := next((char for char in variables if value.strip())), None):
            input_string = value.replace(" ", "")
            parts = re.split('|'.join(re.escape(op)
                             for op in operators), input_string)
            digit = parts[1]
            variables[var.strip()] -= variables[var2.strip()] + int(digit)
        else:
            variables[var.strip()] -= variables[value.strip()]

        line_number += 1
        continue

    # Multiply
    if '*=' in line:
        var, value = line.split('*=')

        if value.strip().isdigit():
            variables[var.strip()] *= int(value.strip())
        elif (var2 := next((char for char in variables if value.strip())), None):
            input_string = value.replace(" ", "")
            parts = re.split('|'.join(re.escape(op)
                             for op in operators), input_string)
            digit = parts[1]
            variables[var.strip()] *= variables[var2.strip()] + int(digit)
        else:
            variables[var.strip()] *= variables[value.strip()]

        line_number += 1
        continue

    # Divide
    if '/=' in line:
        var, value = line.split('/=')

        if value.strip().isdigit():
            variables[var.strip()] /= int(value.strip())
        elif (var2 := next((char for char in variables if value.strip())), None):
            input_string = value.replace(" ", "")
            parts = re.split('|'.join(re.escape(op)
                             for op in operators), input_string)
            digit = parts[1]
            variables[var.strip()] /= variables[var2.strip()] + int(digit)
        else:
            variables[var.strip()] /= variables[value.strip()]

        line_number += 1
        continue

    # Modulus
    if '%=' in line:
        var, value = line.split('%=')

        if value.strip().isdigit():
            variables[var.strip()] %= int(value.strip())
        elif (var2 := next((char for char in variables if value.strip())), None):
            input_string = value.replace(" ", "")
            parts = re.split('|'.join(re.escape(op)
                             for op in operators), input_string)
            digit = parts[1]
            variables[var.strip()] %= variables[var2.strip()] + int(digit)
        else:
            variables[var.strip()] %= variables[value.strip()]

        line_number += 1
        continue

    # Power
    if '^=' in line:
        var, value = line.split('^=')

        if value.strip().isdigit():
            variables[var.strip()] **= int(value.strip())
        elif (var2 := next((char for char in variables if value.strip())), None):
            input_string = value.replace(" ", "")
            parts = re.split('|'.join(re.escape(op)
                             for op in operators), input_string)
            digit = parts[1]
            variables[var.strip()] **= variables[var2.strip()] + int(digit)
        else:
            variables[var.strip()] **= variables[value.strip()]

        line_number += 1
        continue

    # Assign
    if '=' in line:
        var, value = line.split('=')
        variables[var.strip()] = int(value.strip())
        line_number += 1
        continue

    if line_number == 29:
        pass

    # Print
    if line.startswith('print'):
        # Check if print is only 'print'
        if line[5] == '(':
            var = line.split('print')[1].strip()
            var = line.split('(')[1].split(')')[0].strip()

            if line[6] == '"':
                print(line[6:-1])
                line_number += 1
                continue
            elif line[6] == "'":
                print(line[6:-1])
                line_number += 1
                continue
            elif line[6].isdigit():
                print(line[5:])
                line_number += 1
                continue
            elif var in variables:
                print(variables[var])
                line_number += 1
                continue
            else:
                print("Invalid syntax. Exiting the program.")
                break

    # If line start with if
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

            # Mundur 1 indent, karena keluar dari if
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

    # While
    if line.startswith('while'):
        # condition = line.split('while')[1].replace(' ', '').split(':')[0]
        # pattern = '|'.join(re.escape(op) for op in operators) # Constructing the regular expression pattern
        # condition_split = re.split(pattern, condition) # Splitting the condition based on operators
        while_label = line_number
        line_number += 1
        continue
    if while_label is not None:
        condition = lines[while_label].split(
            'while')[1].replace(' ', '').split(':')[0]
        if eval(condition, variables):
            line_number = while_label
            continue
        else:
            while_label = None
            line_number += 1
            continue

    # For loop
    if line.startswith('for'):
        if is_first_for:
            var = line.split('for')[1].split('in')[0].strip()
            max_iteration = line.split('in')[1].split(
                '(')[1].strip().replace(')', '').replace(' ', '').replace(":", "")
            variables[var] = 0
            print(variables[var])
            for_label = line_number
            is_first_for = False
            line_number += 1
            continue
        else:
            pass

    if for_label is not None:
        # Split the line to extract the range value
        range_value = lines[for_label].split('in')[1].split(
            '(')[1].strip().replace(')', '').replace(' ', '').replace(":", "")

        # Create the new string
        # condition = "i < " + range_value
        condition = lines[for_label].split('for')[1].split('in')[0].strip() + '<' + lines[for_label].split('in')[1].split(
            '(')[1].strip().replace(')', '').replace(' ', '').replace(":", "")
        # print(condition)
        if eval(condition, variables):
            line_number = for_label+1
            variables[var] += 1
            continue
        else:
            for_label = None
            line_number += 1
            continue

    # exit()
    if line.startswith('exit()'):
        break
    # Function
    if line.startswith('func'):
        if is_first_func:
            func_name = line.split('func')[1].split('(')[0].strip()
            func_args = line.split('(')[1].split(')')[0].strip().split(',')
            func_args = [arg.strip() for arg in func_args]
            func_label = line_number

            function_names.append(
                {'name': func_name, 'args': func_args, 'label': func_label})
            is_first_func = False

            # print(function_names)
            # Mundur 1 indent
            end_line_number = None

            for i, l in enumerate(lines[line_number:]):
                spaces = count_spaces(l)

                for i, m in enumerate(lines[line_number + i:]):
                    if i != 0 and count_spaces(m) == spaces:
                        end_line_number = line_number + i
                        break
                if end_line_number is not None:
                    break
                if end_line_number is None:
                    end_line_number = len(lines)+1
                    break
            line_number = end_line_number
            function_names[-1]['end_line'] = end_line_number

            # print(function_names)
            continue
        # else:
        #     line_number += 1
        #     continue

        if is_first_func is False and line.startswith("func"):
            for i, l in enumerate(lines[line_number:]):
                spaces = count_spaces(l)

                for i, m in enumerate(lines[line_number + i:]):
                    if i != 0 and count_spaces(m) == spaces:
                        end_line_number = line_number + i
                        break
                if end_line_number is not None:
                    break
                if end_line_number is None:
                    end_line_number = len(lines)+1
                    break
            line_number = end_line_number
            continue

    # Check for function calling
    if len(function_names) != 0:
        repeater += 1
        if repeater % 2 == 1:
            now_line = line_number
            for i, func in enumerate(function_names):
                if func['name'] in line:
                    line_number = func['label'] + 1
                    # value = line.split(func['name'])[1].split('(')[1].split(')')[0].strip()
                    # Run function with arguments and different variables from global variables
                    # run_function(line, func['args'], label_line_numbers, operators, line_number, func['end_line'],lines,value)
                    # line_number = func['end_line']
                    # break
                    is_function = 1
                    break

                else:
                    # end
                    line_number += 1
        else:
            line_number = now_line + 1
        continue

    else:
        line_number += 1