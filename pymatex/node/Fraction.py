from pymatex.listener import MatexASTVisitor
from pymatex.node.IterativeFunction import IterativeFunction, IterativeType


class Fraction(IterativeFunction):

    def __init__(self, variable, start_range, end_range, expression):
        super().__init__(IterativeType.FRACTION, variable, start_range, end_range, expression)

    def __str__(self):
        return 'K_{{{}={}}}^{{{}}}{{{}}}'.format(self.variable, self.start_range, self.end_range,
                                                     self.expression)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_fraction(self)


class InequalityFraction(Fraction):

    def __init__(self, start_range, end_range, expression):
        super().__init__(None, start_range, end_range, expression)

    def __str__(self):
        if self.end_range:
            return 'K_{{{}}}^{{{}}}{{{}}}'.format(self.start_range, self.end_range, self.expression)
        else:
            return 'K_{{{}}}{{{}}}'.format(self.start_range, self.expression)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_fraction(self)


class SetFraction(Fraction):

    def __init__(self, start_range, end_range, expression):
        super().__init__(None, start_range, end_range, expression)

    def __str__(self):
        if self.end_range:
            return 'K_{{{}}}^{{{}}}{{{}}}'.format(self.start_range, self.end_range, self.expression)
        else:
            return 'K_{{{}}}{{{}}}'.format(self.start_range, self.expression)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_fraction(self)
