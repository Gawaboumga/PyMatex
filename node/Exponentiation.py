from .BinaryOperator import BinaryOperator


class Exponentiation(BinaryOperator):

    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs, '^', None)

    def __str__(self):
        return '{}^{{{}}}'.format(self.lhs, self.rhs)
