from pymatex.listener import MatexASTVisitor
from pymatex.node.Node import Node


class Inequality(Node):

    def __init__(self, lhs, rhs, symbol):
        super().__init__()

        self.lhs = lhs
        self.rhs = rhs
        self.symbol = symbol

    def __eq__(self, other):
        assert (self.lhs is not None and self.rhs is not None)
        assert (other.lhs is not None and other.rhs is not None)
        assert (isinstance(self.lhs, type(other.lhs)))
        assert (isinstance(self.rhs, type(other.rhs)))

        return self.lhs == other.lhs and self.rhs == other.rhs

    def __str__(self):
        assert (self.lhs is not None and self.rhs is not None)
        return '({} {} {})'.format(self.lhs, self.symbol, self.rhs)
