'''Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur'''

def greet_user():
    name = input("Enter your name: ")
    formatted_name = name.title()  # Convert the name to title case
    print(f"Hello, {formatted_name}!")

# Call the function to greet the user
greet_user()
