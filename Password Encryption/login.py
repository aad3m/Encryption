import database
import encrypt
from components import customize

color = customize.color

MAX_LOGIN_ATTEMPTS = 3


def get_user_input(prompt, return_to_menu=True):
    while True:
        user_input = input(prompt)
        if return_to_menu and user_input == '1':
            print(f'{color.YELLOW}Returning to Menu...{color.END}')
            return None
        else:
            return user_input


def handle_invalid_login_attempts():
    print(f'{color.RED}Invalid Login, Double-check your username and password.{color.END}')


def login():
    print(color.BOLD + '* Press 1 at any time to return to the menu *' + color.END)
    print(f'{color.DARKCYAN}Welcome back, login to proceed!{color.END}')

    for _ in range(MAX_LOGIN_ATTEMPTS):

        username = get_user_input(f"{color.CYAN}Username: ")

        if username is None:
            return

        if username not in database.users_db:
            print(f'{color.RED}Username not found. Exiting login.{color.END}')
            return

        password = get_user_input(f"Password: {color.END}")
        encrypted_password = encrypt.encrypt(password)

        is_valid_login, user_data = verify_password(username, encrypted_password)

        if is_valid_login:
            user_name = user_data.get('name', 'User')
            print(f'Welcome back, {color.DARKCYAN}{user_name}{color.END}.')
            return
        else:
            handle_invalid_login_attempts()

    print(f'{color.RED}Too many attempts, please try again later.{color.END}')


def verify_password(username, password):
    users_db = database.users_db

    if username in users_db and password == users_db[username]['password']:
        return True, users_db[username]

    return False, None


if __name__ == '__main__':
    login()
