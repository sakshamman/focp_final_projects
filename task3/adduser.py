from password_utils import hash_password, get_user_input

def adduser():
    username = get_user_input("Enter new username: ").strip()

    # Checking if the username already exists
    with open("passwd.txt", "r") as file:
        if any(line.startswith(f"{username}:") for line in file):
            print("Cannot add. Username already exists.")
            return

    real_name = get_user_input("Enter real name: ").strip()
    password = hash_password(get_user_input("Enter password: ", hide_input=True).strip())

    # Add the new user to the file
    with open("passwd.txt", "a") as file:
        file.write(f"{username}:{real_name}:{password}\n")

    print("User Created.")

if __name__ == "__main__":
    adduser()
