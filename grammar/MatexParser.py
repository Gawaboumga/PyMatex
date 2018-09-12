# Generated from .\grammar\MatexParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u011c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\5\4L\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4`\n\4\f\4\16\4c\13")
        buf.write("\4\3\5\3\5\5\5g\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\bv\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\7\n\u0081\n\n\f\n\16\n\u0084\13\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\7\13\u008c\n\13\f\13\16\13\u008f")
        buf.write("\13\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0097\n\f\f\f\16\f")
        buf.write("\u009a\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\7\r\u00a8\n\r\f\r\16\r\u00ab\13\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u00b8\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u00c5\n\20\3\21\3\21\3\21\3\21\5\21\u00cb\n")
        buf.write("\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\5\24\u00dc\n\24\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u00f6\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u0102\n\33\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\2\7\6\22\24\26\30\"\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@\2\7\4\2\6\6,,\4\2\5\5*+\4\2\63\63<<\3\2\25)\3")
        buf.write("\2\66:\2\u011b\2B\3\2\2\2\4D\3\2\2\2\6K\3\2\2\2\bf\3\2")
        buf.write("\2\2\nh\3\2\2\2\fl\3\2\2\2\16u\3\2\2\2\20w\3\2\2\2\22")
        buf.write("z\3\2\2\2\24\u0085\3\2\2\2\26\u0090\3\2\2\2\30\u009b\3")
        buf.write("\2\2\2\32\u00ac\3\2\2\2\34\u00b7\3\2\2\2\36\u00c4\3\2")
        buf.write("\2\2 \u00ca\3\2\2\2\"\u00cc\3\2\2\2$\u00cf\3\2\2\2&\u00db")
        buf.write("\3\2\2\2(\u00dd\3\2\2\2*\u00df\3\2\2\2,\u00e2\3\2\2\2")
        buf.write(".\u00e4\3\2\2\2\60\u00e6\3\2\2\2\62\u00f5\3\2\2\2\64\u0101")
        buf.write("\3\2\2\2\66\u0103\3\2\2\28\u0105\3\2\2\2:\u010a\3\2\2")
        buf.write("\2<\u010f\3\2\2\2>\u0114\3\2\2\2@\u0119\3\2\2\2BC\5\b")
        buf.write("\5\2C\3\3\2\2\2DE\5\b\5\2EF\7\66\2\2FG\5\b\5\2G\5\3\2")
        buf.write("\2\2HI\b\4\1\2IL\5\n\6\2JL\5\f\7\2KH\3\2\2\2KJ\3\2\2\2")
        buf.write("La\3\2\2\2MN\f\b\2\2NO\7\3\2\2O`\5\n\6\2PQ\f\7\2\2QR\7")
        buf.write("\3\2\2R`\5\f\7\2ST\f\6\2\2TU\7\4\2\2U`\5\n\6\2VW\f\5\2")
        buf.write("\2WX\7\4\2\2X`\5\f\7\2YZ\f\4\2\2Z[\7\5\2\2[`\5\n\6\2\\")
        buf.write("]\f\3\2\2]^\7\5\2\2^`\5\f\7\2_M\3\2\2\2_P\3\2\2\2_S\3")
        buf.write("\2\2\2_V\3\2\2\2_Y\3\2\2\2_\\\3\2\2\2`c\3\2\2\2a_\3\2")
        buf.write("\2\2ab\3\2\2\2b\7\3\2\2\2ca\3\2\2\2dg\5\22\n\2eg\5\6\4")
        buf.write("\2fd\3\2\2\2fe\3\2\2\2g\t\3\2\2\2hi\7\23\2\2ij\5\20\t")
        buf.write("\2jk\5\16\b\2k\13\3\2\2\2lm\7\24\2\2mn\5\20\t\2no\5\16")
        buf.write("\b\2o\r\3\2\2\2pv\5\b\5\2qr\7\t\2\2rs\5\b\5\2st\7\n\2")
        buf.write("\2tv\3\2\2\2up\3\2\2\2uq\3\2\2\2v\17\3\2\2\2wx\5<\37\2")
        buf.write("xy\5:\36\2y\21\3\2\2\2z{\b\n\1\2{|\5\24\13\2|\u0082\3")
        buf.write("\2\2\2}~\f\3\2\2~\177\7\4\2\2\177\u0081\5\24\13\2\u0080")
        buf.write("}\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083\23\3\2\2\2\u0084\u0082\3\2\2\2\u0085")
        buf.write("\u0086\b\13\1\2\u0086\u0087\5\26\f\2\u0087\u008d\3\2\2")
        buf.write("\2\u0088\u0089\f\3\2\2\u0089\u008a\7\3\2\2\u008a\u008c")
        buf.write("\5\26\f\2\u008b\u0088\3\2\2\2\u008c\u008f\3\2\2\2\u008d")
        buf.write("\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\25\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u0090\u0091\b\f\1\2\u0091\u0092\5\30\r")
        buf.write("\2\u0092\u0098\3\2\2\2\u0093\u0094\f\3\2\2\u0094\u0095")
        buf.write("\t\2\2\2\u0095\u0097\5\30\r\2\u0096\u0093\3\2\2\2\u0097")
        buf.write("\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\27\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\b\r")
        buf.write("\1\2\u009c\u009d\5\34\17\2\u009d\u00a9\3\2\2\2\u009e\u009f")
        buf.write("\f\6\2\2\u009f\u00a0\t\3\2\2\u00a0\u00a8\5\34\17\2\u00a1")
        buf.write("\u00a2\f\5\2\2\u00a2\u00a8\5\32\16\2\u00a3\u00a4\f\4\2")
        buf.write("\2\u00a4\u00a8\5\36\20\2\u00a5\u00a6\f\3\2\2\u00a6\u00a8")
        buf.write("\5&\24\2\u00a7\u009e\3\2\2\2\u00a7\u00a1\3\2\2\2\u00a7")
        buf.write("\u00a3\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00ab\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\31\3\2")
        buf.write("\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\7-\2\2\u00ad\u00ae")
        buf.write("\7\t\2\2\u00ae\u00af\5\b\5\2\u00af\u00b0\7\n\2\2\u00b0")
        buf.write("\u00b1\7\t\2\2\u00b1\u00b2\5\b\5\2\u00b2\u00b3\7\n\2\2")
        buf.write("\u00b3\33\3\2\2\2\u00b4\u00b8\5 \21\2\u00b5\u00b8\5\32")
        buf.write("\16\2\u00b6\u00b8\5\36\20\2\u00b7\u00b4\3\2\2\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\35\3\2\2\2\u00b9")
        buf.write("\u00ba\5 \21\2\u00ba\u00bb\7/\2\2\u00bb\u00bc\5.\30\2")
        buf.write("\u00bc\u00c5\3\2\2\2\u00bd\u00be\5 \21\2\u00be\u00bf\7")
        buf.write("/\2\2\u00bf\u00c0\5(\25\2\u00c0\u00c5\3\2\2\2\u00c1\u00c2")
        buf.write("\5 \21\2\u00c2\u00c3\5:\36\2\u00c3\u00c5\3\2\2\2\u00c4")
        buf.write("\u00b9\3\2\2\2\u00c4\u00bd\3\2\2\2\u00c4\u00c1\3\2\2\2")
        buf.write("\u00c5\37\3\2\2\2\u00c6\u00cb\5\"\22\2\u00c7\u00cb\5$")
        buf.write("\23\2\u00c8\u00cb\5\64\33\2\u00c9\u00cb\5&\24\2\u00ca")
        buf.write("\u00c6\3\2\2\2\u00ca\u00c7\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00ca\u00c9\3\2\2\2\u00cb!\3\2\2\2\u00cc\u00cd\7\4\2")
        buf.write("\2\u00cd\u00ce\5 \21\2\u00ce#\3\2\2\2\u00cf\u00d0\7\64")
        buf.write("\2\2\u00d0%\3\2\2\2\u00d1\u00dc\5(\25\2\u00d2\u00dc\5")
        buf.write("*\26\2\u00d3\u00dc\5,\27\2\u00d4\u00dc\5.\30\2\u00d5\u00dc")
        buf.write("\5\60\31\2\u00d6\u00dc\5\62\32\2\u00d7\u00d8\7\7\2\2\u00d8")
        buf.write("\u00d9\5\b\5\2\u00d9\u00da\7\b\2\2\u00da\u00dc\3\2\2\2")
        buf.write("\u00db\u00d1\3\2\2\2\u00db\u00d2\3\2\2\2\u00db\u00d3\3")
        buf.write("\2\2\2\u00db\u00d4\3\2\2\2\u00db\u00d5\3\2\2\2\u00db\u00d6")
        buf.write("\3\2\2\2\u00db\u00d7\3\2\2\2\u00dc\'\3\2\2\2\u00dd\u00de")
        buf.write("\t\4\2\2\u00de)\3\2\2\2\u00df\u00e0\7\63\2\2\u00e0\u00e1")
        buf.write("\58\35\2\u00e1+\3\2\2\2\u00e2\u00e3\7\65\2\2\u00e3-\3")
        buf.write("\2\2\2\u00e4\u00e5\7\62\2\2\u00e5/\3\2\2\2\u00e6\u00e7")
        buf.write("\7\17\2\2\u00e7\u00e8\5\b\5\2\u00e8\u00e9\7\17\2\2\u00e9")
        buf.write("\61\3\2\2\2\u00ea\u00eb\7\7\2\2\u00eb\u00ec\5\b\5\2\u00ec")
        buf.write("\u00ed\7\b\2\2\u00ed\u00ee\7;\2\2\u00ee\u00f6\3\2\2\2")
        buf.write("\u00ef\u00f0\5.\30\2\u00f0\u00f1\7;\2\2\u00f1\u00f6\3")
        buf.write("\2\2\2\u00f2\u00f3\5(\25\2\u00f3\u00f4\7;\2\2\u00f4\u00f6")
        buf.write("\3\2\2\2\u00f5\u00ea\3\2\2\2\u00f5\u00ef\3\2\2\2\u00f5")
        buf.write("\u00f2\3\2\2\2\u00f6\63\3\2\2\2\u00f7\u00f8\5\66\34\2")
        buf.write("\u00f8\u00f9\7\t\2\2\u00f9\u00fa\5\b\5\2\u00fa\u00fb\7")
        buf.write("\n\2\2\u00fb\u0102\3\2\2\2\u00fc\u00fd\5\66\34\2\u00fd")
        buf.write("\u00fe\7\7\2\2\u00fe\u00ff\5\b\5\2\u00ff\u0100\7\b\2\2")
        buf.write("\u0100\u0102\3\2\2\2\u0101\u00f7\3\2\2\2\u0101\u00fc\3")
        buf.write("\2\2\2\u0102\65\3\2\2\2\u0103\u0104\t\5\2\2\u0104\67\3")
        buf.write("\2\2\2\u0105\u0106\7.\2\2\u0106\u0107\7\t\2\2\u0107\u0108")
        buf.write("\5\b\5\2\u0108\u0109\7\n\2\2\u01099\3\2\2\2\u010a\u010b")
        buf.write("\7/\2\2\u010b\u010c\7\t\2\2\u010c\u010d\5\b\5\2\u010d")
        buf.write("\u010e\7\n\2\2\u010e;\3\2\2\2\u010f\u0110\7.\2\2\u0110")
        buf.write("\u0111\7\t\2\2\u0111\u0112\5\4\3\2\u0112\u0113\7\n\2\2")
        buf.write("\u0113=\3\2\2\2\u0114\u0115\7/\2\2\u0115\u0116\7\t\2\2")
        buf.write("\u0116\u0117\5\4\3\2\u0117\u0118\7\n\2\2\u0118?\3\2\2")
        buf.write("\2\u0119\u011a\t\6\2\2\u011aA\3\2\2\2\22K_afu\u0082\u008d")
        buf.write("\u0098\u00a7\u00a9\u00b7\u00c4\u00ca\u00db\u00f5\u0101")
        return buf.getvalue()


