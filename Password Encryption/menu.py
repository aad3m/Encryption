import time
from database import add_account
from login import login


def display_menu():  # main menu
    print("\nMenu:")
    print("1. Login")
    print("2. Create a new account")
    print("3. About")
    print("4. Exit")


def about():  # about section
    print("\nPassword Encryption: "
          "\n- Encrypts Username & Password "
          "\n- Menu Option "
          "\n- Create User Logins "
          "\n- Login System "
          "\n- User Database")


if __name__ == '__main__':
    while True:
        print("\nWelcome to the Password Encryption by aad3m!")
        display_menu()

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            login()
            time.sleep(2)
        elif choice == '2':
            new_user, new_password = add_account()
            time.sleep(3)
        elif choice == '3':
            about()
            time.sleep(3)
        elif choice == "4":
            print("Thank you for using Password Encryption by aad3m")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            time.sleep(1.5)
