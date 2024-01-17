# These functions are the LEVEL UP requirements

import database
import encrypt
from customize import color


def login():
    # define i
    i = 3
    # give user 3 attempts
    while i > 0:
        print(f'{color.DARKCYAN} Welcome back login to proceed!{color.END}')
        # username and password
        username = input(f"{color.CYAN}Username: ")
        password = input(f"Password: {color.END}")
        # encrpt the password
        encrypted_password = encrypt.encrypt(password)
        # encrypt the username
        encrypted_username = encrypt.encrypt(username)
        # define verify_password to validated login
        valid = verify_password(encrypted_username, encrypted_password)
        # if login correct
        if valid:
            print('Welcome back ' + color.DARKCYAN + username + color.END + '.')
            i = -1
        # if login wrong
        else:
            print(f'{color.RED}Invalid Login, Double check your username and password {color.END}')
            i -= 1
    # lock account after 3 attempts
    if i == 0:
        print(f'{color.RED}Too many attempts, please try again later. {color.END}')


def verify_password(username, password):
    # define users_db from database for easier handling
    users_db = database.users_db

    # compare username and password to one from user database
    if username in users_db and password == users_db[username]:
        return True

    return False



if __name__ == '__main__':


    login()
