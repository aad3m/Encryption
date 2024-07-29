from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted.decode()


def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message.encode())
    return decrypted.decode()


if __name__ == '__main__':
    # Uncomment the next two lines only if generating a new key
    # key = generate_key()
    # save_key(key)

    password = 'sMiLe:-)'
    encrypted = encrypt_message(password)
    print(f"Encrypted password: {encrypted}")

    decrypted = decrypt_message(encrypted)
    print(f"Decrypted password: {decrypted}")
