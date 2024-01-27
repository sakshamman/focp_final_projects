'''2. The Unix diff command compares two files and reports the differences, if any.
Write a simple implementation of this that takes two file names as command-line
arguments and reports whether or not the two files are the same. (Define "same" as
having the same contents.)
'''

import sys

def file_diff(file_path1, file_path2):
    try:
        with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

            if content1 == content2:
                print("The files are the same.")
            else:
                print("The files are different.")

    except FileNotFoundError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff_command.py <file1> <file2>")
    else:
        file1_path = sys.argv[1]
        file2_path = sys.argv[2]
        file_diff(file1_path, file2_path)
