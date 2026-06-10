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
            text_in_file: str = file_open.read()
            print(text_in_file)
            print("---")
            file_open.close()
            print(f"File '{file_open.name}' closed.")
            print()
            print("Transform data:")
            print("---")
            i: int = 0
            for line in text_in_file:
                if line != "\n":
                    print(line, end="")
                else:
                    print("#")
                i += 1
            if text_in_file[i - 1] != "\n":
                print("#")
        except FileNotFoundError as e:
            print(f"\033[31mError opening file '{sys.argv[1]}': {e}\033[0m")
        except PermissionError as e:
            print(f"\033[31mError opening file '{sys.argv[1]}': {e}\033[0m")
    else:
        print("\033[31mUsage: ft_ancient_text.py <file>\033[0m")
