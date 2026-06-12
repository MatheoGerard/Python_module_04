import sys
import typing


def convert_text(text: str) -> list[str]:
    if not text:
        return []
    convert: list[str] = []
    for line in text:
        if line != "\n":
            convert.append(line)
        else:
            convert.append("#\n")
    if text[-1] != "\n":
        convert.append("#")
    return convert


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        file_open: typing.TextIO | None = None
        file_to_save: typing.TextIO | None = None
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file_open = open(sys.argv[1])
            print("---")
            print()
            text_in_file: str = file_open.read()
            print(text_in_file)
            print()
            print("---")
            file_open.close()
            print(f"File '{file_open.name}' closed.")
            print()
            print("Transform data:")
            print("---")
            print()
            new_text: str = "".join(convert_text(text_in_file))
            print(new_text)
            print()
            print("---")
            print()
            print("Enter new file name (or empty): ", end="")
            sys.stdout.flush()
            saved_name: str = sys.stdin.readline().rstrip("\n")
            if not saved_name:
                print("Not saving data.")
            else:
                print(f"Saving data to '{saved_name}'")
                file_to_save = open(saved_name, "w")
                file_to_save.write(new_text)
                file_to_save.close()
                print(f"Data saved in file '{saved_name}'.")
        except KeyboardInterrupt:
            sys.stderr.write(
                "\033[31m\n[STDERR] Error: interrupt input\033[0m"
            )
        except Exception as e:
            sys.stderr.write(
                "\033[31m[STDERR] Error opening file"
                f" '{sys.argv[1]}': {e}\033[0m"
            )
        finally:
            if file_open:
                file_open.close()
            if file_to_save:
                file_to_save.close()
    else:
        print("\033[31mUsage: ft_ancient_text.py <file>\033[0m")
