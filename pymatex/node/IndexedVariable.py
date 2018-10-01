from pymatex.listener import MatexASTVisitor
from pymatex.node.Variable import Variable


class IndexedVariable(Variable):

    def __init__(self, variable: str, index):
        super().__init__(variable)

        self.index = index

    def __eq__(self, other):
        return super().__eq__(other) and self.index == other.index

    def __str__(self):
        return '{}_{{{}}}'.format(self.variable, self.index)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_indexed_variable(self)
