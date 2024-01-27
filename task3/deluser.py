from password_utils import hash_password, get_user_input

def deluser():
    username = get_user_input("Enter username: ").strip()
    password = hash_password(get_user_input("Enter password: ", hide_input=True).strip())

    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    found = False
    with open("passwd.txt", "w") as file:
        for line in lines:
            parts = line.strip().split(":")
            if parts[0] == username and parts[2] == password:
                found = True
            else:
                file.write(line)

    if found:
        print("User Deleted.")
    else:
        print("User not found or incorrect password. Nothing changed.")

if __name__ == "__main__":
    deluser()
