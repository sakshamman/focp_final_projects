''' 1.Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function.'''

def is_in_range(num):
    return 0 <= num <= 100

# Get user input
user_input = int(input("Enter an integer: "))

# Check if the input is within the range and display the result
if is_in_range(user_input):
    print(f"{user_input} is in the range 0 to 100 i.e True")
else:
    print(f"{user_input} is not in the range 0 to 100 i.e False")



