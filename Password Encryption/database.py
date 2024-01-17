# These functions are the ADVANCED requirements
import encrypt

# Database where users are saved
filename = 'user_database.txt'


def load_users():
    global filename

    # place file contents into a list.
    # each list element corresponds to 1 line in the file
    f = open(filename, 'r')
    text = f.read().splitlines()
    f.close()

    # place user(key) - password(value) pairs in a dictionary
    users_db = {}
    for line in text:
        user = line.split()[0]
        password = line.split()[1]
        users_db[user] = password

    return users_db


def write_users():
    global filename

    # open file with overwite
    with open(filename, 'w') as f:
        # iterates over user.txt using load users function
        for username in users_db:
            encrypted = users_db[username]
            # writes user added username and password
            f.write(f'{username} {encrypted}\n')


def add_account():
    print('Please enter your username and password')
    print('Username no more than 10 characters')

    while True:
        # Get username from the user
        username = input('Enter your username: ')
        # Check if the username is within the required length
        if 8 <= len(username) <= 10:
            # Encrypt the username
            encrypted_username = encrypt.encrypt(username)
            # Check if the username is already taken
            if encrypted_username in users_db:
                print('Username is already taken. Choose another username.')
            else:
                break  # Break out of the loop if the username is valid and not taken
        else:
            print('Username criteria is not met.')

    while True:
        # Get password from the user
        password = input('Enter your password: ')

        # Check if the password is within the required length
        if 6 <= len(password) <= 15:
            # Encrypt the password for the database
            encrypted_password = encrypt.encrypt(password)
            break  # Break out of the loop if the password is valid
        else:
            print('Not a valid password. Choose another password.')

    # Pair the encrypted username with the encrypted password in the users_db
    users_db[encrypted_username] = encrypted_password
    # Write the updated users database to the file
    write_users()
    print(f'Account created successfully. Username: {username}')
    return encrypted_username, encrypted_password,


# used for other files
users_db = load_users()

if __name__ == '__main__':
    add_account()
