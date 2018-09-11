from enum import Enum, auto


class Func(Enum):
    ABS = auto()
    ACOS = auto()
    ACOSH = auto()
    ACOT = auto()
    ACSC = auto()
    ASEC = auto()
    ASIN = auto()
    ASINH = auto()
    ATAN = auto()
    ATANH = auto()
    COS = auto()
    COSH = auto()
    COT = auto()
    CSC = auto()
    FACTORIAL = auto()
    LN = auto()
    LOG = auto()
    SEC = auto()
    SIN = auto()
    SINH = auto()
    SQRT = auto()
    TAN = auto()
    TANH = auto()


class Function:
    def __init__(self, func: Func, expression):
        super().__init__()

        self.func = func
        self.expression = expression

    def __eq__(self, other):
        return self.func == other.func and self.expression == other.expression

    def __str__(self):
        if self.func == Func.ABS:
            return '|{}|'.format(self.expression)
        elif self.func == Func.ACSC:
            return '\\arccsc{{{}}}'.format(self.expression)
        elif self.func == Func.ACOS:
            return '\\arccos{{{}}}'.format(self.expression)
        elif self.func == Func.ACOSH:
            return '\\arccosh{{{}}}'.format(self.expression)
        elif self.func == Func.ACOT:
            return '\\arccot{{{}}}'.format(self.expression)
        elif self.func == Func.ASEC:
            return '\\arcsec{{{}}}'.format(self.expression)
        elif self.func == Func.ASIN:
            return '\\arcsin{{{}}}'.format(self.expression)
        elif self.func == Func.ASINH:
            return '\\arcsinh{{{}}}'.format(self.expression)
        elif self.func == Func.ATAN:
            return '\\arctan{{{}}}'.format(self.expression)
        elif self.func == Func.ATANH:
            return '\\arctanh{{{}}}'.format(self.expression)
        elif self.func == Func.COS:
            return '\\cos{{{}}}'.format(self.expression)
        elif self.func == Func.COSH:
            return '\\cosh{{{}}}'.format(self.expression)
        elif self.func == Func.COT:
            return '\\cot{{{}}}'.format(self.expression)
        elif self.func == Func.CSC:
            return '\\csc{{{}}}'.format(self.expression)
        elif self.func == Func.FACTORIAL:
            return '({})!'.format(self.expression)
        elif self.func == Func.LN:
            return '\\ln{{{}}}'.format(self.expression)
        elif self.func == Func.LOG:
            return '\\log{{{}}}'.format(self.expression)
        elif self.func == Func.SEC:
            return '\\sec{{{}}}'.format(self.expression)
        elif self.func == Func.SIN:
            return '\\sin{{{}}}'.format(self.expression)
        elif self.func == Func.SINH:
            return '\\sinh{{{}}}'.format(self.expression)
        elif self.func == Func.SQRT:
            return '\\sqrt{{{}}}'.format(self.expression)
        elif self.func == Func.TAN:
            return '\\tan{{{}}}'.format(self.expression)
        elif self.func == Func.TANH:
            return '\\tanh{{{}}}'.format(self.expression)
        else:
            return 'UNDEFINED FUNCTION'


