def foo(file_path: str) -> None:
    with open(file_path) as file:  # [unspecified-encoding]
        contents = file.read()
