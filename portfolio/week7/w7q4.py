'''4. One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes.'''

def frequency_analysis(message):
    # Initialize a dictionary to store letter frequencies
    letter_counts = {}

    # Process each character in the message
    for char in message:
        if char.isalpha():  # Ignore non-alphabetic characters
            char_lower = char.lower()  # Convert to lowercase for case-insensitivity
            letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1

    # Sort the dictionary by values in descending order
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    # Display the six most common letters and their counts
    print("Six most common letters:")
    for letter, count in sorted_counts[:6]:
        print(f"{letter}: {count}")

# Example usage:
encrypted_message = "Sxyexynxydxy cxyhxyexyexysxye"
frequency_analysis(encrypted_message)
