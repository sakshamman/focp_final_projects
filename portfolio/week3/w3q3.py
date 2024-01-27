#check 

while True:
    password1 = input("Enter a new password (8-12 characters): ")
    password2 = input("Confirm your new password: ")

    if len(password1) >= 8 and len(password1) <= 12 and password1 == password2:
        print("Password Set")
        
    else:
        if len(password1) < 8 or len(password1) > 12:
            print("Error: Password length should be between 8 and 12 characters.")
        else:
            print("Error: Passwords do not match. Please try again.")
