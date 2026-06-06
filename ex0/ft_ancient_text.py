import io
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file_open = open(sys.argv[1])
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        io.read()
    else:
        print("Usage: ft_ancient_text.py <file>")
