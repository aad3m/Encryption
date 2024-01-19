import database
import encrypt
from customize import color


def get_user_input(prompt, return_to_menu=True):
    while True:
        user_input = input(prompt)
        if return_to_menu and user_input == '1':
            print(f'{color.YELLOW}Returning to Menu...{color.END}')
            return None
        else:
            return user_input


def login():
    # give user 3 attempts
    for _ in range(3):
        print(color.BOLD + '* Press 1 at any time to return to the menu *' + color.END)
        print(f'{color.DARKCYAN} Welcome back, login to proceed!{color.END}')
        # username and password
        username = get_user_input(f"{color.CYAN}Username: ")

        # Check if the username is in the database or if the user wants to return to the menu
        if username is None:
            return

        if username not in database.users_db:
            print(f'{color.RED}Username not found. Exiting login.{color.END}')
            return

        password = get_user_input(f"Password: {color.END}")
        # encrypt the password
        encrypted_password = encrypt.encrypt(password)
        # define verify_password to validate login
        valid, user_data = verify_password(username, encrypted_password)
        # if login correct
        if valid:
            user_name = user_data.get('name', 'User')  # Get the user's name or use a default if not available
            print(f'Welcome back, {color.DARKCYAN}{user_name}{color.END}.')
            return
        # if login wrong
        else:
            print(f'{color.RED}Invalid Login, Double-check your username and password {color.END}')

    # lock account after 3 attempts
    print(f'{color.RED}Too many attempts, please try again later. {color.END}')


def verify_password(username, password):
    # define users_db from the database for easier handling
    users_db = database.users_db

    # compare username and password to one from the user database
    if username in users_db and password == users_db[username]['password']:
        return True, users_db[username]

    return False, None


if __name__ == '__main__':
    login()
