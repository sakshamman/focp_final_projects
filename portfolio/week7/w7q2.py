'''2. Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.'''

def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))

def letters_in_either_not_both(word1, word2):
    return sorted((set(word1) | set(word2)) - (set(word1) & set(word2)))

# Example usage:
word1 = "hello"
word2 = "world"

print(f"Letters in either word: {letters_in_either(word1, word2)}")
print(f"Letters in both words: {letters_in_both(word1, word2)}")
print(f"Letters in either, but not both: {letters_in_either_not_both(word1, word2)}")
