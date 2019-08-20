from abc import ABC, abstractmethod

class Expr(ABC):

	def __init__(self):
		pass

	@abstractmethod
	def accept(self, visitor):
		pass

class Visitor(ABC):
	def visit_Binary_Expr(self, expr):
		pass

	def visit_Grouping_Expr(self, expr):
		pass

	def visit_Literal_Expr(self, expr):
		pass

	def visit_Unary_Expr(self, expr):
		pass

class Binary(Expr):
	def __init__(self, left, operator, right):
		super().__init__()
		self.left = left
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		return visitor.visit_Binary_Expr(self)

class Grouping(Expr):
	def __init__(self, expression):
		super().__init__()
		self.expression = expression

	def accept(self, visitor):
		return visitor.visit_Grouping_Expr(self)

class Literal(Expr):
	def __init__(self, value):
		super().__init__()
		self.value = value

	def accept(self, visitor):
		return visitor.visit_Literal_Expr(self)

class Unary(Expr):
	def __init__(self, operator, right):
		super().__init__()
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		return visitor.visit_Unary_Expr(self)


