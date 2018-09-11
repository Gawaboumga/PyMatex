from grammar import MatexParserListener
from grammar.MatexParser import MatexParser
from node import *


class MatexAST(MatexParserListener.MatexParserListener):

    def __init__(self):
        super().__init__()
        self.__stack = []
        self.__head = None

    def __eq__(self, other):
        assert (self.__head is not None)
        return self.__head == other

    def __str__(self):
        assert (self.__head is not None)
        return str(self.__head)

    def exitAbsolute(self, ctx: MatexParser.AbsoluteContext):
        self.push(Function(Func.ABS, self.pop()))

    def exitAdditionExpr(self, ctx: MatexParser.AdditionExprContext):
        if ctx.getChildCount() < 2:
            return

        rhs = self.pop()
        lhs = self.pop()
        self.push(Addition(lhs, rhs))

    def exitConstant(self, ctx: MatexParser.ConstantContext):
        if ctx.PI():
            self.push(Constant(ctx.PI().getText()))
        elif ctx.INFINITY():
            self.push(Constant(ctx.INFINITY().getText()))

    def exitDivisionExpr(self, ctx: MatexParser.DivisionExprContext):
        if ctx.getChildCount() < 2:
            return

        rhs = self.pop()
        lhs = self.pop()
        self.push(Division(lhs, rhs))

    def exitExponentiationExpr(self, ctx:MatexParser.ExponentiationExprContext):
        rhs = self.pop()
        lhs = self.pop()
        self.push(Exponentiation(lhs, rhs))

    def exitFactorial(self, ctx: MatexParser.FactorialContext):
        expression = self.pop()
        self.push(Function(Func.FACTORIAL, expression))

    def exitFracExpr(self, ctx: MatexParser.FracExprContext):
        rhs = self.pop()
        lhs = self.pop()
        self.push(Division(lhs, rhs))

    def exitFunc(self, ctx: MatexParser.FuncContext):
        funcname: MatexParser.FuncnameContext = ctx.funcname()

        expression = self.pop()
        if funcname.FUNC_ARCCOS():
            self.push(Function(Func.ACOS, expression))
        elif funcname.FUNC_ARCCOSH():
            self.push(Function(Func.ACOSH, expression))
        elif funcname.FUNC_ARCCOT():
            self.push(Function(Func.ACOST, expression))
        elif funcname.FUNC_ARCCSC():
            self.push(Function(Func.ACSC, expression))
        elif funcname.FUNC_ARCSEC():
            self.push(Function(Func.ASEC, expression))
        elif funcname.FUNC_ARCSIN():
            self.push(Function(Func.ASIN, expression))
        elif funcname.FUNC_ARCSINH():
            self.push(Function(Func.ASINH, expression))
        elif funcname.FUNC_ARCTAN():
            self.push(Function(Func.ATAN, expression))
        elif funcname.FUNC_ARCTANH():
            self.push(Function(Func.ATANH, expression))
        elif funcname.FUNC_COS():
            self.push(Function(Func.COS, expression))
        elif funcname.FUNC_COSH():
            self.push(Function(Func.COSH, expression))
        elif funcname.FUNC_COT():
            self.push(Function(Func.COT, expression))
        elif funcname.FUNC_CSC():
            self.push(Function(Func.CSC, expression))
        elif funcname.FUNC_LN():
            self.push(Function(Func.LN, expression))
        elif funcname.FUNC_LOG():
            self.push(Function(Func.LOG, expression))
        elif funcname.FUNC_SEC():
            self.push(Function(Func.SEC, expression))
        elif funcname.FUNC_SIN():
            self.push(Function(Func.SIN, expression))
        elif funcname.FUNC_SINH():
            self.push(Function(Func.SINH, expression))
        elif funcname.FUNC_SQRT():
            self.push(Function(Func.SQRT, expression))
        elif funcname.FUNC_TAN():
            self.push(Function(Func.TAN, expression))
        elif funcname.FUNC_ARCTAN():
            self.push(Function(Func.ATAN, expression))

    def exitLocalMultiplication(self, ctx: MatexParser.LocalMultiplicationContext):
        mixed_number = ctx.MIXNUMBER().getText()
        import re
        for it in re.finditer(r'[-+]?\d*\.?\d+([eE][-+]?\d+)?', mixed_number):
            span = it.span(0)
            number = mixed_number[span[0]:span[1]]
            variable = mixed_number[span[1]:]
            self.push(Multiplication(Constant(number), Variable(variable)))

    def exitNegateAtom(self, ctx: MatexParser.NegateAtomContext):
        value = self.pop()
        self.push(Negate(value))

    def exitNumber(self, ctx: MatexParser.NumberContext):
        number = ctx.NUMBER().getText()
        if number[0] == '+':
            number = number[1:]
        self.push(Constant(number))

    def exitMath(self, ctx: MatexParser.MathContext):
        assert (len(self.__stack) == 1)
        self.__head = self.__stack[0]

    def exitMultiplicationExpr(self, ctx: MatexParser.MultiplicationExprContext):
        if ctx.getChildCount() < 2:
            return

        rhs = self.pop()
        lhs = self.pop()
        self.push(Multiplication(lhs, rhs))

    def exitProductExpr(self, ctx: MatexParser.ProductExprContext):
        expression = self.pop()
        end_range = self.pop()
        start_range = self.pop()
        variable = self.pop()
        self.push(Product(variable, start_range, end_range, expression))

    def exitSubtractionExpr(self, ctx: MatexParser.SubtractionExprContext):
        if ctx.getChildCount() < 2:
            return

        rhs = self.pop()
        lhs = self.pop()
        self.push(Subtraction(lhs, rhs))

    def exitSummationExpr(self, ctx: MatexParser.SummationExprContext):
        expression = self.pop()
        end_range = self.pop()
        start_range = self.pop()
        variable = self.pop()

        self.push(Summation(variable, start_range, end_range, expression))

    def exitVariable(self, ctx: MatexParser.VariableContext):
        self.push(Variable(ctx.VARIABLE().getText()))

    def pop(self):
        assert (len(self.__stack) >= 1)
        return self.__stack.pop()

    def push(self, value):
        self.__stack.append(value)