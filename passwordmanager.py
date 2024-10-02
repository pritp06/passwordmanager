import os
import json

# File to store passwords
PASSWORD_FILE = 'passwords.json'


def load_passwords():
    """Load passwords from a file."""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_passwords(passwords):
    """Save passwords to a file."""
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file)


def add_password(service, password):
    """Add a new password for a service."""
    passwords = load_passwords()
    passwords[service] = password
    save_passwords(passwords)
    print(f"Password for '{service}' added successfully!")


def get_password(service):
    """Retrieve a password for a service."""
    passwords = load_passwords()
    if service in passwords:
        print(f"Password for '{service}': {passwords[service]}")
    else:
        print(f"No password found for '{service}'.")


def delete_password(service):
    """Delete a password for a service."""
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f"Password for '{service}' deleted successfully!")
    else:
        print(f"No password found for '{service}'.")


def list_passwords():
    """List all stored passwords."""
    passwords = load_passwords()
    if passwords:
        print("Stored passwords:")
        for service, password in passwords.items():
            print(f" - {service}: {password}")
    else:
        print("No passwords stored.")


def main():
    print("Welcome to the Password Manager!")

    while True:
        print("\nOptions:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. List Passwords")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            add_password(service, password)

        elif choice == '2':
            service = input("Enter the service name: ")
            get_password(service)

        elif choice == '3':
            service = input("Enter the service name: ")
            delete_password(service)

        elif choice == '4':
            list_passwords()

        elif choice == '5':
            print("Exiting the Password Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please select between 1 and 5.")


if __name__ == "__main__":
    main()
