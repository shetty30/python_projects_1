import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    # start with lowercase letters
    characters = list(string.ascii_lowercase)

    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_symbols:
        characters += list(string.punctuation)

    
    if not characters:
        return "Error: no character sets selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Password Generator 🔐")

    try:
        length = int(input("Enter password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_digits, use_symbols)
        print(f"\nYour secure password is:\n👉 {password}")

    except ValueError:
        print("⚠️ Please enter a valid number for length.")

if __name__ == "__main__":
    main()
