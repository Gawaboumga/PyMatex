from pymatex.listener import MatexASTVisitor
from pymatex.node.Node import Node


class Set(Node):

    def __init__(self, lhs, rhs):
        super().__init__()

        self.lhs = lhs
        self.rhs = rhs

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs

    def __str__(self):
        return '{} \in {}'.format(self.lhs, self.rhs)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_set(self)


class SetDifference(Node):

    def __init__(self, lhs, rhs):
        super().__init__()

        self.lhs = lhs
        self.rhs = rhs

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs

    def __str__(self):
        return '{}\\{{{}}}'.format(self.lhs, self.rhs)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_set_difference(self)
