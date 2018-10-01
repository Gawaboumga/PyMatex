from pymatex.listener import MatexASTVisitor
from pymatex.node.Node import Node


class Negate(Node):

    def __init__(self, node):
        super().__init__()

        self.node = node

    def __eq__(self, other):
        return self.node == other.node

    def __str__(self):
        return '-({})'.format(self.node)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_negate(self)
