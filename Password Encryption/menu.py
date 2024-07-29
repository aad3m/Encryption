""" Interactive Menu To Access Password Encryption Options"""
from filecheck import check_user_database

try:
    check_user_database()
except ValueError as e:
    print(f'Errors were found: {e}')
    exit()

import time
from database import add_account
from login import login
from components import customize

color = customize.color


def display_menu():
    print(f"{color.GREEN}\nMenu:"
          f"\n1. Login"
          f"\n2. Register"
          f"\n3. About"
          f"\n4. Exit {color.END}")


def about():  # about section
    print(f"\n {color.BOLD}Password Encryption: {color.END}"
          f"{color.CYAN}\n- Encrypts Username & Password "
          "\n- Menu Option "
          "\n- Register System "
          "\n- Login System "
          "\n- File Checker"
          f"\n- User Database {color.END}")


if __name__ == '__main__':

    while True:
        print(f"{color.YELLOW}\nWelcome to the Password Encryption by aad3m! {color.END}")
        display_menu()

        choice = input(f"{color.BOLD}Enter your choice (1/2/3/4): {color.END}")

        if choice == '1':
            login()
            time.sleep(2)
        elif choice == '2':
            result = add_account()
            if result is not None:
                new_user, new_password = result
                time.sleep(3)
        elif choice == '3':
            about()
            time.sleep(3)
        elif choice == "4":
            print(f"{color.YELLOW}Thank you for using Password Encryption by aad3m {color.END}")
            break
        else:
            print(f"{color.RED}Invalid choice. Please enter 1, 2, 3, or 4. {color.END}")
            time.sleep(1.5)
