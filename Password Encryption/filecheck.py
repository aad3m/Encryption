def check_user_database():
    # Configuration parameters
    max_blank_lines = 1  # Maximum allowed consecutive blank lines
    expected_fields = 2  # Expected number of fields per line
    data = 'user_database.txt'  # File to be checked

    # Initialize variables
    consecutive_blank_lines = 1
    errors = []

    try:
        # Read lines from the file
        with open(data, 'r') as f:
            lines = f.readlines()

        # Check for consecutive blank lines
        for line_number, line in enumerate(lines, start=1):
            if line.isspace():
                consecutive_blank_lines += 1
            else:
                consecutive_blank_lines = 0

            # Report error if more than the allowed consecutive blank lines
            if consecutive_blank_lines > max_blank_lines:
                error_message = (
                    '\033[1m' + '\033[94m' +
                    f"Error: More than {max_blank_lines} consecutive blank lines found in" + ' ''\033[92m' + f'{data}' + '\033[0m' + ' '
                    + '\033[1m' + '\033[94m' + f"starting from line {line_number - consecutive_blank_lines + 1}."
                )
                errors.append(error_message)

            # Split line into fields and check for the expected number of fields
            fields = line.strip().split(' ')
            if len(fields) != expected_fields:
                error_message = (
                    '\033[1m' + '\033[94m' +
                    f"Error in line {line_number}: {line.strip()}. "
                    f"Expected {expected_fields} fields, but found {len(fields)} fields." + '\033[0m'
                )
                errors.append(error_message)

        # Raise exception with all error messages if any
        if errors:
            raise ValueError("\n".join(errors))

        # If no errors, print success message
        print("All checks completed. No errors found.")

    except ValueError as e:
        # Print error messages and exit with a non-zero code
        print(f"Errors were found: \n{e}")
        exit(1)

# Execute the check_user_database function if the script is run directly
if __name__ == '__main__':
    check_user_database()
