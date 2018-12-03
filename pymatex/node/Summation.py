from pymatex.listener import MatexASTVisitor
from pymatex.node.IterativeFunction import IterativeFunction, IterativeType


class Summation(IterativeFunction):

    def __init__(self, variable, start_range, end_range, expression):
        super().__init__(IterativeType.SUM, variable, start_range, end_range, expression)

    def __str__(self):
        return '\\sum_{{{}={}}}^{{{}}}{{{}}}'.format(self.variable, self.start_range, self.end_range,
                                                     self.expression)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_summation(self)


class InequalitySummation(Summation):

    def __init__(self, start_range, end_range, expression):
        super().__init__(None, start_range, end_range, expression)

    def __str__(self):
        if self.end_range:
            return r'\sum_{{{}}}^{{{}}}{{{}}}'.format(self.start_range, self.end_range, self.expression)
        else:
            return r'\sum_{{{}}}{{{}}}'.format(self.start_range, self.expression)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_summation(self)
