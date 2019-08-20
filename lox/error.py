def error(line, message) -> None:
    report(line, "", message)


def report(line, where, message) -> None:
    print(f"ERROR: Line {line} Error {where}: {message}")
    # raise Exception(f"Line {line} Error {where}: {message}")