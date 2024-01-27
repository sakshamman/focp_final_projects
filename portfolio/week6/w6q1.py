'''1. Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think!'''

def decimal_to_binary(number):
    # Using built-in bin() function to convert decimal to binary
    binary_representation = bin(number)
    # The result includes '0b' as a prefix, so we remove it
    return binary_representation[2:]

# Example usage:
positive_integer = 10
binary_result = decimal_to_binary(positive_integer)
print(f"The binary representation of {positive_integer} is: {binary_result}")
