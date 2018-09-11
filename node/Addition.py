from .BinaryOperator import BinaryOperator


class Addition(BinaryOperator):

    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs, '+', None)
