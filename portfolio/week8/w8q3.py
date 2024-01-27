'''3. The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string.
'''

import sys

def grep_pattern(pattern, file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line.strip())

    except FileNotFoundError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep_command.py <pattern> <file>")
    else:
        pattern_to_search = sys.argv[1]
        file_path = sys.argv[2]
        grep_pattern(pattern_to_search, file_path)
