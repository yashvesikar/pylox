from enum import Enum
from enum import auto

class TokenType(Enum) :
    # Single-character tokens.                      
    LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE = 0, 1, 2, 3
    COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR = 4, 5, 6, 7, 8, 9, 10

    # One or two character tokens.                  
    BANG, BANG_EQUAL = auto(), auto()
    EQUAL, EQUAL_EQUAL = auto(), auto()
    GREATER, GREATER_EQUAL = auto(), auto()  
    LESS, LESS_EQUAL = auto(), auto()    

    # Literals.                                     
    IDENTIFIER, STRING, NUMBER = 21, 22, 23

    # Keywords.                                     
    AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR = 24, 25, 26, 27, 28, 29, 30, 31, 32
    PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE = 33, 34, 35, 36, 37, 38, 39

    EOF = 40