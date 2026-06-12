def secure_archive(
    file_name: str, mode: int = 1, text_to_write: str = "Message"
) -> tuple[bool, str]:
    if mode == 1:
        try:
            open(file_name)
        except FileNotFoundError as e:
            return (False, str(e))
        except PermissionError as e:
            return (False, str(e))
        content: str = ""
        with open(file_name) as file:
            content = file.read()
        return (True, content)
    elif mode == 2:
        try:
            open(file_name, "w")
        except PermissionError as e:
            return (False, str(e))
        with open(file_name, "w") as file:
            file.write(text_to_write)
        return (True, "Content successfully written to file")
    else:
        return (False, f"{mode} is not correct mode")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    file_state: tuple[bool, str] = secure_archive("/not/existing/file")
    print(file_state)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    file_state = secure_archive("/etc/master.passwd")
    print(file_state)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    file_state = secure_archive("test.txt")
    print(file_state)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    file_state = secure_archive("test.txt", 0, "affiche moi ca stp")
    print(file_state)
