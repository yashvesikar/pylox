from token_type import TokenType as tk
from pylox_token import Token
from error import error


class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens = []

        # Keep track of where in the source code the scanner is
        self.start = 0
        self.current = 0
        self.line = 1

        self.token_map = {
            r'(': tk.LEFT_PAREN,
            r')': tk.RIGHT_PAREN,
            r'{': tk.LEFT_BRACE,
            r'}': tk.RIGHT_BRACE,
            r',': tk.COMMA,
            r'.': tk.DOT,
            r'-': tk.MINUS,
            r'+': tk.PLUS,
            r';': tk.SEMICOLON,
            r'*': tk.STAR,
            r' ': None,
            '\r': None,
            '\t': None,
            'and': tk.AND,
            'class': tk.CLASS,
            'else': tk.ELSE,
            'false': tk.FALSE,
            'for': tk.FOR,
            'fun': tk.FUN,
            'if': tk.IF,
            'nil': tk.NIL,
            'or': tk.OR,
            'print': tk.PRINT,
            'return': tk.RETURN,
            'super': tk.SUPER,
            'this': tk.THIS,
            'true': tk.TRUE,
            'var': tk.VAR,
            'while': tk.WHILE
        }

    def is_at_end(self) -> bool:
        # False if not at the end
        # True if at the end
        return self.current >= len(self.source)

    def scan_tokens(self):

        while not self.is_at_end():
            # We are at the beginning of the next lexeme. 
            self.start = self.current  # Update the start
            self.scan_token()  # Scan the next token

        self.tokens.append(Token(tk.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        # Scan current character, move current up by one
        c = self.source[self.current]
        self.current += 1

        val = None

        # If block to get value of lexeme, unary and more complex lexemes
        # Unary lexemes
        if c in self.token_map:
            val = self.token_map[c]
        # binary lexemes/conditional, single char lookahead
        elif c == '!':
            val = tk.BANG_EQUAL if self.match(r'=') else tk.BANG
        elif c == '<':
            val = tk.LESS_EQUAL if self.match(r'=') else tk.LESS
        elif c == '>':
            val = tk.GREATER_EQUAL if self.match(r'=') else tk.GREATER
        elif c == '=':
            val = tk.EQUAL_EQUAL if self.match(r'=') else tk.EQUAL
        elif c == '/':
            val = tk.SLASH if self.match_slash() else None
        # Strings
        elif c == '"':
            while self.peek() != '"' and not self.is_at_end():
                if self.peek() == '\n':
                    self.line += 1
                self.advance()

            if self.is_at_end():
                error(self.line, "Unterminated string.")
                return

            # closing, pass the last element in the string '"'
            self.advance()

            val = (tk.STRING, self.source[self.start + 1: self.current - 1])
        # New lines
        elif c == '\n':
            # Increment the count of line
            self.line += 1
        else:
            if self.is_digit(c):
                # Numbers, floating point at runtime - supports integer and decimal literals
                # Supports 1234, 12.34
                # Does not support .1234 or 1234.

                while self.is_digit(self.peek()) and not self.is_at_end(): self.advance()

                # If it is a decimal number
                if self.peek() == '.' and self.is_digit(self.peek(k=1)): self.advance()

                while self.is_digit(self.peek()) and not self.is_at_end(): self.advance()

                val = (tk.NUMBER, self.string_to_int(self.source[self.start: self.current]))

            elif self.is_alpha(c):
                while self.is_alphanumeric(self.peek()): self.advance()
                text = self.source[self.start: self.current]
                tok_type = self.token_map.get(text, tk.IDENTIFIER)
                val = (tok_type, text)

            else:
                error(self.line, "Unexpected character.")

        # If val is a valid lexeme, add it to the tokens list
        if val:
            # Lexemes with literal value
            if isinstance(val, tuple):
                self.add_token(val[0], val[1])
            # No literal value
            else:
                self.add_token(val)

    def add_token(self, token_type: tk, literal: object = None) -> None:
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def peek(self, k=0):
        """
        Allows lookahead, max lookaead of 2 chars
        :param k: number of chars to lookahead
        0 -> lookahead of 1 char
        1 -> lookagead of 2 chars
        :return:
        """
        assert 0 <= k <= 1
        if self.is_at_end():
            return ''
        elif k and self.current < len(self.source):
            return self.source[self.current + k]
        else:
            return self.source[self.current]

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def match(self, expected: str):
        if self.is_at_end(): return False
        if self.source[self.current] != expected: return False

        self.current += 1
        return True

    def match_slash(self):
        # If the second character is a slash then the token is a comment //
        # and the rest of the line should be ignored
        if self.match(r'/'):
            while self.peek() != '\n' and not self.is_at_end():
                self.advance()
        else:
            return True

    def is_digit(self, d):
        try:
            return '0' <= d <= '9'
        except TypeError:
            return False

    def is_alpha(self, c):

        return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or c == '_'

    def is_alphanumeric(self, ch):
        return self.is_alpha(ch) or self.is_digit(ch)

    @staticmethod
    def string_to_int(value:str) -> float:
        power = 0   # power of 10 to multiply for
        length = len(value) # Length of the number string
        offset = 0  # Offset if number is a decimal
        number = 0  # Number to return/number in string

        # Read the number from the least significant digit first
        while length > 0:
            if value[length - 1] == '.':  # If decimal, store the offset
                offset = power
            # For every digit, cast to int and add to number, incrememt power
            else:
                digit = int(value[length - 1]) * 10 ** power
                number += digit
                power += 1

            length -= 1

        number = number/(10**offset)  # Update to decimal if necessary
        return number

if __name__ == "__main__":
    print(Scanner.string_to_int("123.4"))