from cryptography.fernet import Fernet
import os
import json

# generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# load the key from a file
def load_key():
    return open("secret.key", "rb").read()

# save the key to a file
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

# decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted

# save passwords to a JSON file
def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# load passwords from a JSON file
def load_passwords():
    if not os.path.exists("passwords.json"):
        return {}
    with open("passwords.json", "r") as file:
        return json.load(file)


def main():
    if not os.path.exists("secret.key"):
        print("Generating a new encryption key...")
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    passwords = load_passwords()

    while True:
        print("\nPassword Manager v1")
        print("1. Add a new password🤺")
        print("2. Retrieve a password👾")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter website name🌐: ")
            password = input("Enter password🔑: ")
            encrypted_password = encrypt_message(password, key)
            passwords[website] = encrypted_password.decode()
            save_passwords(passwords)
            print("Password saved successfully!")

        elif choice == "2":
            website = input("Enter website name🌐: ")
            if website in passwords:
                encrypted_password = passwords[website].encode()
                decrypted_password = decrypt_message(encrypted_password, key)
                print(f"Password for {website}: {decrypted_password}")
            else:
                print("No password found for this website❌.")

        elif choice == "3":
            print("Exiting the Program...")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 3.")
#Run only if it directy run as a program not a module 
if __name__ == "__main__":
    main()
