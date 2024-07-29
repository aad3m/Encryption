from components import customize

color = customize.color

# Configuration Constants
MAX_BLANK_LINES = 1
EXPECTED_FIELDS = 3
DATA_FILE = 'user_database.txt'


def check_consecutive_blank_lines(lines):
    consecutive_blank_lines = 0
    errors = []

    for line_number, line in enumerate(lines, start=1):
        if line.isspace():
            consecutive_blank_lines += 1
        else:
            consecutive_blank_lines = 0

        if consecutive_blank_lines > MAX_BLANK_LINES:
            error_message = (
                f"{color.BOLD}{color.RED}Error: More than {MAX_BLANK_LINES} consecutive blank lines found in"
                f" {color.GREEN}{DATA_FILE}{color.RED} starting from line {line_number - consecutive_blank_lines + 1}.{color.END}"
            )
            errors.append(error_message)

    return errors


def check_fields(lines):
    errors = []

    for line_number, line in enumerate(lines, start=1):
        fields = line.strip().split(' ')
        if len(fields) != EXPECTED_FIELDS:
            error_message = (
                f"{color.BOLD}{color.RED}Error in line {line_number}: {line.strip()}. "
                f"Expected {EXPECTED_FIELDS} fields, but found {len(fields)} fields.{color.END}"
            )
            errors.append(error_message)

    return errors


def check_user_database():
    try:
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()

        consecutive_blank_lines_errors = check_consecutive_blank_lines(lines)
        fields_errors = check_fields(lines)

        all_errors = consecutive_blank_lines_errors + fields_errors

        if all_errors:
            raise ValueError("\n".join(all_errors))

        print(f"{color.GREEN}{color.BOLD}All checks completed. No errors found.{color.END}")

    except ValueError as e:
        print(f"{color.RED}{color.BOLD}Errors were found:\n{e}{color.END}")
        exit(1)

    finally:
        if 'f' in locals():
            f.close()


if __name__ == '__main__':
    check_user_database()
