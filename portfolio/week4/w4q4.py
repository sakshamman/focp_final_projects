'''4.When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)'''

def remove_last_character(input_string):
    if len(input_string) > 1:
        return input_string[:-1]  # Return the string excluding the last character..,, #Slicing method use gareko 
    else:
        return input_string  # Return the input string unchanged if it contains one or fewer characters

# Get user input
user_input = input("Enter a string: ")

# Call the function with user input
result = remove_last_character(user_input)

# Display the result
print(f"Modified string: {result}")

