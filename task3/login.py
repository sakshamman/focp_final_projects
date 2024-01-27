from password_utils import hash_password, get_user_input

def login():
    username = get_user_input("User: ").strip()
    password = hash_password(get_user_input("Password: ", hide_input=True).strip())

    with open("passwd.txt", "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if parts[0] == username and parts[2] == password:
                print("Access granted.")
                return

    print("Access denied.")

if __name__ == "__main__":
    login()

