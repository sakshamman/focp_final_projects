# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password (8-12 characters): ")
    password2 = input("Confirm your new password: ")

    if len(password1) >= 8 and len(password1) <= 12:
        if password1 == password2:
            if password1 not in BAD_PASSWORDS:
                print("Password Set")
                break
            else:
                print("Error: Please choose a stronger password. This password is too common.")
        else:
            print("Error: Passwords do not match. Please try again.")
    else:
        print("Error: Password length should be between 8 and 12 characters. Please try again.")
