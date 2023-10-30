def count_spaces(string):
    count = 0
    for i in range(len(string)):
        if string[i] == " ":
            count += 1
            continue
        break  # Exit the loop once the first character is found
    return count