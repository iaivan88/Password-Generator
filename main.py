import secrets
import string

# Configuration settings
count = 1000  # Number of passwords to generate
length = 20  # Desired password length
use_uppercase = True  # Include uppercase letters
use_lowercase = True  # Include lowercase letters
use_digits = True  # Include digits
use_special = True  # Include special symbols
excluded_characters = ""  # Characters to exclude (e.g., ":" or "a" or "4")


def generate_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_special, excluded_characters):
    # Define character pools based on user preferences and exclude specified characters
    character_pool = ''
    if use_uppercase:
        character_pool += ''.join([ch for ch in string.ascii_uppercase if ch not in excluded_characters])
    if use_lowercase:
        character_pool += ''.join([ch for ch in string.ascii_lowercase if ch not in excluded_characters])
    if use_digits:
        character_pool += ''.join([ch for ch in string.digits if ch not in excluded_characters])
    if use_special:
        character_pool += ''.join([ch for ch in string.punctuation if ch not in excluded_characters])

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
passwords = generate_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_special,
                               excluded_characters)

# Save passwords to a file
with open("pswd.txt", "w") as file:
    for i, password in enumerate(passwords, start=1):
        file.write(f"{password}\n")

print("Passwords have been generated securely and saved to 'pswd.txt'.")
