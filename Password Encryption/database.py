import encrypt
from customize import color

# Database where users are saved
filename = 'user_database.txt'


def load_users():
    global filename

    # place file contents into a list.
    # each list element corresponds to 1 line in the file
    f = open(filename, 'r')
    text = f.read().splitlines()
    f.close()

    # place user(key) - (password, name)(value) pairs in a dictionary
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

    # open file with overwrite
    with open(filename, 'w') as f:
        # iterates over user.txt using load users function
        for username, user_data in users_db.items():
            encrypted_password = user_data['password']
            name = user_data.get('name', ' ')
            # writes user added username, password, and name
            f.write(f'{username} {encrypted_password} {name}\n')


def get_user_input(prompt, return_to_menu=True):
    while True:
        user_input = input(prompt)
        if return_to_menu and user_input == '1':
            print(color.YELLOW + 'Returning To Menu...' + color.END)
            return None
        else:
            return user_input


def add_account():
    print(color.BOLD + '* Press 1 at any time to return to the menu *' + color.END)
    while True:
        # Get name from the user
        name = input(color.CYAN + "What's your name? " + color.END)
        # Check if the user wants to return to the menu
        if name == '1':
            print(color.YELLOW + 'Returning to Menu...' + color.END)
            return
        # Break out of the loop if the name is valid
        if len(name) <= 30:  # You can adjust the maximum length as needed
            break
        else:
            print(color.BOLD + color.RED + 'Name criteria is not met. Maximum length is 30 characters.' + color.END)

    while True:
        # Get username from the user
        print(color.PURPLE + '\n Username Criterias:'
                             '\n1. No more than 20 characters'
                             '\n2. Atleast 6 characters ' + color.END)
        username = input(color.CYAN + 'Enter a username: ' + color.END)
        # Check if the user wants to return to the menu
        if username == '1':
            print(color.YELLOW + 'Returning to Menu...' + color.END)
            return
        # Check if the username is within the required length
        if 6 <= len(username) <= 20:
            # Check if the username is already taken
            if username in users_db:
                print(color.BOLD + color.RED + 'Username is already taken. Choose another username.' + color.END)
            else:
                break  # Break out of the loop if the username is valid and not taken
        else:
            print(color.BOLD + color.RED + 'Username criteria is not met.' + color.END)

    while True:
        # Get password from the user
        print(color.PURPLE + '\nPassword Criterias:'
              '\n1. No more than 16 characters long'
              '\n2. No Spaces'
              '\n3. At least one special character' + color.END)
        password = input(color.CYAN + 'Enter a password: ' + color.END)
        # Check if the user wants to return to the menu
        if password == '1':
            print(color.YELLOW + 'Returning to Menu...' + color.END)
            return
        # Check if the password is within the required length
        if 6 <= len(password) <= 16:
            # Encrypt the password for the database
            encrypted_password = encrypt.encrypt(password)
            if not any(char in "!@#$%^&*()-+?_=,<>/;:'\"[]{}|\\" for char in password):
                print('Not a valid password. Choose another password.')
            else:
                break  # Break out of the loop if the password is valid
        else:
            print(color.BOLD + color.RED + 'Not a valid password. Choose another password.' + color.RED)

    # Pair the encrypted username with the encrypted password and name in the users_db
    users_db[username] = {'password': encrypted_password, 'name': name}
    # Write the updated users database to the file
    write_users()
    print(f'Thank You {color.PURPLE}{name}{color.END} your account was created. '
          f'\nUsername: ' + color.BOLD + color.PURPLE + username + color.END)
    return username, encrypted_password


# Used for other files
users_db = load_users()

if __name__ == '__main__':
    add_account()
