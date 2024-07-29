# Password Encryption System


The Password Encryption System is a tool for managing user accounts with encrypted passwords. It includes features for user registration, login, and file validation.

## Features

- **User Registration:** Allows users to create accounts with encrypted passwords.
- **Login System:** Authenticates users with their encrypted credentials.
- **File Checker:** Validates the format and content of the user database file.
- **About Section:** Provides information about the system.

## Components

### `database.py`

Handles user data storage and retrieval, including:
- Loading and saving user data from `user_database.txt`.
- Creating and verifying user accounts.
- Encrypting passwords.

### `encrypt.py`

Performs password encryption through:
- Salting the password.
- Converting it into a bitstream.
- Encoding it into a hexadecimal string.
- Transforming it into ASCII characters.

### `filecheck.py`

Validates the `user_database.txt` file by checking:
- Consecutive blank lines.
- Correct number of fields per line.

### `login.py`

Manages user login, including:
- Validating login attempts.
- Encrypting and verifying passwords.

### `menu.py`

Provides an interactive menu for:
- Logging in.
- Registering new accounts.
- Viewing system information.
- Exiting the application.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/password-encryption.git

2. **Navigate to the project directory:**
    ```
    cd password-encryption 
    ```

3. **Install any required dependencies:**
    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```sh
    python menu.py
    ```
2. **Interact with the menu:**
   - Log in with an existing account.
   - Register a new account.
   - View information about the system.
   - Exit the application.

## Configuration
- user_database.txt: The file where user data is stored. Ensure it follows the required format.

## Contributing
Feel free to submit issues, enhancements, or pull requests. Please follow the standard contribution guidelines.

## License
This project is licensed under the [MIT License](LICENSE.md).