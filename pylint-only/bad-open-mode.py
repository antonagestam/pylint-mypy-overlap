def foo(file_path: str) -> None:
    with open(file_path, "rwx") as file:  # [bad-open-mode]
        contents = file.read()
