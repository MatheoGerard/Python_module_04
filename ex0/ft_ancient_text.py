import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file_open: typing.TextIO = open(sys.argv[1])
            print("---")
            print()
            print(file_open.read())
            print()
            print("---")
            file_open.close()
            print(f"File '{file_open.name}' closed.")
        except FileNotFoundError as e:
            print(f"\033[31mError opening file '{sys.argv[1]}': {e}\033[0m")
        except PermissionError as e:
            print(f"\033[31mError opening file '{sys.argv[1]}': {e}\033[0m")
    else:
        print("\033[31mUsage: ft_ancient_text.py <file>\033[0m")
