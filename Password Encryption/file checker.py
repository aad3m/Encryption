''' This program is used to check minor things before running the code '''


def check_user_database():
    max_blank_lines = 1
    consecutive_blank_lines = 1

    with open('user_database.txt', 'r') as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, start=1):
        if line.isspace():
            consecutive_blank_lines += 1
        else:
            consecutive_blank_lines = 0

        if consecutive_blank_lines > max_blank_lines:
            print(f"Error: More than {max_blank_lines} consecutive blank lines starting from line {line_number - consecutive_blank_lines + 1}.")

if __name__ == '__main__':
    check_user_database()
