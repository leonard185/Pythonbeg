import random
import string


def generate_password(length=8, include_special_chars=True):
    # Define character sets to generate password from
    if include_special_chars:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


# Function to get user input for password criteria
def get_password_criteria():
    try:
        length = int(input("Enter the length of the password (minimum 6 characters recommended): "))
        include_special_chars = input("Include special characters (e.g., !@#$%&*): [y/n] ").lower() == 'y'

        if length < 6:
            print("Password length should be at least 6 characters.")
            return None, None

        return length, include_special_chars

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")
        return None, None


# Main program to generate password based on user input
def main():
    print("Welcome to the Password Generator!")
    print("This tool will create a random, secure password based on your specified criteria.")

    while True:
        length, include_special_chars = get_password_criteria()
        if length is not None and include_special_chars is not None:
            generated_password = generate_password(length, include_special_chars)
            print(f"Generated Password: {generated_password}")
            break


# Run the main program
if __name__ == "__main__":
    main()
