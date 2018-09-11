from .BinaryOperator import BinaryOperator


class Multiplication(BinaryOperator):

    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs, '*', None)
