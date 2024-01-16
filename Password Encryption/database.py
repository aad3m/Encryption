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
    # get username from user
    username = input('Enter your username: ')
    i = 0
    while i == 0:
        # if username is required length
        if 8 <= len(username) <= 10:
            # if it's a dupilcate within db
            if username in users_db:
                print('Username is already taken. Choose another username.')
                username = input('Enter your username: ')
            else:
                i = 1
        # if username isn't required length
        else:
            print('Username criteria is not met. ')
            username = input('Enter your username: ')
    # encrypt username
    username = encrypt.encrypt(username)


    # get password from user
    password = input('Enter your password: ')
    x = 0
    while x == 0:
        # if password is required length
        if 6 <= len(password) <= 15:
            # change to encrypted password for db
            encrypted_password = encrypt.encrypt(password)
            x = 1
        # if password not required length
        else:
            print('Not a valid password. Choose another password. ')
            password = input('Enter your password: ')

    # pairs username with encrypted password into user_db
    users_db[username] = encrypted_password
    # writes users username and password in users.text
    write_users()
    return username, encrypted_password


# used for other files
users_db = load_users()

if __name__ == '__main__':
    add_account()
