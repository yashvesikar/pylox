from lox.expr import Unary, Binary, Expr, Grouping, Literal, Visitor
from lox.pylox_token import Token
from lox.token_type import TokenType
from lox.ast_printer import AstPrinter

if __name__ == "__main__":
    expression = Binary(
        Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Literal(123)),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(
            Literal(45.67)
        )
    )

    print(AstPrinter().pretty_print(expression))