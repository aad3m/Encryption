# These functions are the LEVEL UP requirements

import database
import encrypt


def login():
    # define i
    i = 3
    # give user 3 attempts
    while i > 0:
        # username and password
        username = input("Username: ")
        password = input("Password: ")
        # encrpt the password
        encrypted_password = encrypt.encrypt(password)
        # encrypt the username
        username = encrypt.encrypt(username)
        # define verify_password to validated login
        valid = verify_password(username, encrypted_password)
        # if login correct
        if valid:
            print('Correct Login')
            i = -1
        # if login wrong
        else:
            print('Wrong Login, Double check your username and password')
            i -= 1
    # lock account after 3 attempts
    if i == 0:
        print('Too many attempts, account has been locked.')


def verify_password(username, password):
    # define users_db from database for easier handling
    users_db = database.users_db

    # compare username and password to one from user database
    if username in users_db and password == users_db[username]:
        return True

    return False



if __name__ == '__main__':


    login()
