import hashlib
import getpass

def hash_password(password):
    # Using hashlib to hash the password (you can use a stronger hashing algorithm)
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_input(prompt, hide_input=False):
    if hide_input:
        return getpass.getpass(prompt)
    else:
        return input(prompt)
