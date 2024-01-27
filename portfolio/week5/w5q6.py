'''6. Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs.
'''

import sys
import shutil

def create_backup(input_file):
    try:
        # Create a backup filename by adding "_backup" before the extension
        backup_file = input_file.replace('.', '_backup.')

        # Copy the contents of the original file to the backup file
        shutil.copy2(input_file, backup_file)

        print(f"Backup created successfully: {backup_file}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_backup.py <filename>")
    else:
        input_file = sys.argv[1]
        create_backup(input_file)
