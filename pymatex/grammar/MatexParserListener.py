# Generated from .\pymatex\grammar\MatexParser.g4 by ANTLR 4.7.2
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


    # Enter a parse tree produced by MatexParser#megaExpr.
    def enterMegaExpr(self, ctx:MatexParser.MegaExprContext):
        pass

    # Exit a parse tree produced by MatexParser#megaExpr.
    def exitMegaExpr(self, ctx:MatexParser.MegaExprContext):
        pass


    # Enter a parse tree produced by MatexParser#specialExpr.
    def enterSpecialExpr(self, ctx:MatexParser.SpecialExprContext):
        pass

    # Exit a parse tree produced by MatexParser#specialExpr.
    def exitSpecialExpr(self, ctx:MatexParser.SpecialExprContext):
        pass


    # Enter a parse tree produced by MatexParser#expr.
    def enterExpr(self, ctx:MatexParser.ExprContext):
        pass

    # Exit a parse tree produced by MatexParser#expr.
    def exitExpr(self, ctx:MatexParser.ExprContext):
        pass


    # Enter a parse tree produced by MatexParser#integralExpr.
    def enterIntegralExpr(self, ctx:MatexParser.IntegralExprContext):
        pass

    # Exit a parse tree produced by MatexParser#integralExpr.
    def exitIntegralExpr(self, ctx:MatexParser.IntegralExprContext):
        pass


    # Enter a parse tree produced by MatexParser#continuedFactionExpr.
    def enterContinuedFactionExpr(self, ctx:MatexParser.ContinuedFactionExprContext):
        pass

    # Exit a parse tree produced by MatexParser#continuedFactionExpr.
    def exitContinuedFactionExpr(self, ctx:MatexParser.ContinuedFactionExprContext):
        pass


    # Enter a parse tree produced by MatexParser#continuedFactionInequalityExpr.
    def enterContinuedFactionInequalityExpr(self, ctx:MatexParser.ContinuedFactionInequalityExprContext):
        pass

    # Exit a parse tree produced by MatexParser#continuedFactionInequalityExpr.
    def exitContinuedFactionInequalityExpr(self, ctx:MatexParser.ContinuedFactionInequalityExprContext):
        pass


    # Enter a parse tree produced by MatexParser#summationExpr.
    def enterSummationExpr(self, ctx:MatexParser.SummationExprContext):
        pass

    # Exit a parse tree produced by MatexParser#summationExpr.
    def exitSummationExpr(self, ctx:MatexParser.SummationExprContext):
        pass


    # Enter a parse tree produced by MatexParser#summationInequalityExpr.
    def enterSummationInequalityExpr(self, ctx:MatexParser.SummationInequalityExprContext):
        pass

    # Exit a parse tree produced by MatexParser#summationInequalityExpr.
    def exitSummationInequalityExpr(self, ctx:MatexParser.SummationInequalityExprContext):
        pass


    # Enter a parse tree produced by MatexParser#productExpr.
    def enterProductExpr(self, ctx:MatexParser.ProductExprContext):
        pass

    # Exit a parse tree produced by MatexParser#productExpr.
    def exitProductExpr(self, ctx:MatexParser.ProductExprContext):
        pass


    # Enter a parse tree produced by MatexParser#productInequalityExpr.
    def enterProductInequalityExpr(self, ctx:MatexParser.ProductInequalityExprContext):
        pass

    # Exit a parse tree produced by MatexParser#productInequalityExpr.
    def exitProductInequalityExpr(self, ctx:MatexParser.ProductInequalityExprContext):
        pass


    # Enter a parse tree produced by MatexParser#tailExpr.
    def enterTailExpr(self, ctx:MatexParser.TailExprContext):
        pass

    # Exit a parse tree produced by MatexParser#tailExpr.
    def exitTailExpr(self, ctx:MatexParser.TailExprContext):
        pass


    # Enter a parse tree produced by MatexParser#funcParams.
    def enterFuncParams(self, ctx:MatexParser.FuncParamsContext):
        pass

    # Exit a parse tree produced by MatexParser#funcParams.
    def exitFuncParams(self, ctx:MatexParser.FuncParamsContext):
        pass


    # Enter a parse tree produced by MatexParser#funcIneqParams.
    def enterFuncIneqParams(self, ctx:MatexParser.FuncIneqParamsContext):
        pass

    # Exit a parse tree produced by MatexParser#funcIneqParams.
    def exitFuncIneqParams(self, ctx:MatexParser.FuncIneqParamsContext):
        pass


    # Enter a parse tree produced by MatexParser#implicitMultiplicationExpr.
    def enterImplicitMultiplicationExpr(self, ctx:MatexParser.ImplicitMultiplicationExprContext):
        pass

    # Exit a parse tree produced by MatexParser#implicitMultiplicationExpr.
    def exitImplicitMultiplicationExpr(self, ctx:MatexParser.ImplicitMultiplicationExprContext):
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


    # Enter a parse tree produced by MatexParser#exactDivision.
    def enterExactDivision(self, ctx:MatexParser.ExactDivisionContext):
        pass

    # Exit a parse tree produced by MatexParser#exactDivision.
    def exitExactDivision(self, ctx:MatexParser.ExactDivisionContext):
        pass


    # Enter a parse tree produced by MatexParser#factorial.
    def enterFactorial(self, ctx:MatexParser.FactorialContext):
        pass

    # Exit a parse tree produced by MatexParser#factorial.
    def exitFactorial(self, ctx:MatexParser.FactorialContext):
        pass


    # Enter a parse tree produced by MatexParser#binomial.
    def enterBinomial(self, ctx:MatexParser.BinomialContext):
        pass

    # Exit a parse tree produced by MatexParser#binomial.
    def exitBinomial(self, ctx:MatexParser.BinomialContext):
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


    # Enter a parse tree produced by MatexParser#bracedMultiExpr.
    def enterBracedMultiExpr(self, ctx:MatexParser.BracedMultiExprContext):
        pass

    # Exit a parse tree produced by MatexParser#bracedMultiExpr.
    def exitBracedMultiExpr(self, ctx:MatexParser.BracedMultiExprContext):
        pass


    # Enter a parse tree produced by MatexParser#parenMultiExpr.
    def enterParenMultiExpr(self, ctx:MatexParser.ParenMultiExprContext):
        pass

    # Exit a parse tree produced by MatexParser#parenMultiExpr.
    def exitParenMultiExpr(self, ctx:MatexParser.ParenMultiExprContext):
        pass


    # Enter a parse tree produced by MatexParser#multiExpr.
    def enterMultiExpr(self, ctx:MatexParser.MultiExprContext):
        pass

    # Exit a parse tree produced by MatexParser#multiExpr.
    def exitMultiExpr(self, ctx:MatexParser.MultiExprContext):
        pass


    # Enter a parse tree produced by MatexParser#bracedExpr.
    def enterBracedExpr(self, ctx:MatexParser.BracedExprContext):
        pass

    # Exit a parse tree produced by MatexParser#bracedExpr.
    def exitBracedExpr(self, ctx:MatexParser.BracedExprContext):
        pass


    # Enter a parse tree produced by MatexParser#brackExpr.
    def enterBrackExpr(self, ctx:MatexParser.BrackExprContext):
        pass

    # Exit a parse tree produced by MatexParser#brackExpr.
    def exitBrackExpr(self, ctx:MatexParser.BrackExprContext):
        pass


    # Enter a parse tree produced by MatexParser#parenExpr.
    def enterParenExpr(self, ctx:MatexParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MatexParser#parenExpr.
    def exitParenExpr(self, ctx:MatexParser.ParenExprContext):
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


    # Enter a parse tree produced by MatexParser#subIneq.
    def enterSubIneq(self, ctx:MatexParser.SubIneqContext):
        pass

    # Exit a parse tree produced by MatexParser#subIneq.
    def exitSubIneq(self, ctx:MatexParser.SubIneqContext):
        pass


    # Enter a parse tree produced by MatexParser#equality.
    def enterEquality(self, ctx:MatexParser.EqualityContext):
        pass

    # Exit a parse tree produced by MatexParser#equality.
    def exitEquality(self, ctx:MatexParser.EqualityContext):
        pass


    # Enter a parse tree produced by MatexParser#inequality.
    def enterInequality(self, ctx:MatexParser.InequalityContext):
        pass

    # Exit a parse tree produced by MatexParser#inequality.
    def exitInequality(self, ctx:MatexParser.InequalityContext):
        pass


