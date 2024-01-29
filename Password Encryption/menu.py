from filecheck import check_user_database
try:
    check_user_database()
except ValueError as e:
    print(f'Errors were found: {e}')
    exit()


import time
from database import add_account
from login import login
from customize import color

# Constants
LOGIN_CHOICE = '1'
REGISTER_CHOICE = '2'
ABOUT_CHOICE = '3'
EXIT_CHOICE = '4'

def display_menu():
    """Display the menu options."""
    print(f"{color.GREEN}\nMenu:"
          f"\n{LOGIN_CHOICE}. Login"
          f"\n{REGISTER_CHOICE}. Register"
          f"\n{ABOUT_CHOICE}. About"
          f"\n{EXIT_CHOICE}. Exit {color.END}")

def about():
    """Display information about the program."""
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

        choice = input(f"{color.BOLD}Enter your choice ({LOGIN_CHOICE}/{REGISTER_CHOICE}/{ABOUT_CHOICE}/{EXIT_CHOICE}): {color.END}")

        if choice == LOGIN_CHOICE:
            login()
            time.sleep(2)
        elif choice == REGISTER_CHOICE:
            result = add_account()
            if result is not None:
                time.sleep(3)
        elif choice == ABOUT_CHOICE:
            about()
            time.sleep(3)
        elif choice == EXIT_CHOICE:
            print(f"{color.YELLOW}Thank you for using Password Encryption by aad3m {color.END}")
            break
        else:
            print(f"{color.RED}Invalid choice. Please enter {LOGIN_CHOICE}, {REGISTER_CHOICE}, {ABOUT_CHOICE}, or {EXIT_CHOICE}. {color.END}")
            time.sleep(1.5)
