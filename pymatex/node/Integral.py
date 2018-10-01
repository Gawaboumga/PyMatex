from pymatex.listener import MatexASTVisitor
from pymatex.node.IterativeFunction import IterativeFunction, IterativeType


class Integral(IterativeFunction):

    def __init__(self, variable, start_range, end_range, expression):
        super().__init__(IterativeType.SUM, variable, start_range, end_range, expression)

    def __str__(self):
        return '\\int_{{{}}}^{{{}}}{{{} d{}}}'.format(self.start_range, self.end_range, self.expression, self.variable)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_integral(self)
