from enum import Enum, auto
from pymatex.listener import MatexASTVisitor
from pymatex.node.Node import Node


class Func(Enum):
    ABS = auto()
    ACOS = auto()
    ACOSH = auto()
    ACOT = auto()
    ACSC = auto()
    AECOS = auto()
    AEDELTAAMPLITUDE = auto()
    AESIN = auto()
    ASEC = auto()
    ASIN = auto()
    ASINH = auto()
    ATAN = auto()
    ATANH = auto()
    BINOMIAL = auto()
    COS = auto()
    COSH = auto()
    COT = auto()
    CSC = auto()
    ECOS = auto()
    EDELTAAMPLITUDE = auto()
    ESIN = auto()
    EXACTDIVISION = auto()
    FACTORIAL = auto()
    LN = auto()
    LOG = auto()
    SEC = auto()
    SIN = auto()
    SINH = auto()
    SQRT = auto()
    TAN = auto()
    TANH = auto()
    ZETA = auto()


class Function(Node):
    def __init__(self, func: Func, *arguments):
        super().__init__()

        self.func = func
        self.arguments = arguments
        
    def argument(self, i):
        assert i < self.number_of_arguments()
        return self.arguments[i]
        
    def number_of_arguments(self):
        return len(self.arguments)

    def __eq__(self, other):
        return self.func == other.func and self.arguments == other.arguments

    def __str__(self):
        if self.func == Func.ABS:
            return '|{}|'.format(self.argument(0))
        elif self.func == Func.ACSC:
            return '\\arccsc{{{}}}'.format(self.argument(0))
        elif self.func == Func.ACOS:
            return '\\arccos{{{}}}'.format(self.argument(0))
        elif self.func == Func.ACOSH:
            return '\\arccosh{{{}}}'.format(self.argument(0))
        elif self.func == Func.ACOT:
            return '\\arccot{{{}}}'.format(self.argument(0))
        elif self.func == Func.AECOS:
            return '\\arccn{{{}, {}}}'.format(self.argument(0), self.argument(1))
        elif self.func == Func.AEDELTAAMPLITUDE:
            return '\\arcdn{{{}}}'.format(self.argument(0), self.argument(1))
        elif self.func == Func.AESIN:
            return '\\arcsn{{{}}}'.format(self.argument(0), self.argument(1))
        elif self.func == Func.ASEC:
            return '\\arcsec{{{}}}'.format(self.argument(0))
        elif self.func == Func.ASIN:
            return '\\arcsin{{{}}}'.format(self.argument(0))
        elif self.func == Func.ASINH:
            return '\\arcsinh{{{}}}'.format(self.argument(0))
        elif self.func == Func.ATAN:
            return '\\arctan{{{}}}'.format(self.argument(0))
        elif self.func == Func.ATANH:
            return '\\arctanh{{{}}}'.format(self.argument(0))
        elif self.func == Func.BINOMIAL:
            return '\\binom{{{}}}{{{}}}'.format(self.argument(0), self.argument(1))
        elif self.func == Func.COS:
            return '\\cos{{{}}}'.format(self.argument(0))
        elif self.func == Func.COSH:
            return '\\cosh{{{}}}'.format(self.argument(0))
        elif self.func == Func.COT:
            return '\\cot{{{}}}'.format(self.argument(0))
        elif self.func == Func.CSC:
            return '\\csc{{{}}}'.format(self.argument(0))
        elif self.func == Func.ECOS:
            return '\\cn{{{}, {}}}'.format(self.argument(0), self.argument(1))
        elif self.func == Func.EDELTAAMPLITUDE:
            return '\\dn{{{}}}'.format(self.argument(0), self.argument(1))
        elif self.func == Func.ESIN:
            return '\\sn{{{}}}'.format(self.argument(0), self.argument(1))
        elif self.func == Func.EXACTDIVISION:
            return '{}|{}'.format(self.argument(0), self.argument(1))
        elif self.func == Func.FACTORIAL:
            return '({})!'.format(self.argument(0))
        elif self.func == Func.LN:
            return '\\ln{{{}}}'.format(self.argument(0))
        elif self.func == Func.LOG:
            return '\\log{{{}}}'.format(self.argument(0))
        elif self.func == Func.SEC:
            return '\\sec{{{}}}'.format(self.argument(0))
        elif self.func == Func.SIN:
            return '\\sin{{{}}}'.format(self.argument(0))
        elif self.func == Func.SINH:
            return '\\sinh{{{}}}'.format(self.argument(0))
        elif self.func == Func.SQRT:
            return '\\sqrt{{{}}}'.format(self.argument(0))
        elif self.func == Func.TAN:
            return '\\tan{{{}}}'.format(self.argument(0))
        elif self.func == Func.TANH:
            return '\\tanh{{{}}}'.format(self.argument(0))
        elif self.func == Func.ZETA:
            return '\\zeta{{{}}}'.format(self.argument(0))
        else:
            return 'UNDEFINED FUNCTION'

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_function(self)

