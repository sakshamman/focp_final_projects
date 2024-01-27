''' 2.Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.
'''
    
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Get user input
user_input = input("Enter a string: ")

# Call the function with user input
upper, lower = count_upper_lower(user_input)

# Display the counts of uppercase and lowercase letters
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")


''' # You can also use this function for easy understanding
def count_upper_lower(string):
    # Initialize counters for uppercase and lowercase letters
    upper_count = 0
    lower_count = 0

    # Iterate through each character in the string
    for char in string:
        # Check if the character is uppercase
        if char.isupper():
            # Increment the count of uppercase letters
            upper_count += 1
        # Check if the character is lowercase
        elif char.islower():
            # Increment the count of lowercase letters
            lower_count += 1
    
    # Return the counts of uppercase and lowercase letters as a tuple
    return upper_count, lower_count
'''

