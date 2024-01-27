'''6. Write a program that decrypts messages encoded as above.'''

def decrypt_message(encrypted_message, interval):
    decrypted_message = ''
    index = 0

    for char in encrypted_message:
        if char.isalpha():
            if index % interval == 0:
                decrypted_message += char
            index += 1
        else:
            decrypted_message += char

    return decrypted_message

# Example usage:
encrypted_message = "sxyexynxydxy cxyhxyexyexysxye"
interval_used = 2  # Replace with the actual interval used
decrypted = decrypt_message(encrypted_message, interval_used)
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted}")
