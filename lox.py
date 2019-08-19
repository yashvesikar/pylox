import sys
from scanner import Scanner
import pprint as pp


class Lox:

    def __init__(self, args) -> None:
        self.had_error = False
        self.tokens = []
        if len(args) > 1:
            raise IOError("Usage: Pylox [script]")
        elif len(args) == 1:
            self.run_file(args[0])
        else:
            self.run_prompt()

    def run_file(self, filename) -> None:
        # Indicate an error in the exit code
        if self.had_error: exit(65)
        try:
            with open(filename) as fp:
                data = fp.read()
                self.run(data)
        except FileNotFoundError:
            print(f"{filename} does not exist")

    def run_prompt(self) -> None:
        cmd = input()
        while cmd:
            cmd = input()
            print(f"> {cmd}")
            self.run(cmd)

            # reset had_error in prompt mode
            self.had_error = False

    def run(self, source) -> None:

        scanner = Scanner(source)
        self.tokens = scanner.scan_tokens()
        pp.pprint(self.tokens)


def error(line, message) -> None:
    report(line, "", message)


def report(line, where, message) -> None:
    raise Exception(f"Line {line} Error {where}: {message}")


if __name__ == "__main__":
    print(sys.argv[1:])
    lox = Lox(sys.argv[1:])
