import database
import encrypt
from customize import color

def login():
    # define i
    i = 3
    # give user 3 attempts
    while i > 0:
        print(f'{color.DARKCYAN} Welcome back, login to proceed!{color.END}')
        # username and password
        username = input(f"{color.CYAN}Username: ")
        password = input(f"Password: {color.END}")
        # encrypt the password
        encrypted_password = encrypt.encrypt(password)
        # define verify_password to validate login
        valid, user_data = verify_password(username, encrypted_password)
        # if login correct
        if valid:
            user_name = user_data.get('name', 'User')  # Get the user's name or use a default if not available
            print(f'Welcome back, {color.DARKCYAN}{user_name}{color.END}.')
            i = -1
        # if login wrong
        else:
            print(f'{color.RED}Invalid Login, Double check your username and password {color.END}')
            i -= 1
    # lock account after 3 attempts
    if i == 0:
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