class MatexParser ( Parser ):

    grammarFileName = "MatexParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "'.'", "'|'", "'\\lim'", 
                     "<INVALID>", "'\\int'", "'\\sum'", "'\\prod'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\times'", "'\\cdot'", "'\\div'", "'\\frac'", "'_'", 
                     "'^'", "':'", "'\\'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\infty'", "'='", "'<'", "'\\leq'", "'>'", "'\\geq'", 
                     "'!'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "L_PAREN", 
                      "R_PAREN", "L_BRACE", "R_BRACE", "L_BRACKET", "R_BRACKET", 
                      "COMMA", "DOT", "BAR", "FUNC_LIM", "LIM_APPROACH_SYM", 
                      "FUNC_INT", "FUNC_SUM", "FUNC_PROD", "FUNC_LOG", "FUNC_LN", 
                      "FUNC_SIN", "FUNC_COS", "FUNC_TAN", "FUNC_CSC", "FUNC_SEC", 
                      "FUNC_COT", "FUNC_ARCSIN", "FUNC_ARCCOS", "FUNC_ARCTAN", 
                      "FUNC_ARCCSC", "FUNC_ARCSEC", "FUNC_ARCCOT", "FUNC_SINH", 
                      "FUNC_COSH", "FUNC_TANH", "FUNC_ARCSINH", "FUNC_ARCCOSH", 
                      "FUNC_ARCTANH", "FUNC_SQRT", "CMD_TIMES", "CMD_CDOT", 
                      "CMD_DIV", "CMD_FRAC", "UNDERSCORE", "CARET", "COLON", 
                      "BACKSLASH", "NUMBER", "VARIABLE", "MIXNUMBER", "INFINITY", 
                      "EQ", "LT", "LTE", "GT", "GTE", "BANG", "GREEKLETTER", 
                      "WS" ]

    RULE_math = 0
    RULE_equality = 1
    RULE_megaExpr = 2
    RULE_expr = 3
    RULE_summationExpr = 4
    RULE_productExpr = 5
    RULE_tailExpr = 6
    RULE_funcParams = 7
    RULE_subtractionExpr = 8
    RULE_additionExpr = 9
    RULE_divisionExpr = 10
    RULE_multiplicationExpr = 11
    RULE_fracExpr = 12
    RULE_powExpr = 13
    RULE_exponentiationExpr = 14
    RULE_signedAtom = 15
    RULE_negateAtom = 16
    RULE_localMultiplication = 17
    RULE_atom = 18
    RULE_variable = 19
    RULE_indexedVariable = 20
    RULE_constant = 21
    RULE_number = 22
    RULE_absolute = 23
    RULE_factorial = 24
    RULE_func = 25
    RULE_funcname = 26
    RULE_subexpr = 27
    RULE_supexpr = 28
    RULE_subeq = 29
    RULE_supeq = 30
    RULE_relop = 31

    ruleNames =  [ "math", "equality", "megaExpr", "expr", "summationExpr", 
                   "productExpr", "tailExpr", "funcParams", "subtractionExpr", 
                   "additionExpr", "divisionExpr", "multiplicationExpr", 
                   "fracExpr", "powExpr", "exponentiationExpr", "signedAtom", 
                   "negateAtom", "localMultiplication", "atom", "variable", 
                   "indexedVariable", "constant", "number", "absolute", 
                   "factorial", "func", "funcname", "subexpr", "supexpr", 
                   "subeq", "supeq", "relop" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MUL=3
    DIV=4
    L_PAREN=5
    R_PAREN=6
    L_BRACE=7
    R_BRACE=8
    L_BRACKET=9
    R_BRACKET=10
    COMMA=11
    DOT=12
    BAR=13
    FUNC_LIM=14
    LIM_APPROACH_SYM=15
    FUNC_INT=16
    FUNC_SUM=17
    FUNC_PROD=18
    FUNC_LOG=19
    FUNC_LN=20
    FUNC_SIN=21
    FUNC_COS=22
    FUNC_TAN=23
    FUNC_CSC=24
    FUNC_SEC=25
    FUNC_COT=26
    FUNC_ARCSIN=27
    FUNC_ARCCOS=28
    FUNC_ARCTAN=29
    FUNC_ARCCSC=30
    FUNC_ARCSEC=31
    FUNC_ARCCOT=32
    FUNC_SINH=33
    FUNC_COSH=34
    FUNC_TANH=35
    FUNC_ARCSINH=36
    FUNC_ARCCOSH=37
    FUNC_ARCTANH=38
    FUNC_SQRT=39
    CMD_TIMES=40
    CMD_CDOT=41
    CMD_DIV=42
    CMD_FRAC=43
    UNDERSCORE=44
    CARET=45
    COLON=46
    BACKSLASH=47
    NUMBER=48
    VARIABLE=49
    MIXNUMBER=50
    INFINITY=51
    EQ=52
    LT=53
    LTE=54
    GT=55
    GTE=56
    BANG=57
    GREEKLETTER=58
    WS=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_math

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath" ):
                listener.enterMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath" ):
                listener.exitMath(self)




    def math(self):

        localctx = MatexParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_math)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EqualityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatexParser.ExprContext)
            else:
                return self.getTypedRuleContext(MatexParser.ExprContext,i)


        def EQ(self):
            return self.getToken(MatexParser.EQ, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)




    def equality(self):

        localctx = MatexParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.expr()
            self.state = 67
            self.match(MatexParser.EQ)
            self.state = 68
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MegaExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def summationExpr(self):
            return self.getTypedRuleContext(MatexParser.SummationExprContext,0)


        def productExpr(self):
            return self.getTypedRuleContext(MatexParser.ProductExprContext,0)


        def megaExpr(self):
            return self.getTypedRuleContext(MatexParser.MegaExprContext,0)


        def PLUS(self):
            return self.getToken(MatexParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MatexParser.MINUS, 0)

        def MUL(self):
            return self.getToken(MatexParser.MUL, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_megaExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMegaExpr" ):
                listener.enterMegaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMegaExpr" ):
                listener.exitMegaExpr(self)



    def megaExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatexParser.MegaExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_megaExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.FUNC_SUM]:
                self.state = 71
                self.summationExpr()
                pass
            elif token in [MatexParser.FUNC_PROD]:
                self.state = 72
                self.productExpr()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 93
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 75
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 76
                        self.match(MatexParser.PLUS)
                        self.state = 77
                        self.summationExpr()
                        pass

                    elif la_ == 2:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 78
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 79
                        self.match(MatexParser.PLUS)
                        self.state = 80
                        self.productExpr()
                        pass

                    elif la_ == 3:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 81
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 82
                        self.match(MatexParser.MINUS)
                        self.state = 83
                        self.summationExpr()
                        pass

                    elif la_ == 4:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 84
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 85
                        self.match(MatexParser.MINUS)
                        self.state = 86
                        self.productExpr()
                        pass

                    elif la_ == 5:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 87
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 88
                        self.match(MatexParser.MUL)
                        self.state = 89
                        self.summationExpr()
                        pass

                    elif la_ == 6:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 90
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 91
                        self.match(MatexParser.MUL)
                        self.state = 92
                        self.productExpr()
                        pass

             
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subtractionExpr(self):
            return self.getTypedRuleContext(MatexParser.SubtractionExprContext,0)


        def megaExpr(self):
            return self.getTypedRuleContext(MatexParser.MegaExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = MatexParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS, MatexParser.L_PAREN, MatexParser.BAR, MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_SQRT, MatexParser.CMD_FRAC, MatexParser.NUMBER, MatexParser.VARIABLE, MatexParser.MIXNUMBER, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.subtractionExpr(0)
                pass
            elif token in [MatexParser.FUNC_SUM, MatexParser.FUNC_PROD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.megaExpr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SummationExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_SUM(self):
            return self.getToken(MatexParser.FUNC_SUM, 0)

        def funcParams(self):
            return self.getTypedRuleContext(MatexParser.FuncParamsContext,0)


        def tailExpr(self):
            return self.getTypedRuleContext(MatexParser.TailExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_summationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummationExpr" ):
                listener.enterSummationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummationExpr" ):
                listener.exitSummationExpr(self)




    def summationExpr(self):

        localctx = MatexParser.SummationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_summationExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MatexParser.FUNC_SUM)
            self.state = 103
            self.funcParams()
            self.state = 104
            self.tailExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProductExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_PROD(self):
            return self.getToken(MatexParser.FUNC_PROD, 0)

        def funcParams(self):
            return self.getTypedRuleContext(MatexParser.FuncParamsContext,0)


        def tailExpr(self):
            return self.getTypedRuleContext(MatexParser.TailExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_productExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProductExpr" ):
                listener.enterProductExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProductExpr" ):
                listener.exitProductExpr(self)




    def productExpr(self):

        localctx = MatexParser.ProductExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_productExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(MatexParser.FUNC_PROD)
            self.state = 107
            self.funcParams()
            self.state = 108
            self.tailExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TailExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_tailExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTailExpr" ):
                listener.enterTailExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTailExpr" ):
                listener.exitTailExpr(self)




    def tailExpr(self):

        localctx = MatexParser.TailExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tailExpr)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS, MatexParser.L_PAREN, MatexParser.BAR, MatexParser.FUNC_SUM, MatexParser.FUNC_PROD, MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_SQRT, MatexParser.CMD_FRAC, MatexParser.NUMBER, MatexParser.VARIABLE, MatexParser.MIXNUMBER, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.expr()
                pass
            elif token in [MatexParser.L_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(MatexParser.L_BRACE)
                self.state = 112
                self.expr()
                self.state = 113
                self.match(MatexParser.R_BRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subeq(self):
            return self.getTypedRuleContext(MatexParser.SubeqContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(MatexParser.SupexprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_funcParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncParams" ):
                listener.enterFuncParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncParams" ):
                listener.exitFuncParams(self)




    def funcParams(self):

        localctx = MatexParser.FuncParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcParams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.subeq()
            self.state = 118
            self.supexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubtractionExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additionExpr(self):
            return self.getTypedRuleContext(MatexParser.AdditionExprContext,0)


        def subtractionExpr(self):
            return self.getTypedRuleContext(MatexParser.SubtractionExprContext,0)


        def MINUS(self):
            return self.getToken(MatexParser.MINUS, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_subtractionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtractionExpr" ):
                listener.enterSubtractionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtractionExpr" ):
                listener.exitSubtractionExpr(self)



    def subtractionExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatexParser.SubtractionExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_subtractionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.additionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.SubtractionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_subtractionExpr)
                    self.state = 123
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 124
                    self.match(MatexParser.MINUS)
                    self.state = 125
                    self.additionExpr(0) 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AdditionExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def divisionExpr(self):
            return self.getTypedRuleContext(MatexParser.DivisionExprContext,0)


        def additionExpr(self):
            return self.getTypedRuleContext(MatexParser.AdditionExprContext,0)


        def PLUS(self):
            return self.getToken(MatexParser.PLUS, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_additionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionExpr" ):
                listener.enterAdditionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionExpr" ):
                listener.exitAdditionExpr(self)



    def additionExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatexParser.AdditionExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_additionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.divisionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.AdditionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additionExpr)
                    self.state = 134
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 135
                    self.match(MatexParser.PLUS)
                    self.state = 136
                    self.divisionExpr(0) 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DivisionExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicationExpr(self):
            return self.getTypedRuleContext(MatexParser.MultiplicationExprContext,0)


        def divisionExpr(self):
            return self.getTypedRuleContext(MatexParser.DivisionExprContext,0)


        def DIV(self):
            return self.getToken(MatexParser.DIV, 0)

        def CMD_DIV(self):
            return self.getToken(MatexParser.CMD_DIV, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_divisionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivisionExpr" ):
                listener.enterDivisionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivisionExpr" ):
                listener.exitDivisionExpr(self)



    def divisionExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatexParser.DivisionExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_divisionExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.multiplicationExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.DivisionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_divisionExpr)
                    self.state = 145
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 146
                    _la = self._input.LA(1)
                    if not(_la==MatexParser.DIV or _la==MatexParser.CMD_DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 147
                    self.multiplicationExpr(0) 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MultiplicationExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def powExpr(self):
            return self.getTypedRuleContext(MatexParser.PowExprContext,0)


        def multiplicationExpr(self):
            return self.getTypedRuleContext(MatexParser.MultiplicationExprContext,0)


        def MUL(self):
            return self.getToken(MatexParser.MUL, 0)

        def CMD_TIMES(self):
            return self.getToken(MatexParser.CMD_TIMES, 0)

        def CMD_CDOT(self):
            return self.getToken(MatexParser.CMD_CDOT, 0)

        def fracExpr(self):
            return self.getTypedRuleContext(MatexParser.FracExprContext,0)


        def exponentiationExpr(self):
            return self.getTypedRuleContext(MatexParser.ExponentiationExprContext,0)


        def atom(self):
            return self.getTypedRuleContext(MatexParser.AtomContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_multiplicationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpr" ):
                listener.enterMultiplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpr" ):
                listener.exitMultiplicationExpr(self)



    def multiplicationExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatexParser.MultiplicationExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_multiplicationExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 165
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                        self.state = 156
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 157
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MUL) | (1 << MatexParser.CMD_TIMES) | (1 << MatexParser.CMD_CDOT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 158
                        self.powExpr()
                        pass

                    elif la_ == 2:
                        localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                        self.state = 159
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 160
                        self.fracExpr()
                        pass

                    elif la_ == 3:
                        localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                        self.state = 161
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 162
                        self.exponentiationExpr()
                        pass

                    elif la_ == 4:
                        localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                        self.state = 163
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 164
                        self.atom()
                        pass

             
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FracExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CMD_FRAC(self):
            return self.getToken(MatexParser.CMD_FRAC, 0)

        def L_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MatexParser.L_BRACE)
            else:
                return self.getToken(MatexParser.L_BRACE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatexParser.ExprContext)
            else:
                return self.getTypedRuleContext(MatexParser.ExprContext,i)


        def R_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MatexParser.R_BRACE)
            else:
                return self.getToken(MatexParser.R_BRACE, i)

        def getRuleIndex(self):
            return MatexParser.RULE_fracExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFracExpr" ):
                listener.enterFracExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFracExpr" ):
                listener.exitFracExpr(self)




    def fracExpr(self):

        localctx = MatexParser.FracExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_fracExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MatexParser.CMD_FRAC)
            self.state = 171
            self.match(MatexParser.L_BRACE)
            self.state = 172
            self.expr()
            self.state = 173
            self.match(MatexParser.R_BRACE)
            self.state = 174
            self.match(MatexParser.L_BRACE)
            self.state = 175
            self.expr()
            self.state = 176
            self.match(MatexParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PowExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signedAtom(self):
            return self.getTypedRuleContext(MatexParser.SignedAtomContext,0)


        def fracExpr(self):
            return self.getTypedRuleContext(MatexParser.FracExprContext,0)


        def exponentiationExpr(self):
            return self.getTypedRuleContext(MatexParser.ExponentiationExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_powExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowExpr" ):
                listener.enterPowExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowExpr" ):
                listener.exitPowExpr(self)




    def powExpr(self):

        localctx = MatexParser.PowExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_powExpr)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.signedAtom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.fracExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.exponentiationExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExponentiationExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signedAtom(self):
            return self.getTypedRuleContext(MatexParser.SignedAtomContext,0)


        def CARET(self):
            return self.getToken(MatexParser.CARET, 0)

        def number(self):
            return self.getTypedRuleContext(MatexParser.NumberContext,0)


        def variable(self):
            return self.getTypedRuleContext(MatexParser.VariableContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(MatexParser.SupexprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_exponentiationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponentiationExpr" ):
                listener.enterExponentiationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponentiationExpr" ):
                listener.exitExponentiationExpr(self)




    def exponentiationExpr(self):

        localctx = MatexParser.ExponentiationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exponentiationExpr)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.signedAtom()
                self.state = 184
                self.match(MatexParser.CARET)
                self.state = 185
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.signedAtom()
                self.state = 188
                self.match(MatexParser.CARET)
                self.state = 189
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.signedAtom()
                self.state = 192
                self.supexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SignedAtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negateAtom(self):
            return self.getTypedRuleContext(MatexParser.NegateAtomContext,0)


        def localMultiplication(self):
            return self.getTypedRuleContext(MatexParser.LocalMultiplicationContext,0)


        def func(self):
            return self.getTypedRuleContext(MatexParser.FuncContext,0)


        def atom(self):
            return self.getTypedRuleContext(MatexParser.AtomContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_signedAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedAtom" ):
                listener.enterSignedAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedAtom" ):
                listener.exitSignedAtom(self)




    def signedAtom(self):

        localctx = MatexParser.SignedAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_signedAtom)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.negateAtom()
                pass
            elif token in [MatexParser.MIXNUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.localMultiplication()
                pass
            elif token in [MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_SQRT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.func()
                pass
            elif token in [MatexParser.L_PAREN, MatexParser.BAR, MatexParser.NUMBER, MatexParser.VARIABLE, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NegateAtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MatexParser.MINUS, 0)

        def signedAtom(self):
            return self.getTypedRuleContext(MatexParser.SignedAtomContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_negateAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegateAtom" ):
                listener.enterNegateAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegateAtom" ):
                listener.exitNegateAtom(self)




    def negateAtom(self):

        localctx = MatexParser.NegateAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_negateAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MatexParser.MINUS)
            self.state = 203
            self.signedAtom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LocalMultiplicationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIXNUMBER(self):
            return self.getToken(MatexParser.MIXNUMBER, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_localMultiplication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalMultiplication" ):
                listener.enterLocalMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalMultiplication" ):
                listener.exitLocalMultiplication(self)




    def localMultiplication(self):

        localctx = MatexParser.LocalMultiplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_localMultiplication)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MatexParser.MIXNUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(MatexParser.VariableContext,0)


        def indexedVariable(self):
            return self.getTypedRuleContext(MatexParser.IndexedVariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(MatexParser.ConstantContext,0)


        def number(self):
            return self.getTypedRuleContext(MatexParser.NumberContext,0)


        def absolute(self):
            return self.getTypedRuleContext(MatexParser.AbsoluteContext,0)


        def factorial(self):
            return self.getTypedRuleContext(MatexParser.FactorialContext,0)


        def L_PAREN(self):
            return self.getToken(MatexParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(MatexParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = MatexParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_atom)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.indexedVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 211
                self.absolute()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 212
                self.factorial()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 213
                self.match(MatexParser.L_PAREN)
                self.state = 214
                self.expr()
                self.state = 215
                self.match(MatexParser.R_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(MatexParser.VARIABLE, 0)

        def GREEKLETTER(self):
            return self.getToken(MatexParser.GREEKLETTER, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = MatexParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==MatexParser.VARIABLE or _la==MatexParser.GREEKLETTER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IndexedVariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(MatexParser.VARIABLE, 0)

        def subexpr(self):
            return self.getTypedRuleContext(MatexParser.SubexprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_indexedVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexedVariable" ):
                listener.enterIndexedVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexedVariable" ):
                listener.exitIndexedVariable(self)




    def indexedVariable(self):

        localctx = MatexParser.IndexedVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_indexedVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MatexParser.VARIABLE)
            self.state = 222
            self.subexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INFINITY(self):
            return self.getToken(MatexParser.INFINITY, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = MatexParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MatexParser.INFINITY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MatexParser.NUMBER, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = MatexParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MatexParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AbsoluteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BAR(self, i:int=None):
            if i is None:
                return self.getTokens(MatexParser.BAR)
            else:
                return self.getToken(MatexParser.BAR, i)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_absolute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbsolute" ):
                listener.enterAbsolute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbsolute" ):
                listener.exitAbsolute(self)




    def absolute(self):

        localctx = MatexParser.AbsoluteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_absolute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MatexParser.BAR)
            self.state = 229
            self.expr()
            self.state = 230
            self.match(MatexParser.BAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MatexParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(MatexParser.R_PAREN, 0)

        def BANG(self):
            return self.getToken(MatexParser.BANG, 0)

        def number(self):
            return self.getTypedRuleContext(MatexParser.NumberContext,0)


        def variable(self):
            return self.getTypedRuleContext(MatexParser.VariableContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_factorial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorial" ):
                listener.enterFactorial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorial" ):
                listener.exitFactorial(self)




    def factorial(self):

        localctx = MatexParser.FactorialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_factorial)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(MatexParser.L_PAREN)
                self.state = 233
                self.expr()
                self.state = 234
                self.match(MatexParser.R_PAREN)
                self.state = 235
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.number()
                self.state = 238
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.variable()
                self.state = 241
                self.match(MatexParser.BANG)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcname(self):
            return self.getTypedRuleContext(MatexParser.FuncnameContext,0)


        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def L_PAREN(self):
            return self.getToken(MatexParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(MatexParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = MatexParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_func)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.funcname()
                self.state = 246
                self.match(MatexParser.L_BRACE)
                self.state = 247
                self.expr()
                self.state = 248
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.funcname()
                self.state = 251
                self.match(MatexParser.L_PAREN)
                self.state = 252
                self.expr()
                self.state = 253
                self.match(MatexParser.R_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_LOG(self):
            return self.getToken(MatexParser.FUNC_LOG, 0)

        def FUNC_LN(self):
            return self.getToken(MatexParser.FUNC_LN, 0)

        def FUNC_SQRT(self):
            return self.getToken(MatexParser.FUNC_SQRT, 0)

        def FUNC_SIN(self):
            return self.getToken(MatexParser.FUNC_SIN, 0)

        def FUNC_COS(self):
            return self.getToken(MatexParser.FUNC_COS, 0)

        def FUNC_TAN(self):
            return self.getToken(MatexParser.FUNC_TAN, 0)

        def FUNC_CSC(self):
            return self.getToken(MatexParser.FUNC_CSC, 0)

        def FUNC_SEC(self):
            return self.getToken(MatexParser.FUNC_SEC, 0)

        def FUNC_COT(self):
            return self.getToken(MatexParser.FUNC_COT, 0)

        def FUNC_ARCSIN(self):
            return self.getToken(MatexParser.FUNC_ARCSIN, 0)

        def FUNC_ARCCOS(self):
            return self.getToken(MatexParser.FUNC_ARCCOS, 0)

        def FUNC_ARCTAN(self):
            return self.getToken(MatexParser.FUNC_ARCTAN, 0)

        def FUNC_ARCCSC(self):
            return self.getToken(MatexParser.FUNC_ARCCSC, 0)

        def FUNC_ARCSEC(self):
            return self.getToken(MatexParser.FUNC_ARCSEC, 0)

        def FUNC_ARCCOT(self):
            return self.getToken(MatexParser.FUNC_ARCCOT, 0)

        def FUNC_SINH(self):
            return self.getToken(MatexParser.FUNC_SINH, 0)

        def FUNC_COSH(self):
            return self.getToken(MatexParser.FUNC_COSH, 0)

        def FUNC_TANH(self):
            return self.getToken(MatexParser.FUNC_TANH, 0)

        def FUNC_ARCSINH(self):
            return self.getToken(MatexParser.FUNC_ARCSINH, 0)

        def FUNC_ARCCOSH(self):
            return self.getToken(MatexParser.FUNC_ARCCOSH, 0)

        def FUNC_ARCTANH(self):
            return self.getToken(MatexParser.FUNC_ARCTANH, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_funcname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncname" ):
                listener.enterFuncname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncname" ):
                listener.exitFuncname(self)




    def funcname(self):

        localctx = MatexParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.FUNC_LOG) | (1 << MatexParser.FUNC_LN) | (1 << MatexParser.FUNC_SIN) | (1 << MatexParser.FUNC_COS) | (1 << MatexParser.FUNC_TAN) | (1 << MatexParser.FUNC_CSC) | (1 << MatexParser.FUNC_SEC) | (1 << MatexParser.FUNC_COT) | (1 << MatexParser.FUNC_ARCSIN) | (1 << MatexParser.FUNC_ARCCOS) | (1 << MatexParser.FUNC_ARCTAN) | (1 << MatexParser.FUNC_ARCCSC) | (1 << MatexParser.FUNC_ARCSEC) | (1 << MatexParser.FUNC_ARCCOT) | (1 << MatexParser.FUNC_SINH) | (1 << MatexParser.FUNC_COSH) | (1 << MatexParser.FUNC_TANH) | (1 << MatexParser.FUNC_ARCSINH) | (1 << MatexParser.FUNC_ARCCOSH) | (1 << MatexParser.FUNC_ARCTANH) | (1 << MatexParser.FUNC_SQRT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(MatexParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_subexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubexpr" ):
                listener.enterSubexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubexpr" ):
                listener.exitSubexpr(self)




    def subexpr(self):

        localctx = MatexParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MatexParser.UNDERSCORE)
            self.state = 260
            self.match(MatexParser.L_BRACE)
            self.state = 261
            self.expr()
            self.state = 262
            self.match(MatexParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SupexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(MatexParser.CARET, 0)

        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_supexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSupexpr" ):
                listener.enterSupexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSupexpr" ):
                listener.exitSupexpr(self)




    def supexpr(self):

        localctx = MatexParser.SupexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(MatexParser.CARET)
            self.state = 265
            self.match(MatexParser.L_BRACE)
            self.state = 266
            self.expr()
            self.state = 267
            self.match(MatexParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubeqContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(MatexParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def equality(self):
            return self.getTypedRuleContext(MatexParser.EqualityContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_subeq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubeq" ):
                listener.enterSubeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubeq" ):
                listener.exitSubeq(self)




    def subeq(self):

        localctx = MatexParser.SubeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MatexParser.UNDERSCORE)
            self.state = 270
            self.match(MatexParser.L_BRACE)
            self.state = 271
            self.equality()
            self.state = 272
            self.match(MatexParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SupeqContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(MatexParser.CARET, 0)

        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def equality(self):
            return self.getTypedRuleContext(MatexParser.EqualityContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_supeq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSupeq" ):
                listener.enterSupeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSupeq" ):
                listener.exitSupeq(self)




    def supeq(self):

        localctx = MatexParser.SupeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_supeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MatexParser.CARET)
            self.state = 275
            self.match(MatexParser.L_BRACE)
            self.state = 276
            self.equality()
            self.state = 277
            self.match(MatexParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MatexParser.EQ, 0)

        def LT(self):
            return self.getToken(MatexParser.LT, 0)

        def LTE(self):
            return self.getToken(MatexParser.LTE, 0)

        def GT(self):
            return self.getToken(MatexParser.GT, 0)

        def GTE(self):
            return self.getToken(MatexParser.GTE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)




    def relop(self):

        localctx = MatexParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.EQ) | (1 << MatexParser.LT) | (1 << MatexParser.LTE) | (1 << MatexParser.GT) | (1 << MatexParser.GTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.megaExpr_sempred
        self._predicates[8] = self.subtractionExpr_sempred
        self._predicates[9] = self.additionExpr_sempred
        self._predicates[10] = self.divisionExpr_sempred
        self._predicates[11] = self.multiplicationExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def megaExpr_sempred(self, localctx:MegaExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def subtractionExpr_sempred(self, localctx:SubtractionExprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def additionExpr_sempred(self, localctx:AdditionExprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def divisionExpr_sempred(self, localctx:DivisionExprContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         

    def multiplicationExpr_sempred(self, localctx:MultiplicationExprContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         




