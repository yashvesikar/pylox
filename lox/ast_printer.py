from lox.expr import Visitor

class AstPrinter(Visitor):

    def __init__(self):
        super().__init__()

    def pretty_print(self, expr):
        return expr.accept(self)

    def visit_Binary_Expr(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_Grouping_Expr(self, expr):
        return self.parenthesize("group", expr.expression)

    def visit_Literal_Expr(self, expr):
        if expr.value is None: return None
        else:
            return str(expr.value)

    def visit_Unary_Expr(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *args):
        builder = ""
        builder += f"({name}"

        for expr in args:
            builder += f" {expr.accept(self)}"

        builder += ")"

        return builder