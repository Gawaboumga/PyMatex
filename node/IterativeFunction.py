from enum import Enum, auto
from node.Node import Node


class IterativeType(Enum):
    INTEGRAL = auto()
    PRODUCT = auto()
    SUM = auto()


class IterativeFunction(Node):

    def __init__(self, iterative_type: IterativeType, variable, start_range, end_range, expression):
        super().__init__()

        self.iterative_type = iterative_type
        self.variable = variable
        self.start_range = start_range
        self.end_range = end_range
        self.expression = expression

    def __eq__(self, other):
        return self.iterative_type == other.iterative_type and \
               self.variable == other.variable and self.start_range == other.start_range and \
               self.end_range == other.end_range and self.expression == other.expression
