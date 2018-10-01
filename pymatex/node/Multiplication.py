from pymatex.listener import MatexASTVisitor
from pymatex.node.BinaryOperator import BinaryOperator


class Multiplication(BinaryOperator):

    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs, '*', None)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_multiplication(self)
