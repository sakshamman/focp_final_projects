import sys

def spell_checker(file_path, dictionary_path):
    try:
        with open(dictionary_path, 'r') as dict_file:
            dictionary = set(word.strip().lower() for word in dict_file.readlines())

        with open(file_path, 'r') as file:
            words = [word.strip().lower() for line in file for word in line.split()]

        misspelled_words = [word for word in words if word not in dictionary]

        if misspelled_words:
            print("Misspelled words:")
            for misspelled_word in misspelled_words:
                print(misspelled_word)
        else:
            print("No misspelled words found!")

    except FileNotFoundError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python spell_checker.py <file> <dictionary>")
    else:
        file_path = sys.argv[1]
        dictionary_path = sys.argv[2]
        spell_checker(file_path, dictionary_path)
