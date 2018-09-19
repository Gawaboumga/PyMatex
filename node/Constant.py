import math
from listener import MatexASTVisitor
from node.Node import Node


class Constant(Node):

    def __init__(self, constant: str):
        super().__init__()

        self.value = None

        if constant == '\\infty':
            self.value = math.inf
        else:
            _ = float(constant)
            self.value = constant

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        if self.value == math.inf:
            return '\\infty'

        if self.value[0] == '-':
            return '({})'.format(self.value)
        else:
            return self.value

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_constant(self)
