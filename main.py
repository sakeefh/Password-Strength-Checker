import string
import re

def check_password_strength(password):
    # Define character types using regex
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'[0-9]')
    special_regex = re.compile(r'[{}]'.format(re.escape(string.punctuation)))

    # Check for character types
    character_types = [bool(uppercase_regex.search(password)),
                       bool(lowercase_regex.search(password)),
                       bool(digit_regex.search(password)),
                       bool(special_regex.search(password))]

    # Calculate password length
    length = len(password)

    # Check if password is in common list
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        common_passwords = f.read().splitlines()
    
    if password in common_passwords:
        print("Your password was found in the common list. Score 0 / 7")
        return

    # Calculate score based on length
    score = 0
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length >= 24:
        score += 1

    # Calculate score based on character types
    score += sum(character_types)

    # Print password details
    print(f"Password length is {length}, adding {score} points!")
    print(f"Password contains {sum(character_types)} different character types.")

    # Calculate entropy (optional)

    # Print password strength score
    if score < 4:
        print(f"Your Password Score: {score} / 7")
    elif score == 4:
        print(f"Your Password Score: {score} / 7")
    elif 4 < score < 6:
        print(f"Your Password Score: {score} / 7")
    elif score > 6:
        print(f"Your Password Score: {score} / 7")

# Main program
if __name__ == "__main__":
    password = input("Enter the password: ")
    check_password_strength(password)
