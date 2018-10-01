from pymatex.listener import MatexASTVisitor
from pymatex.node.Node import Node


class Variable(Node):

    def __init__(self, variable: str):
        super().__init__()

        self.variable = variable

    def __eq__(self, other):
        return self.variable == other.variable

    def __str__(self):
        return self.variable

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_variable(self)
