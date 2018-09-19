from listener import MatexASTVisitor
from node.BinaryOperator import BinaryOperator


class Subtraction(BinaryOperator):

    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs, '-', None)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_subtraction(self)
