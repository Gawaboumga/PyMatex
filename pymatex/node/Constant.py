import math
from pymatex.listener import MatexASTVisitor
from pymatex.node.Node import Node


class Constant(Node):

    value: str

    def __init__(self, constant: str):
        super().__init__()

        self.value = None

        if constant == '\\infty':
            self.value = constant
        else:
            _ = float(constant)
            self.value = constant

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        if self.value[0] == '-':
            return '({})'.format(self.value)
        else:
            return self.value

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_constant(self)
