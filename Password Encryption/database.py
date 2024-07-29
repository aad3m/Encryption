import encrypt
from components import customize

color = customize.color

# Database where users are saved
filename = 'user_database.txt'

# Constants for criteria
MAX_NAME_LENGTH = 30
MIN_USERNAME_LENGTH = 6
MAX_USERNAME_LENGTH = 20
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 16


def load_users():
    global filename
    with open(filename, 'r') as f:
        text = f.read().splitlines()

    users_db = {}
    for line in text:
        user_data = line.split()
        user = user_data[0]
        password = user_data[1]
        name = user_data[2] if len(user_data) > 2 else None
        users_db[user] = {'password': password, 'name': name}

    return users_db


def write_users():
    global filename
    with open(filename, 'w') as f:
        for username, user_data in users_db.items():
            encrypted_password = user_data['password']
            name = user_data.get('name', ' ')
            f.write(f'{username} {encrypted_password} {name}\n')


def get_name():
    while True:
        name = input(color.CYAN + "What's your name? " + color.END)
        if name == '1':
            print(color.YELLOW + 'Returning to Menu...' + color.END)
            return None
        if len(name) <= MAX_NAME_LENGTH:
            return name
        else:
            print(color.BOLD + color.RED + 'Name criteria not met. Maximum length is 30 characters.' + color.END)


def get_username():
    while True:
        print(color.PURPLE + '\n Username Criteria:'
                             '\n1. No more than 20 characters'
                             '\n2. At least 6 characters ' + color.END)
        username = input(color.CYAN + 'Enter a username: ' + color.END)
        if username == '1':
            print(color.YELLOW + 'Returning to Menu...' + color.END)
            return None
        if MIN_USERNAME_LENGTH <= len(username) <= MAX_USERNAME_LENGTH:
            if username not in users_db:
                return username
            else:
                print(color.BOLD + color.RED + 'Username is already taken. Choose another username.' + color.END)
        else:
            print(color.BOLD + color.RED + 'Username criteria not met.' + color.END)


def get_password():
    while True:
        print(color.PURPLE + '\nPassword Criteria:'
                             '\n1. No more than 16 characters long'
                             '\n2. No Spaces'
                             '\n3. At least one special character' + color.END)
        password = input(color.CYAN + 'Enter a password: ' + color.END)
        if password == '1':
            print(color.YELLOW + 'Returning to Menu...' + color.END)
            return None
        if MIN_PASSWORD_LENGTH <= len(password) <= MAX_PASSWORD_LENGTH:
            if any(char in "!@#$%^&*()-+?_=,<>/;:'\"[]{}|\\" for char in password):
                return encrypt.encrypt(password)
            else:
                print(color.BOLD + color.RED + 'Not a valid password. Choose another password.' + color.RED)
        else:
            print(color.BOLD + color.RED + 'Not a valid password. Choose another password.' + color.RED)


def add_account():
    print(color.BOLD + '* Press 1 at any time to return to the menu *' + color.END)

    name = get_name()
    if name is None:
        return

    username = get_username()
    if username is None:
        return

    encrypted_password = get_password()
    if encrypted_password is None:
        return

    users_db[username] = {'password': encrypted_password, 'name': name}
    write_users()

    print(f'Thank You {color.PURPLE}{name}{color.END} your account was created. '
          f'\nUsername: {color.BOLD}{color.PURPLE}{username}{color.END}')


# Used for other files
users_db = load_users()

if __name__ == '__main__':
    add_account()
