from listener import MatexASTVisitor
from node.BinaryOperator import BinaryOperator


class Division(BinaryOperator):

    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs, '/', None)

    def __str__(self):
        return '\\frac{{{}}}{{{}}}'.format(self.lhs, self.rhs)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_division(self)
