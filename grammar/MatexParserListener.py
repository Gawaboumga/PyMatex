# Generated from .\grammar\MatexParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MatexParser import MatexParser
else:
    from MatexParser import MatexParser

# This class defines a complete listener for a parse tree produced by MatexParser.
class MatexParserListener(ParseTreeListener):

    # Enter a parse tree produced by MatexParser#math.
    def enterMath(self, ctx:MatexParser.MathContext):
        pass

    # Exit a parse tree produced by MatexParser#math.
    def exitMath(self, ctx:MatexParser.MathContext):
        pass


    # Enter a parse tree produced by MatexParser#equality.
    def enterEquality(self, ctx:MatexParser.EqualityContext):
        pass

    # Exit a parse tree produced by MatexParser#equality.
    def exitEquality(self, ctx:MatexParser.EqualityContext):
        pass


    # Enter a parse tree produced by MatexParser#expr.
    def enterExpr(self, ctx:MatexParser.ExprContext):
        pass

    # Exit a parse tree produced by MatexParser#expr.
    def exitExpr(self, ctx:MatexParser.ExprContext):
        pass


    # Enter a parse tree produced by MatexParser#summationExpr.
    def enterSummationExpr(self, ctx:MatexParser.SummationExprContext):
        pass

    # Exit a parse tree produced by MatexParser#summationExpr.
    def exitSummationExpr(self, ctx:MatexParser.SummationExprContext):
        pass


    # Enter a parse tree produced by MatexParser#productExpr.
    def enterProductExpr(self, ctx:MatexParser.ProductExprContext):
        pass

    # Exit a parse tree produced by MatexParser#productExpr.
    def exitProductExpr(self, ctx:MatexParser.ProductExprContext):
        pass


    # Enter a parse tree produced by MatexParser#funcParams.
    def enterFuncParams(self, ctx:MatexParser.FuncParamsContext):
        pass

    # Exit a parse tree produced by MatexParser#funcParams.
    def exitFuncParams(self, ctx:MatexParser.FuncParamsContext):
        pass


    # Enter a parse tree produced by MatexParser#subtractionExpr.
    def enterSubtractionExpr(self, ctx:MatexParser.SubtractionExprContext):
        pass

    # Exit a parse tree produced by MatexParser#subtractionExpr.
    def exitSubtractionExpr(self, ctx:MatexParser.SubtractionExprContext):
        pass


    # Enter a parse tree produced by MatexParser#additionExpr.
    def enterAdditionExpr(self, ctx:MatexParser.AdditionExprContext):
        pass

    # Exit a parse tree produced by MatexParser#additionExpr.
    def exitAdditionExpr(self, ctx:MatexParser.AdditionExprContext):
        pass


    # Enter a parse tree produced by MatexParser#divisionExpr.
    def enterDivisionExpr(self, ctx:MatexParser.DivisionExprContext):
        pass

    # Exit a parse tree produced by MatexParser#divisionExpr.
    def exitDivisionExpr(self, ctx:MatexParser.DivisionExprContext):
        pass


    # Enter a parse tree produced by MatexParser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:MatexParser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by MatexParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:MatexParser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by MatexParser#fracExpr.
    def enterFracExpr(self, ctx:MatexParser.FracExprContext):
        pass

    # Exit a parse tree produced by MatexParser#fracExpr.
    def exitFracExpr(self, ctx:MatexParser.FracExprContext):
        pass


    # Enter a parse tree produced by MatexParser#powExpr.
    def enterPowExpr(self, ctx:MatexParser.PowExprContext):
        pass

    # Exit a parse tree produced by MatexParser#powExpr.
    def exitPowExpr(self, ctx:MatexParser.PowExprContext):
        pass


    # Enter a parse tree produced by MatexParser#exponentiationExpr.
    def enterExponentiationExpr(self, ctx:MatexParser.ExponentiationExprContext):
        pass

    # Exit a parse tree produced by MatexParser#exponentiationExpr.
    def exitExponentiationExpr(self, ctx:MatexParser.ExponentiationExprContext):
        pass


    # Enter a parse tree produced by MatexParser#signedAtom.
    def enterSignedAtom(self, ctx:MatexParser.SignedAtomContext):
        pass

    # Exit a parse tree produced by MatexParser#signedAtom.
    def exitSignedAtom(self, ctx:MatexParser.SignedAtomContext):
        pass


    # Enter a parse tree produced by MatexParser#negateAtom.
    def enterNegateAtom(self, ctx:MatexParser.NegateAtomContext):
        pass

    # Exit a parse tree produced by MatexParser#negateAtom.
    def exitNegateAtom(self, ctx:MatexParser.NegateAtomContext):
        pass


    # Enter a parse tree produced by MatexParser#localMultiplication.
    def enterLocalMultiplication(self, ctx:MatexParser.LocalMultiplicationContext):
        pass

    # Exit a parse tree produced by MatexParser#localMultiplication.
    def exitLocalMultiplication(self, ctx:MatexParser.LocalMultiplicationContext):
        pass


    # Enter a parse tree produced by MatexParser#atom.
    def enterAtom(self, ctx:MatexParser.AtomContext):
        pass

    # Exit a parse tree produced by MatexParser#atom.
    def exitAtom(self, ctx:MatexParser.AtomContext):
        pass


    # Enter a parse tree produced by MatexParser#variable.
    def enterVariable(self, ctx:MatexParser.VariableContext):
        pass

    # Exit a parse tree produced by MatexParser#variable.
    def exitVariable(self, ctx:MatexParser.VariableContext):
        pass


    # Enter a parse tree produced by MatexParser#indexedVariable.
    def enterIndexedVariable(self, ctx:MatexParser.IndexedVariableContext):
        pass

    # Exit a parse tree produced by MatexParser#indexedVariable.
    def exitIndexedVariable(self, ctx:MatexParser.IndexedVariableContext):
        pass


    # Enter a parse tree produced by MatexParser#constant.
    def enterConstant(self, ctx:MatexParser.ConstantContext):
        pass

    # Exit a parse tree produced by MatexParser#constant.
    def exitConstant(self, ctx:MatexParser.ConstantContext):
        pass


    # Enter a parse tree produced by MatexParser#number.
    def enterNumber(self, ctx:MatexParser.NumberContext):
        pass

    # Exit a parse tree produced by MatexParser#number.
    def exitNumber(self, ctx:MatexParser.NumberContext):
        pass


    # Enter a parse tree produced by MatexParser#absolute.
    def enterAbsolute(self, ctx:MatexParser.AbsoluteContext):
        pass

    # Exit a parse tree produced by MatexParser#absolute.
    def exitAbsolute(self, ctx:MatexParser.AbsoluteContext):
        pass


    # Enter a parse tree produced by MatexParser#factorial.
    def enterFactorial(self, ctx:MatexParser.FactorialContext):
        pass

    # Exit a parse tree produced by MatexParser#factorial.
    def exitFactorial(self, ctx:MatexParser.FactorialContext):
        pass


    # Enter a parse tree produced by MatexParser#func.
    def enterFunc(self, ctx:MatexParser.FuncContext):
        pass

    # Exit a parse tree produced by MatexParser#func.
    def exitFunc(self, ctx:MatexParser.FuncContext):
        pass


    # Enter a parse tree produced by MatexParser#funcname.
    def enterFuncname(self, ctx:MatexParser.FuncnameContext):
        pass

    # Exit a parse tree produced by MatexParser#funcname.
    def exitFuncname(self, ctx:MatexParser.FuncnameContext):
        pass


    # Enter a parse tree produced by MatexParser#subexpr.
    def enterSubexpr(self, ctx:MatexParser.SubexprContext):
        pass

    # Exit a parse tree produced by MatexParser#subexpr.
    def exitSubexpr(self, ctx:MatexParser.SubexprContext):
        pass


    # Enter a parse tree produced by MatexParser#supexpr.
    def enterSupexpr(self, ctx:MatexParser.SupexprContext):
        pass

    # Exit a parse tree produced by MatexParser#supexpr.
    def exitSupexpr(self, ctx:MatexParser.SupexprContext):
        pass


    # Enter a parse tree produced by MatexParser#subeq.
    def enterSubeq(self, ctx:MatexParser.SubeqContext):
        pass

    # Exit a parse tree produced by MatexParser#subeq.
    def exitSubeq(self, ctx:MatexParser.SubeqContext):
        pass


    # Enter a parse tree produced by MatexParser#supeq.
    def enterSupeq(self, ctx:MatexParser.SupeqContext):
        pass

    # Exit a parse tree produced by MatexParser#supeq.
    def exitSupeq(self, ctx:MatexParser.SupeqContext):
        pass


    # Enter a parse tree produced by MatexParser#relop.
    def enterRelop(self, ctx:MatexParser.RelopContext):
        pass

    # Exit a parse tree produced by MatexParser#relop.
    def exitRelop(self, ctx:MatexParser.RelopContext):
        pass


