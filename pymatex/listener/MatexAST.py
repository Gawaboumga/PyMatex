from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from pymatex.error import ExceptionErrorListener
from pymatex.grammar import MatexLexer, MatexParser, MatexParserListener
from pymatex.listener import MatexASTVisitor
from pymatex.node import *


class MatexAST(MatexParserListener):

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

    def accept(self, visitor: MatexASTVisitor):
        assert (self.__head is not None)
        return self.__head.accept(visitor)

    @staticmethod
    def get_tree(latex: str):
        lexer = MatexLexer(InputStream(latex))
        stream = CommonTokenStream(lexer)
        parser = MatexParser(stream)
        parser._listeners = [ExceptionErrorListener()]
        return parser.math()

    @staticmethod
    def parse(latex: str):
        tree = MatexAST.get_tree(latex)
        ast = MatexAST()
        walker = ParseTreeWalker()
        walker.walk(ast, tree)
        return ast

    def exitAbsolute(self, ctx: MatexParser.AbsoluteContext):
        self.push(Function(Func.ABS, self.pop()))

    def exitAdditionExpr(self, ctx: MatexParser.AdditionExprContext):
        if ctx.getChildCount() < 2:
            return

        rhs = self.pop()
        lhs = self.pop()
        self.push(Addition(lhs, rhs))

    def exitBinomial(self, ctx: MatexParser.BinomialContext):
        if ctx.getChildCount() < 2:
            return

        rhs = self.pop()
        lhs = self.pop()
        self.push(Function(Func.BINOMIAL, lhs, rhs))

    def exitConstant(self, ctx: MatexParser.ConstantContext):
        if ctx.INFINITY():
            self.push(Constant(ctx.INFINITY().getText()))

    def exitContinuedFactionExpr(self, ctx: MatexParser.ContinuedFactionExprContext):
        expression = self.pop()
        end_range = self.pop()
        start_range = self.pop()
        variable = self.pop()
        self.push(Fraction(variable, start_range, end_range, expression))

    def exitContinuedFactionInequalityExpr(self, ctx: MatexParser.ContinuedFactionInequalityExprContext):
        expression = self.pop()
        end_range = None
        if ctx.funcIneqParams().supexpr():
            end_range = self.pop()
        start_range = self.pop()

        self.push(InequalityFraction(start_range, end_range, expression))

    def exitContinuedFactionSetExpr(self, ctx: MatexParser.ContinuedFactionSetExprContext):
        expression = self.pop()
        end_range = None
        if ctx.funcSetParams().supexpr():
            end_range = self.pop()
        start_range = self.pop()

        self.push(InequalityFraction(start_range, end_range, expression))

    def exitDivisionExpr(self, ctx: MatexParser.DivisionExprContext):
        if ctx.getChildCount() < 2:
            return

        rhs = self.pop()
        lhs = self.pop()
        self.push(Division(lhs, rhs))

    def exitExactDivision(self, ctx: MatexParser.ExactDivisionContext):
        self.push(Function(Func.EXACTDIVISION, Variable(ctx.VARIABLE(0).getText()), Variable(ctx.VARIABLE(1).getText())))

    def exitExponentiationExpr(self, ctx: MatexParser.ExponentiationExprContext):
        rhs = self.pop()
        lhs = self.pop()

        # Fix the case where 2a^2 is interpreted as (2 * a)^2
        if isinstance(lhs, Multiplication):
            if isinstance(lhs.lhs, Constant) and isinstance(lhs.rhs, Variable):
                self.push(Multiplication(lhs.lhs, Exponentiation(lhs.rhs, rhs)))
                return

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

        if funcname is None:
            greek_letter = ctx.GREEKFUNCTIONPAREN()
            if greek_letter is None:
                greek_letter = ctx.GREEKFUNCTIONBRACE()
            if greek_letter is None:
                greek_letter = ctx.LETTERFUNCTIONBRACE()
            if greek_letter is None:
                greek_letter = ctx.LETTERFUNCTIONPAREN()

            letter = greek_letter.getText()[:-1]

            arguments = ctx.bracedMultiExpr()
            if not arguments:
                arguments = ctx.parenMultiExpr()
            if not arguments:
                arguments = ctx.multiExpr()

            expressions = []
            for _ in range((arguments.getChildCount() + 1) // 2):
                expressions.insert(0, self.pop())

            if letter == r'\zeta':
                return self.push(Function(Func.ZETA, *expressions))

            return self.push(Function(letter, *expressions))

        argument_0 = self.pop()
        if funcname.FUNC_ARCCOS():
            self.push(Function(Func.ACOS, argument_0))
        elif funcname.FUNC_ARCCOSH():
            self.push(Function(Func.ACOSH, argument_0))
        elif funcname.FUNC_ARCCOT():
            self.push(Function(Func.ACOST, argument_0))
        elif funcname.FUNC_ARCCSC():
            self.push(Function(Func.ACSC, argument_0))
        elif funcname.FUNC_ARCSEC():
            self.push(Function(Func.ASEC, argument_0))
        elif funcname.FUNC_ARCECOS():
            self.push(Function(Func.AECOS, self.pop(), argument_0))
        elif funcname.FUNC_ARCEDELTAAMPLITUDE():
            self.push(Function(Func.AEDELTAAMPLITUDE, self.pop(), argument_0))
        elif funcname.FUNC_ARCESIN():
            self.push(Function(Func.AESIN, self.pop(), argument_0))
        elif funcname.FUNC_ARCSIN():
            self.push(Function(Func.ASIN, argument_0))
        elif funcname.FUNC_ARCSINH():
            self.push(Function(Func.ASINH, argument_0))
        elif funcname.FUNC_ARCTAN():
            self.push(Function(Func.ATAN, argument_0))
        elif funcname.FUNC_ARCTANH():
            self.push(Function(Func.ATANH, argument_0))
        elif funcname.FUNC_COS():
            self.push(Function(Func.COS, argument_0))
        elif funcname.FUNC_COSH():
            self.push(Function(Func.COSH, argument_0))
        elif funcname.FUNC_COT():
            self.push(Function(Func.COT, argument_0))
        elif funcname.FUNC_CSC():
            self.push(Function(Func.CSC, argument_0))
        elif funcname.FUNC_ECOS():
            self.push(Function(Func.ECOS, self.pop(), argument_0))
        elif funcname.FUNC_EDELTAAMPLITUDE():
            self.push(Function(Func.EDELTAAMPLITUDE, self.pop(), argument_0))
        elif funcname.FUNC_ESIN():
            self.push(Function(Func.ESIN, self.pop(), argument_0))
        elif funcname.FUNC_LN():
            self.push(Function(Func.LN, argument_0))
        elif funcname.FUNC_LOG():
            self.push(Function(Func.LOG, argument_0))
        elif funcname.FUNC_SEC():
            self.push(Function(Func.SEC, argument_0))
        elif funcname.FUNC_SIN():
            self.push(Function(Func.SIN, argument_0))
        elif funcname.FUNC_SINH():
            self.push(Function(Func.SINH, argument_0))
        elif funcname.FUNC_SQRT():
            self.push(Function(Func.SQRT, argument_0))
        elif funcname.FUNC_TAN():
            self.push(Function(Func.TAN, argument_0))
        elif funcname.FUNC_ARCTAN():
            self.push(Function(Func.ATAN, argument_0))

    def exitIndexedVariable(self, ctx: MatexParser.IndexedVariableContext):
        expression = self.pop()
        self.push(IndexedVariable(ctx.VARIABLE().getText(), expression))

    def exitInequality(self, ctx: MatexParser.InequalityContext):
        rhs = self.pop()
        lhs = self.pop()
        self.push(Inequality(lhs, rhs, ctx.INEQUALITIES().getText()))

    def exitIntegralExpr(self, ctx: MatexParser.IntegralExprContext):
        expression = self.pop()
        end_range = self.pop()
        start_range = self.pop()

        variable = None
        if ctx.DERIVATIVE():
            variable = Variable(ctx.DERIVATIVE().getText()[1:])

        self.push(Integral(variable, start_range, end_range, expression))

    def exitLocalMultiplication(self, ctx: MatexParser.LocalMultiplicationContext):
        last = None
        variables = None

        if ctx.MIXNUMBER():
            mixed_number = ctx.MIXNUMBER().getText()

            import re
            for it in re.finditer(r'[-+]?\d*\.?\d+([eE][-+]?\d+)?', mixed_number):
                span = it.span(0)
                number = mixed_number[span[0]:span[1]]
                last = Constant(number)
                variables = mixed_number[span[1]:]
        elif ctx.WORD():
            variables = ctx.WORD().getText()
        else:
            variables = ctx.DERIVATIVE().getText()

        for variable in variables:
            if last is None:
                last = Variable(variable)
            else:
                last = Multiplication(last, Variable(variable))
        self.push(last)

    def exitNegateAtom(self, ctx: MatexParser.NegateAtomContext):
        value = self.pop()
        self.push(Negate(value))

    def exitNumber(self, ctx: MatexParser.NumberContext):
        self.push(Constant(ctx.NUMBER().getText()))

    def exitMath(self, ctx: MatexParser.MathContext):
        assert (len(self.__stack) == 1)
        self.__head = self.__stack[0]

    def exitMegaExpr(self, ctx: MatexParser.MegaExprContext):
        if ctx.getChildCount() < 2:
            return

        rhs = self.pop()
        lhs = self.pop()

        if ctx.PLUS():
            self.push(Addition(lhs, rhs))
        elif ctx.MUL():
            self.push(Multiplication(lhs, rhs))
        elif ctx.MINUS():
            self.push(Subtraction(lhs, rhs))
        else:
            self.push(Multiplication(lhs, rhs))

    def exitImplicitMultiplicationExpr(self, ctx: MatexParser.ImplicitMultiplicationExprContext):
        if ctx.getChildCount() < 2:
            return

        rhs = self.pop()
        lhs = self.pop()

        self.push(Multiplication(lhs, rhs))

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

    def exitProductInequalityExpr(self, ctx: MatexParser.SummationInequalityExprContext):
        expression = self.pop()
        end_range = None
        if ctx.funcIneqParams().supexpr():
            end_range = self.pop()
        start_range = self.pop()

        self.push(InequalityProduct(start_range, end_range, expression))

    def exitProductSetExpr(self, ctx: MatexParser.ProductSetExprContext):
        expression = self.pop()
        end_range = None
        if ctx.funcSetParams().supexpr():
            end_range = self.pop()
        start_range = self.pop()

        self.push(SetProduct(start_range, end_range, expression))

    def exitSetDifferenceExpr(self, ctx: MatexParser.SetDifferenceExprContext):
        rhs = self.pop()
        lhs = self.pop()

        self.push(SetDifference(lhs, rhs))

    def exitSetExpr(self, ctx: MatexParser.SetExprContext):
        rhs = self.pop()
        lhs = self.pop()

        self.push(Set(lhs, rhs))

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

    def exitSummationInequalityExpr(self, ctx: MatexParser.SummationInequalityExprContext):
        expression = self.pop()
        end_range = None
        if ctx.funcIneqParams().supexpr():
            end_range = self.pop()
        start_range = self.pop()

        self.push(InequalitySummation(start_range, end_range, expression))

    def exitSummationSetExpr(self, ctx: MatexParser.SummationSetExprContext):
        expression = self.pop()
        end_range = None
        if ctx.funcSetParams().supexpr():
            end_range = self.pop()
        start_range = self.pop()

        self.push(SetSummation(start_range, end_range, expression))

    def exitVariable(self, ctx: MatexParser.VariableContext):
        if ctx.VARIABLE():
            self.push(Variable(ctx.VARIABLE().getText()))
        else:
            self.push(Variable(ctx.GREEKLETTER().getText()))

    def pop(self):
        assert (len(self.__stack) >= 1)
        return self.__stack.pop()

    def push(self, value):
        self.__stack.append(value)
