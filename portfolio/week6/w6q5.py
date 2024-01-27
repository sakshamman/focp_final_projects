'''5. Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fifth character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye
'''

import random
import string

def encrypt_message(message):
    interval = random.randint(2, 20)
    encrypted_message = ''

    for i, char in enumerate(message):
        if char.isalpha():
            if (i + 1) % interval == 0:
                encrypted_message += char
            else:
                encrypted_message += random.choice(string.ascii_letters)
        else:
            encrypted_message += char

    return encrypted_message, interval

# Example usage:
original_message = "send cheese"
encrypted, interval_used = encrypt_message(original_message)
print(f"Original Message: {original_message}")
print(f"Encrypted Message: {encrypted}")
print(f"Interval Used: {interval_used}")
