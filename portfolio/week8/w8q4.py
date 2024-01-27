import sys

def wc_command(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            char_count = sum(len(line) for line in lines)

            print(f"Lines: {line_count}")
            print(f"Characters: {char_count}")

    except FileNotFoundError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc_command.py <file>")
    else:
        file_path = sys.argv[1]
        wc_command(file_path)
