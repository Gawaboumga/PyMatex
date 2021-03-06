from pymatex.listener import MatexASTVisitor
from enum import Enum, auto


class NodeType(Enum):
    ADDITION = auto()
    BOUNDVARIABLE = auto()
    CONSTANT = auto()
    DIVISION = auto()
    EXPONENTIATION = auto()
    FRACTION = auto()
    FUNCTION = auto()
    INDEXEDVARIABLE = auto()
    INTEGRAL = auto()
    MULTIPLICATION = auto()
    NEGATE = auto()
    PRODUCT = auto()
    SET = auto()
    SET_DIFFERENCE = auto()
    SUBTRACTION = auto()
    SUMMATION = auto()
    VARIABLE = auto()


class Node:
    def accept(self, visitor: MatexASTVisitor):
        pass
