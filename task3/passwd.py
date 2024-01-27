from password_utils import hash_password, get_user_input

def passwd():
    username = get_user_input("User: ").strip()
    current_password = hash_password(get_user_input("Current Password: ", hide_input=True).strip())
    new_password = hash_password(get_user_input("New Password: ", hide_input=True).strip())
    confirm_password = hash_password(get_user_input("Confirm: ", hide_input=True).strip())

    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    found = False
    with open("passwd.txt", "w") as file:
        for line in lines:
            parts = line.strip().split(":")
            if parts[0] == username:
                found = True
                if parts[2] == current_password:
                    if new_password == confirm_password:
                        file.write(f"{username}:{parts[1]}:{new_password}\n")
                        print("Password changed.")
                    else:
                        print("Passwords do not match. Nothing changed.")
                else:
                    print("Invalid current password. Nothing changed.")
            else:
                file.write(line)

    if not found:
        print("User not found. Nothing changed.")

if __name__ == "__main__":
    passwd()
