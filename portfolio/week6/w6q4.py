def encrypt_message(message):

    no_spaces_message = message.replace(" ", "")
    
    reversed_message = no_spaces_message[::-1]
    
    return reversed_message

test_message = "Hello World!"
print(encrypt_message(test_message)) 