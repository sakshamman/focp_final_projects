import sys

def nl(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}\t{line.strip()}")

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl_command.py <filename>")
    else:
        file_path = sys.argv[1]
        nl(file_path)
