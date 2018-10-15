# Generated from .\pymatex\grammar\MatexParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u0144\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4S\n\4\5\4U\n\4\3\4\3\4")
        buf.write("\3\4\5\4Z\n\4\3\4\3\4\5\4^\n\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\7\4i\n\4\f\4\16\4l\13\4\3\5\3\5\3\5\5\5q")
        buf.write("\n\5\3\6\3\6\3\6\5\6v\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0086\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u0095\n\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00a0\n\f")
        buf.write("\f\f\16\f\u00a3\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00ab")
        buf.write("\n\r\f\r\16\r\u00ae\13\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\7\16\u00b6\n\16\f\16\16\16\u00b9\13\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\7\17\u00c1\n\17\f\17\16\17\u00c4\13\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00cc\n\20\f\20\16")
        buf.write("\20\u00cf\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\5\22\u00dc\n\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e9\n\23\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u00ef\n\24\3\25\3\25\3\25\3\26\3")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0104\n\27\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u011e\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u012a\n\36\3\37\3\37\3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\2\b\6\26\30\32\34\36%\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF\2\b\4\2\6\6,,\4")
        buf.write("\2\5\5*+\4\2\63\63\65\66\4\2\64\64>>\3\2\25)\3\28<\2\u0143")
        buf.write("\2H\3\2\2\2\4K\3\2\2\2\6]\3\2\2\2\bp\3\2\2\2\nu\3\2\2")
        buf.write("\2\f\u0085\3\2\2\2\16\u0087\3\2\2\2\20\u008b\3\2\2\2\22")
        buf.write("\u0094\3\2\2\2\24\u0096\3\2\2\2\26\u0099\3\2\2\2\30\u00a4")
        buf.write("\3\2\2\2\32\u00af\3\2\2\2\34\u00ba\3\2\2\2\36\u00c5\3")
        buf.write("\2\2\2 \u00d0\3\2\2\2\"\u00db\3\2\2\2$\u00e8\3\2\2\2&")
        buf.write("\u00ee\3\2\2\2(\u00f0\3\2\2\2*\u00f3\3\2\2\2,\u0103\3")
        buf.write("\2\2\2.\u0105\3\2\2\2\60\u0107\3\2\2\2\62\u010a\3\2\2")
        buf.write("\2\64\u010c\3\2\2\2\66\u010e\3\2\2\28\u011d\3\2\2\2:\u0129")
        buf.write("\3\2\2\2<\u012b\3\2\2\2>\u012d\3\2\2\2@\u0132\3\2\2\2")
        buf.write("B\u0137\3\2\2\2D\u013c\3\2\2\2F\u0141\3\2\2\2HI\5\n\6")
        buf.write("\2IJ\7\2\2\3J\3\3\2\2\2KL\5\n\6\2LM\78\2\2MN\5\n\6\2N")
        buf.write("\5\3\2\2\2OT\b\4\1\2PR\5\30\r\2QS\7\5\2\2RQ\3\2\2\2RS")
        buf.write("\3\2\2\2SU\3\2\2\2TP\3\2\2\2TU\3\2\2\2UV\3\2\2\2V^\5\b")
        buf.write("\5\2WY\5\26\f\2XZ\7\5\2\2YX\3\2\2\2YZ\3\2\2\2Z[\3\2\2")
        buf.write("\2[\\\5\b\5\2\\^\3\2\2\2]O\3\2\2\2]W\3\2\2\2^j\3\2\2\2")
        buf.write("_`\f\5\2\2`a\7\3\2\2ai\5\b\5\2bc\f\4\2\2cd\7\4\2\2di\5")
        buf.write("\b\5\2ef\f\3\2\2fg\7\5\2\2gi\5\b\5\2h_\3\2\2\2hb\3\2\2")
        buf.write("\2he\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2k\7\3\2\2\2")
        buf.write("lj\3\2\2\2mq\5\f\7\2nq\5\16\b\2oq\5\20\t\2pm\3\2\2\2p")
        buf.write("n\3\2\2\2po\3\2\2\2q\t\3\2\2\2rv\5\30\r\2sv\5\26\f\2t")
        buf.write("v\5\6\4\2ur\3\2\2\2us\3\2\2\2ut\3\2\2\2v\13\3\2\2\2wx")
        buf.write("\7\22\2\2xy\5> \2yz\5@!\2z{\7\t\2\2{|\5\n\6\2|}\7\63\2")
        buf.write("\2}~\7\n\2\2~\u0086\3\2\2\2\177\u0080\7\22\2\2\u0080\u0081")
        buf.write("\5> \2\u0081\u0082\5@!\2\u0082\u0083\5\n\6\2\u0083\u0084")
        buf.write("\7\63\2\2\u0084\u0086\3\2\2\2\u0085w\3\2\2\2\u0085\177")
        buf.write("\3\2\2\2\u0086\r\3\2\2\2\u0087\u0088\7\23\2\2\u0088\u0089")
        buf.write("\5\24\13\2\u0089\u008a\5\22\n\2\u008a\17\3\2\2\2\u008b")
        buf.write("\u008c\7\24\2\2\u008c\u008d\5\24\13\2\u008d\u008e\5\22")
        buf.write("\n\2\u008e\21\3\2\2\2\u008f\u0095\5\n\6\2\u0090\u0091")
        buf.write("\7\t\2\2\u0091\u0092\5\n\6\2\u0092\u0093\7\n\2\2\u0093")
        buf.write("\u0095\3\2\2\2\u0094\u008f\3\2\2\2\u0094\u0090\3\2\2\2")
        buf.write("\u0095\23\3\2\2\2\u0096\u0097\5B\"\2\u0097\u0098\5@!\2")
        buf.write("\u0098\25\3\2\2\2\u0099\u009a\b\f\1\2\u009a\u009b\5\30")
        buf.write("\r\2\u009b\u009c\5\30\r\2\u009c\u00a1\3\2\2\2\u009d\u009e")
        buf.write("\f\3\2\2\u009e\u00a0\5\30\r\2\u009f\u009d\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\27\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\b\r")
        buf.write("\1\2\u00a5\u00a6\5\32\16\2\u00a6\u00ac\3\2\2\2\u00a7\u00a8")
        buf.write("\f\3\2\2\u00a8\u00a9\7\4\2\2\u00a9\u00ab\5\32\16\2\u00aa")
        buf.write("\u00a7\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\31\3\2\2\2\u00ae\u00ac\3\2")
        buf.write("\2\2\u00af\u00b0\b\16\1\2\u00b0\u00b1\5\34\17\2\u00b1")
        buf.write("\u00b7\3\2\2\2\u00b2\u00b3\f\3\2\2\u00b3\u00b4\7\3\2\2")
        buf.write("\u00b4\u00b6\5\34\17\2\u00b5\u00b2\3\2\2\2\u00b6\u00b9")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8")
        buf.write("\33\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb\b\17\1\2\u00bb")
        buf.write("\u00bc\5\36\20\2\u00bc\u00c2\3\2\2\2\u00bd\u00be\f\3\2")
        buf.write("\2\u00be\u00bf\t\2\2\2\u00bf\u00c1\5\36\20\2\u00c0\u00bd")
        buf.write("\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\35\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5")
        buf.write("\u00c6\b\20\1\2\u00c6\u00c7\5\"\22\2\u00c7\u00cd\3\2\2")
        buf.write("\2\u00c8\u00c9\f\3\2\2\u00c9\u00ca\t\3\2\2\u00ca\u00cc")
        buf.write("\5\"\22\2\u00cb\u00c8\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\37\3\2\2\2\u00cf")
        buf.write("\u00cd\3\2\2\2\u00d0\u00d1\7-\2\2\u00d1\u00d2\7\t\2\2")
        buf.write("\u00d2\u00d3\5\n\6\2\u00d3\u00d4\7\n\2\2\u00d4\u00d5\7")
        buf.write("\t\2\2\u00d5\u00d6\5\n\6\2\u00d6\u00d7\7\n\2\2\u00d7!")
        buf.write("\3\2\2\2\u00d8\u00dc\5&\24\2\u00d9\u00dc\5 \21\2\u00da")
        buf.write("\u00dc\5$\23\2\u00db\u00d8\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00da\3\2\2\2\u00dc#\3\2\2\2\u00dd\u00de\5&\24")
        buf.write("\2\u00de\u00df\7/\2\2\u00df\u00e0\5\64\33\2\u00e0\u00e9")
        buf.write("\3\2\2\2\u00e1\u00e2\5&\24\2\u00e2\u00e3\7/\2\2\u00e3")
        buf.write("\u00e4\5.\30\2\u00e4\u00e9\3\2\2\2\u00e5\u00e6\5&\24\2")
        buf.write("\u00e6\u00e7\5@!\2\u00e7\u00e9\3\2\2\2\u00e8\u00dd\3\2")
        buf.write("\2\2\u00e8\u00e1\3\2\2\2\u00e8\u00e5\3\2\2\2\u00e9%\3")
        buf.write("\2\2\2\u00ea\u00ef\5(\25\2\u00eb\u00ef\5*\26\2\u00ec\u00ef")
        buf.write("\5:\36\2\u00ed\u00ef\5,\27\2\u00ee\u00ea\3\2\2\2\u00ee")
        buf.write("\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2")
        buf.write("\u00ef\'\3\2\2\2\u00f0\u00f1\7\4\2\2\u00f1\u00f2\5&\24")
        buf.write("\2\u00f2)\3\2\2\2\u00f3\u00f4\t\4\2\2\u00f4+\3\2\2\2\u00f5")
        buf.write("\u0104\5.\30\2\u00f6\u0104\5\60\31\2\u00f7\u0104\5\62")
        buf.write("\32\2\u00f8\u0104\5\64\33\2\u00f9\u0104\5\66\34\2\u00fa")
        buf.write("\u0104\58\35\2\u00fb\u00fc\7\13\2\2\u00fc\u00fd\5\n\6")
        buf.write("\2\u00fd\u00fe\7\f\2\2\u00fe\u0104\3\2\2\2\u00ff\u0100")
        buf.write("\7\7\2\2\u0100\u0101\5\n\6\2\u0101\u0102\7\b\2\2\u0102")
        buf.write("\u0104\3\2\2\2\u0103\u00f5\3\2\2\2\u0103\u00f6\3\2\2\2")
        buf.write("\u0103\u00f7\3\2\2\2\u0103\u00f8\3\2\2\2\u0103\u00f9\3")
        buf.write("\2\2\2\u0103\u00fa\3\2\2\2\u0103\u00fb\3\2\2\2\u0103\u00ff")
        buf.write("\3\2\2\2\u0104-\3\2\2\2\u0105\u0106\t\5\2\2\u0106/\3\2")
        buf.write("\2\2\u0107\u0108\7\64\2\2\u0108\u0109\5> \2\u0109\61\3")
        buf.write("\2\2\2\u010a\u010b\7\67\2\2\u010b\63\3\2\2\2\u010c\u010d")
        buf.write("\7\62\2\2\u010d\65\3\2\2\2\u010e\u010f\7\17\2\2\u010f")
        buf.write("\u0110\5\n\6\2\u0110\u0111\7\17\2\2\u0111\67\3\2\2\2\u0112")
        buf.write("\u0113\7\7\2\2\u0113\u0114\5\n\6\2\u0114\u0115\7\b\2\2")
        buf.write("\u0115\u0116\7=\2\2\u0116\u011e\3\2\2\2\u0117\u0118\5")
        buf.write("\64\33\2\u0118\u0119\7=\2\2\u0119\u011e\3\2\2\2\u011a")
        buf.write("\u011b\5.\30\2\u011b\u011c\7=\2\2\u011c\u011e\3\2\2\2")
        buf.write("\u011d\u0112\3\2\2\2\u011d\u0117\3\2\2\2\u011d\u011a\3")
        buf.write("\2\2\2\u011e9\3\2\2\2\u011f\u0120\5<\37\2\u0120\u0121")
        buf.write("\7\t\2\2\u0121\u0122\5\n\6\2\u0122\u0123\7\n\2\2\u0123")
        buf.write("\u012a\3\2\2\2\u0124\u0125\5<\37\2\u0125\u0126\7\7\2\2")
        buf.write("\u0126\u0127\5\n\6\2\u0127\u0128\7\b\2\2\u0128\u012a\3")
        buf.write("\2\2\2\u0129\u011f\3\2\2\2\u0129\u0124\3\2\2\2\u012a;")
        buf.write("\3\2\2\2\u012b\u012c\t\6\2\2\u012c=\3\2\2\2\u012d\u012e")
        buf.write("\7.\2\2\u012e\u012f\7\t\2\2\u012f\u0130\5\n\6\2\u0130")
        buf.write("\u0131\7\n\2\2\u0131?\3\2\2\2\u0132\u0133\7/\2\2\u0133")
        buf.write("\u0134\7\t\2\2\u0134\u0135\5\n\6\2\u0135\u0136\7\n\2\2")
        buf.write("\u0136A\3\2\2\2\u0137\u0138\7.\2\2\u0138\u0139\7\t\2\2")
        buf.write("\u0139\u013a\5\4\3\2\u013a\u013b\7\n\2\2\u013bC\3\2\2")
        buf.write("\2\u013c\u013d\7/\2\2\u013d\u013e\7\t\2\2\u013e\u013f")
        buf.write("\5\4\3\2\u013f\u0140\7\n\2\2\u0140E\3\2\2\2\u0141\u0142")
        buf.write("\t\7\2\2\u0142G\3\2\2\2\27RTY]hjpu\u0085\u0094\u00a1\u00ac")
        buf.write("\u00b7\u00c2\u00cd\u00db\u00e8\u00ee\u0103\u011d\u0129")
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
                     "<INVALID>", "<INVALID>", "'\\infty'", "'='", "'<'", 
                     "'\\leq'", "'>'", "'\\geq'", "'!'" ]

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
                      "BACKSLASH", "NUMBER", "DERIVATIVE", "VARIABLE", "MIXNUMBER", 
                      "WORD", "INFINITY", "EQ", "LT", "LTE", "GT", "GTE", 
                      "BANG", "GREEKLETTER", "WS" ]

    RULE_math = 0
    RULE_equality = 1
    RULE_megaExpr = 2
    RULE_specialExpr = 3
    RULE_expr = 4
    RULE_integralExpr = 5
    RULE_summationExpr = 6
    RULE_productExpr = 7
    RULE_tailExpr = 8
    RULE_funcParams = 9
    RULE_implicitMultiplicationExpr = 10
    RULE_subtractionExpr = 11
    RULE_additionExpr = 12
    RULE_divisionExpr = 13
    RULE_multiplicationExpr = 14
    RULE_fracExpr = 15
    RULE_powExpr = 16
    RULE_exponentiationExpr = 17
    RULE_signedAtom = 18
    RULE_negateAtom = 19
    RULE_localMultiplication = 20
    RULE_atom = 21
    RULE_variable = 22
    RULE_indexedVariable = 23
    RULE_constant = 24
    RULE_number = 25
    RULE_absolute = 26
    RULE_factorial = 27
    RULE_func = 28
    RULE_funcname = 29
    RULE_subexpr = 30
    RULE_supexpr = 31
    RULE_subeq = 32
    RULE_supeq = 33
    RULE_relop = 34

    ruleNames =  [ "math", "equality", "megaExpr", "specialExpr", "expr", 
                   "integralExpr", "summationExpr", "productExpr", "tailExpr", 
                   "funcParams", "implicitMultiplicationExpr", "subtractionExpr", 
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
    DERIVATIVE=49
    VARIABLE=50
    MIXNUMBER=51
    WORD=52
    INFINITY=53
    EQ=54
    LT=55
    LTE=56
    GT=57
    GTE=58
    BANG=59
    GREEKLETTER=60
    WS=61

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


        def EOF(self):
            return self.getToken(MatexParser.EOF, 0)

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
            self.state = 70
            self.expr()
            self.state = 71
            self.match(MatexParser.EOF)
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
            self.state = 73
            self.expr()
            self.state = 74
            self.match(MatexParser.EQ)
            self.state = 75
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

        def specialExpr(self):
            return self.getTypedRuleContext(MatexParser.SpecialExprContext,0)


        def subtractionExpr(self):
            return self.getTypedRuleContext(MatexParser.SubtractionExprContext,0)


        def MUL(self):
            return self.getToken(MatexParser.MUL, 0)

        def implicitMultiplicationExpr(self):
            return self.getTypedRuleContext(MatexParser.ImplicitMultiplicationExprContext,0)


        def megaExpr(self):
            return self.getTypedRuleContext(MatexParser.MegaExprContext,0)


        def PLUS(self):
            return self.getToken(MatexParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MatexParser.MINUS, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MINUS) | (1 << MatexParser.L_PAREN) | (1 << MatexParser.L_BRACKET) | (1 << MatexParser.BAR) | (1 << MatexParser.FUNC_LOG) | (1 << MatexParser.FUNC_LN) | (1 << MatexParser.FUNC_SIN) | (1 << MatexParser.FUNC_COS) | (1 << MatexParser.FUNC_TAN) | (1 << MatexParser.FUNC_CSC) | (1 << MatexParser.FUNC_SEC) | (1 << MatexParser.FUNC_COT) | (1 << MatexParser.FUNC_ARCSIN) | (1 << MatexParser.FUNC_ARCCOS) | (1 << MatexParser.FUNC_ARCTAN) | (1 << MatexParser.FUNC_ARCCSC) | (1 << MatexParser.FUNC_ARCSEC) | (1 << MatexParser.FUNC_ARCCOT) | (1 << MatexParser.FUNC_SINH) | (1 << MatexParser.FUNC_COSH) | (1 << MatexParser.FUNC_TANH) | (1 << MatexParser.FUNC_ARCSINH) | (1 << MatexParser.FUNC_ARCCOSH) | (1 << MatexParser.FUNC_ARCTANH) | (1 << MatexParser.FUNC_SQRT) | (1 << MatexParser.CMD_FRAC) | (1 << MatexParser.NUMBER) | (1 << MatexParser.DERIVATIVE) | (1 << MatexParser.VARIABLE) | (1 << MatexParser.MIXNUMBER) | (1 << MatexParser.WORD) | (1 << MatexParser.INFINITY) | (1 << MatexParser.GREEKLETTER))) != 0):
                    self.state = 78
                    self.subtractionExpr(0)
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MatexParser.MUL:
                        self.state = 79
                        self.match(MatexParser.MUL)




                self.state = 84
                self.specialExpr()
                pass

            elif la_ == 2:
                self.state = 85
                self.implicitMultiplicationExpr(0)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MatexParser.MUL:
                    self.state = 86
                    self.match(MatexParser.MUL)


                self.state = 89
                self.specialExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 102
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 93
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 94
                        self.match(MatexParser.PLUS)
                        self.state = 95
                        self.specialExpr()
                        pass

                    elif la_ == 2:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 96
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 97
                        self.match(MatexParser.MINUS)
                        self.state = 98
                        self.specialExpr()
                        pass

                    elif la_ == 3:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 99
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 100
                        self.match(MatexParser.MUL)
                        self.state = 101
                        self.specialExpr()
                        pass

             
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class SpecialExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integralExpr(self):
            return self.getTypedRuleContext(MatexParser.IntegralExprContext,0)


        def summationExpr(self):
            return self.getTypedRuleContext(MatexParser.SummationExprContext,0)


        def productExpr(self):
            return self.getTypedRuleContext(MatexParser.ProductExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_specialExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecialExpr" ):
                listener.enterSpecialExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecialExpr" ):
                listener.exitSpecialExpr(self)




    def specialExpr(self):

        localctx = MatexParser.SpecialExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_specialExpr)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.FUNC_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.integralExpr()
                pass
            elif token in [MatexParser.FUNC_SUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.summationExpr()
                pass
            elif token in [MatexParser.FUNC_PROD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.productExpr()
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

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subtractionExpr(self):
            return self.getTypedRuleContext(MatexParser.SubtractionExprContext,0)


        def implicitMultiplicationExpr(self):
            return self.getTypedRuleContext(MatexParser.ImplicitMultiplicationExprContext,0)


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
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.subtractionExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.implicitMultiplicationExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.megaExpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntegralExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_INT(self):
            return self.getToken(MatexParser.FUNC_INT, 0)

        def subexpr(self):
            return self.getTypedRuleContext(MatexParser.SubexprContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(MatexParser.SupexprContext,0)


        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def DERIVATIVE(self):
            return self.getToken(MatexParser.DERIVATIVE, 0)

        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_integralExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegralExpr" ):
                listener.enterIntegralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegralExpr" ):
                listener.exitIntegralExpr(self)




    def integralExpr(self):

        localctx = MatexParser.IntegralExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_integralExpr)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(MatexParser.FUNC_INT)
                self.state = 118
                self.subexpr()
                self.state = 119
                self.supexpr()
                self.state = 120
                self.match(MatexParser.L_BRACE)
                self.state = 121
                self.expr()
                self.state = 122
                self.match(MatexParser.DERIVATIVE)
                self.state = 123
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(MatexParser.FUNC_INT)
                self.state = 126
                self.subexpr()
                self.state = 127
                self.supexpr()
                self.state = 128
                self.expr()
                self.state = 129
                self.match(MatexParser.DERIVATIVE)
                pass


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
        self.enterRule(localctx, 12, self.RULE_summationExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(MatexParser.FUNC_SUM)
            self.state = 134
            self.funcParams()
            self.state = 135
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
        self.enterRule(localctx, 14, self.RULE_productExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MatexParser.FUNC_PROD)
            self.state = 138
            self.funcParams()
            self.state = 139
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
        self.enterRule(localctx, 16, self.RULE_tailExpr)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS, MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_INT, MatexParser.FUNC_SUM, MatexParser.FUNC_PROD, MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_SQRT, MatexParser.CMD_FRAC, MatexParser.NUMBER, MatexParser.DERIVATIVE, MatexParser.VARIABLE, MatexParser.MIXNUMBER, MatexParser.WORD, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.expr()
                pass
            elif token in [MatexParser.L_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(MatexParser.L_BRACE)
                self.state = 143
                self.expr()
                self.state = 144
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
        self.enterRule(localctx, 18, self.RULE_funcParams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.subeq()
            self.state = 149
            self.supexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImplicitMultiplicationExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subtractionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatexParser.SubtractionExprContext)
            else:
                return self.getTypedRuleContext(MatexParser.SubtractionExprContext,i)


        def implicitMultiplicationExpr(self):
            return self.getTypedRuleContext(MatexParser.ImplicitMultiplicationExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_implicitMultiplicationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicitMultiplicationExpr" ):
                listener.enterImplicitMultiplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicitMultiplicationExpr" ):
                listener.exitImplicitMultiplicationExpr(self)



    def implicitMultiplicationExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatexParser.ImplicitMultiplicationExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_implicitMultiplicationExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.subtractionExpr(0)
            self.state = 153
            self.subtractionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.ImplicitMultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_implicitMultiplicationExpr)
                    self.state = 155
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 156
                    self.subtractionExpr(0) 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_subtractionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.additionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.SubtractionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_subtractionExpr)
                    self.state = 165
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 166
                    self.match(MatexParser.MINUS)
                    self.state = 167
                    self.additionExpr(0) 
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_additionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.divisionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.AdditionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additionExpr)
                    self.state = 176
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 177
                    self.match(MatexParser.PLUS)
                    self.state = 178
                    self.divisionExpr(0) 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_divisionExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.multiplicationExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.DivisionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_divisionExpr)
                    self.state = 187
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 188
                    _la = self._input.LA(1)
                    if not(_la==MatexParser.DIV or _la==MatexParser.CMD_DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 189
                    self.multiplicationExpr(0) 
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_multiplicationExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                    self.state = 198
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 199
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MUL) | (1 << MatexParser.CMD_TIMES) | (1 << MatexParser.CMD_CDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 200
                    self.powExpr() 
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_fracExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MatexParser.CMD_FRAC)
            self.state = 207
            self.match(MatexParser.L_BRACE)
            self.state = 208
            self.expr()
            self.state = 209
            self.match(MatexParser.R_BRACE)
            self.state = 210
            self.match(MatexParser.L_BRACE)
            self.state = 211
            self.expr()
            self.state = 212
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
        self.enterRule(localctx, 32, self.RULE_powExpr)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.signedAtom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.fracExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
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
        self.enterRule(localctx, 34, self.RULE_exponentiationExpr)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.signedAtom()
                self.state = 220
                self.match(MatexParser.CARET)
                self.state = 221
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.signedAtom()
                self.state = 224
                self.match(MatexParser.CARET)
                self.state = 225
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.signedAtom()
                self.state = 228
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
        self.enterRule(localctx, 36, self.RULE_signedAtom)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.negateAtom()
                pass
            elif token in [MatexParser.DERIVATIVE, MatexParser.MIXNUMBER, MatexParser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.localMultiplication()
                pass
            elif token in [MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_SQRT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.func()
                pass
            elif token in [MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.NUMBER, MatexParser.VARIABLE, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
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
        self.enterRule(localctx, 38, self.RULE_negateAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MatexParser.MINUS)
            self.state = 239
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

        def WORD(self):
            return self.getToken(MatexParser.WORD, 0)

        def DERIVATIVE(self):
            return self.getToken(MatexParser.DERIVATIVE, 0)

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
        self.enterRule(localctx, 40, self.RULE_localMultiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.DERIVATIVE) | (1 << MatexParser.MIXNUMBER) | (1 << MatexParser.WORD))) != 0)):
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


        def L_BRACKET(self):
            return self.getToken(MatexParser.L_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_BRACKET(self):
            return self.getToken(MatexParser.R_BRACKET, 0)

        def L_PAREN(self):
            return self.getToken(MatexParser.L_PAREN, 0)

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
        self.enterRule(localctx, 42, self.RULE_atom)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.indexedVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                self.absolute()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 248
                self.factorial()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 249
                self.match(MatexParser.L_BRACKET)
                self.state = 250
                self.expr()
                self.state = 251
                self.match(MatexParser.R_BRACKET)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 253
                self.match(MatexParser.L_PAREN)
                self.state = 254
                self.expr()
                self.state = 255
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
        self.enterRule(localctx, 44, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
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
        self.enterRule(localctx, 46, self.RULE_indexedVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MatexParser.VARIABLE)
            self.state = 262
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
        self.enterRule(localctx, 48, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
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
        self.enterRule(localctx, 50, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
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
        self.enterRule(localctx, 52, self.RULE_absolute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MatexParser.BAR)
            self.state = 269
            self.expr()
            self.state = 270
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
        self.enterRule(localctx, 54, self.RULE_factorial)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(MatexParser.L_PAREN)
                self.state = 273
                self.expr()
                self.state = 274
                self.match(MatexParser.R_PAREN)
                self.state = 275
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.number()
                self.state = 278
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.variable()
                self.state = 281
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
        self.enterRule(localctx, 56, self.RULE_func)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.funcname()
                self.state = 286
                self.match(MatexParser.L_BRACE)
                self.state = 287
                self.expr()
                self.state = 288
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.funcname()
                self.state = 291
                self.match(MatexParser.L_PAREN)
                self.state = 292
                self.expr()
                self.state = 293
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
        self.enterRule(localctx, 58, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
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
        self.enterRule(localctx, 60, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(MatexParser.UNDERSCORE)
            self.state = 300
            self.match(MatexParser.L_BRACE)
            self.state = 301
            self.expr()
            self.state = 302
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
        self.enterRule(localctx, 62, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(MatexParser.CARET)
            self.state = 305
            self.match(MatexParser.L_BRACE)
            self.state = 306
            self.expr()
            self.state = 307
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
        self.enterRule(localctx, 64, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(MatexParser.UNDERSCORE)
            self.state = 310
            self.match(MatexParser.L_BRACE)
            self.state = 311
            self.equality()
            self.state = 312
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
        self.enterRule(localctx, 66, self.RULE_supeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(MatexParser.CARET)
            self.state = 315
            self.match(MatexParser.L_BRACE)
            self.state = 316
            self.equality()
            self.state = 317
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
        self.enterRule(localctx, 68, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
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
        self._predicates[10] = self.implicitMultiplicationExpr_sempred
        self._predicates[11] = self.subtractionExpr_sempred
        self._predicates[12] = self.additionExpr_sempred
        self._predicates[13] = self.divisionExpr_sempred
        self._predicates[14] = self.multiplicationExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def megaExpr_sempred(self, localctx:MegaExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def implicitMultiplicationExpr_sempred(self, localctx:ImplicitMultiplicationExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def subtractionExpr_sempred(self, localctx:SubtractionExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def additionExpr_sempred(self, localctx:AdditionExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def divisionExpr_sempred(self, localctx:DivisionExprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def multiplicationExpr_sempred(self, localctx:MultiplicationExprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         




