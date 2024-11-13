import secrets
import string

# Configuration settings
count = 48  # Number of passwords to generate
length = 19  # Desired password length
use_uppercase = True  # Include uppercase letters
use_lowercase = True  # Include lowercase letters
use_digits = True  # Include digits
use_special = True  # Include special symbols


def generate_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_special):
    # Define character pools based on user preferences
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    # Generate passwords using cryptographically secure random values
    passwords = []
    for _ in range(count):
        if character_pool:
            password = ''.join(secrets.choice(character_pool) for _ in range(length))
            passwords.append(password)
        else:
            passwords.append('')  # Empty password if no character types selected

    return passwords


# Generate passwords
passwords = generate_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_special)

# Save passwords to a file
with open("pswd.txt", "w") as file:
    for i, password in enumerate(passwords, start=1):
        file.write(f"{password}\n")

print("Passwords have been generated securely and saved to 'pswd.txt'.")
