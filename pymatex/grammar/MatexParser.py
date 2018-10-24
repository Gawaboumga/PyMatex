# Generated from .\pymatex\grammar\MatexParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0140\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\3\2\3\2\3\2\3\3\3\3\3\3\5\3S\n\3\5\3U\n\3\3\3\3\3\3")
        buf.write("\3\5\3Z\n\3\3\3\3\3\5\3^\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\7\3i\n\3\f\3\16\3l\13\3\3\4\3\4\3\4\5\4q\n")
        buf.write("\4\3\5\3\5\3\5\5\5v\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0086\n\6\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u0092\n\t\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\7\13\u009d\n\13\f\13\16\13")
        buf.write("\u00a0\13\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00a8\n\f\f\f")
        buf.write("\16\f\u00ab\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00b3\n\r")
        buf.write("\f\r\16\r\u00b6\13\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16")
        buf.write("\u00be\n\16\f\16\16\16\u00c1\13\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00c9\n\17\f\17\16\17\u00cc\13\17\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\5\21\u00d5\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u00e2\n\22\3\23\3\23\3\23\3\23\5\23\u00e8\n\23\3\24\3")
        buf.write("\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u00f7\n\26\3\27\3\27\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u010f\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u011f\n\35\3\36\3\36\3\37\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3&\3&\3&\2\b\4\24\26\30\32\34\'\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJ\2\b\4\2\6\6,,\4\2\5\5*+\4\2\63\63\65\66\4\2")
        buf.write("\64\64>>\3\2\25)\3\28<\2\u013f\2L\3\2\2\2\4]\3\2\2\2\6")
        buf.write("p\3\2\2\2\bu\3\2\2\2\n\u0085\3\2\2\2\f\u0087\3\2\2\2\16")
        buf.write("\u008b\3\2\2\2\20\u0091\3\2\2\2\22\u0093\3\2\2\2\24\u0096")
        buf.write("\3\2\2\2\26\u00a1\3\2\2\2\30\u00ac\3\2\2\2\32\u00b7\3")
        buf.write("\2\2\2\34\u00c2\3\2\2\2\36\u00cd\3\2\2\2 \u00d4\3\2\2")
        buf.write("\2\"\u00e1\3\2\2\2$\u00e7\3\2\2\2&\u00e9\3\2\2\2(\u00ec")
        buf.write("\3\2\2\2*\u00f6\3\2\2\2,\u00f8\3\2\2\2.\u00fa\3\2\2\2")
        buf.write("\60\u00fd\3\2\2\2\62\u00ff\3\2\2\2\64\u0101\3\2\2\2\66")
        buf.write("\u010e\3\2\2\28\u011e\3\2\2\2:\u0120\3\2\2\2<\u0122\3")
        buf.write("\2\2\2>\u0126\3\2\2\2@\u012a\3\2\2\2B\u012e\3\2\2\2D\u0131")
        buf.write("\3\2\2\2F\u0134\3\2\2\2H\u0139\3\2\2\2J\u013d\3\2\2\2")
        buf.write("LM\5\b\5\2MN\7\2\2\3N\3\3\2\2\2OT\b\3\1\2PR\5\26\f\2Q")
        buf.write("S\7\5\2\2RQ\3\2\2\2RS\3\2\2\2SU\3\2\2\2TP\3\2\2\2TU\3")
        buf.write("\2\2\2UV\3\2\2\2V^\5\6\4\2WY\5\24\13\2XZ\7\5\2\2YX\3\2")
        buf.write("\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\5\6\4\2\\^\3\2\2\2]O\3\2\2")
        buf.write("\2]W\3\2\2\2^j\3\2\2\2_`\f\5\2\2`a\7\3\2\2ai\5\6\4\2b")
        buf.write("c\f\4\2\2cd\7\4\2\2di\5\6\4\2ef\f\3\2\2fg\7\5\2\2gi\5")
        buf.write("\6\4\2h_\3\2\2\2hb\3\2\2\2he\3\2\2\2il\3\2\2\2jh\3\2\2")
        buf.write("\2jk\3\2\2\2k\5\3\2\2\2lj\3\2\2\2mq\5\n\6\2nq\5\f\7\2")
        buf.write("oq\5\16\b\2pm\3\2\2\2pn\3\2\2\2po\3\2\2\2q\7\3\2\2\2r")
        buf.write("v\5\26\f\2sv\5\24\13\2tv\5\4\3\2ur\3\2\2\2us\3\2\2\2u")
        buf.write("t\3\2\2\2v\t\3\2\2\2wx\7\22\2\2xy\5B\"\2yz\5D#\2z{\7\t")
        buf.write("\2\2{|\5\b\5\2|}\7\63\2\2}~\7\n\2\2~\u0086\3\2\2\2\177")
        buf.write("\u0080\7\22\2\2\u0080\u0081\5B\"\2\u0081\u0082\5D#\2\u0082")
        buf.write("\u0083\5\b\5\2\u0083\u0084\7\63\2\2\u0084\u0086\3\2\2")
        buf.write("\2\u0085w\3\2\2\2\u0085\177\3\2\2\2\u0086\13\3\2\2\2\u0087")
        buf.write("\u0088\7\23\2\2\u0088\u0089\5\22\n\2\u0089\u008a\5\20")
        buf.write("\t\2\u008a\r\3\2\2\2\u008b\u008c\7\24\2\2\u008c\u008d")
        buf.write("\5\22\n\2\u008d\u008e\5\20\t\2\u008e\17\3\2\2\2\u008f")
        buf.write("\u0092\5\b\5\2\u0090\u0092\5<\37\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0090\3\2\2\2\u0092\21\3\2\2\2\u0093\u0094\5F$")
        buf.write("\2\u0094\u0095\5D#\2\u0095\23\3\2\2\2\u0096\u0097\b\13")
        buf.write("\1\2\u0097\u0098\5\26\f\2\u0098\u0099\5\26\f\2\u0099\u009e")
        buf.write("\3\2\2\2\u009a\u009b\f\3\2\2\u009b\u009d\5\26\f\2\u009c")
        buf.write("\u009a\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\25\3\2\2\2\u00a0\u009e\3\2")
        buf.write("\2\2\u00a1\u00a2\b\f\1\2\u00a2\u00a3\5\30\r\2\u00a3\u00a9")
        buf.write("\3\2\2\2\u00a4\u00a5\f\3\2\2\u00a5\u00a6\7\4\2\2\u00a6")
        buf.write("\u00a8\5\30\r\2\u00a7\u00a4\3\2\2\2\u00a8\u00ab\3\2\2")
        buf.write("\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\27\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\b\r\1\2\u00ad\u00ae")
        buf.write("\5\32\16\2\u00ae\u00b4\3\2\2\2\u00af\u00b0\f\3\2\2\u00b0")
        buf.write("\u00b1\7\3\2\2\u00b1\u00b3\5\32\16\2\u00b2\u00af\3\2\2")
        buf.write("\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\31\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8")
        buf.write("\b\16\1\2\u00b8\u00b9\5\34\17\2\u00b9\u00bf\3\2\2\2\u00ba")
        buf.write("\u00bb\f\3\2\2\u00bb\u00bc\t\2\2\2\u00bc\u00be\5\34\17")
        buf.write("\2\u00bd\u00ba\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\33\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\u00c3\b\17\1\2\u00c3\u00c4\5 \21\2\u00c4")
        buf.write("\u00ca\3\2\2\2\u00c5\u00c6\f\3\2\2\u00c6\u00c7\t\3\2\2")
        buf.write("\u00c7\u00c9\5 \21\2\u00c8\u00c5\3\2\2\2\u00c9\u00cc\3")
        buf.write("\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\35")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\7-\2\2\u00ce")
        buf.write("\u00cf\5<\37\2\u00cf\u00d0\5<\37\2\u00d0\37\3\2\2\2\u00d1")
        buf.write("\u00d5\5$\23\2\u00d2\u00d5\5\36\20\2\u00d3\u00d5\5\"\22")
        buf.write("\2\u00d4\u00d1\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d5!\3\2\2\2\u00d6\u00d7\5$\23\2\u00d7\u00d8")
        buf.write("\7/\2\2\u00d8\u00d9\5\62\32\2\u00d9\u00e2\3\2\2\2\u00da")
        buf.write("\u00db\5$\23\2\u00db\u00dc\7/\2\2\u00dc\u00dd\5,\27\2")
        buf.write("\u00dd\u00e2\3\2\2\2\u00de\u00df\5$\23\2\u00df\u00e0\5")
        buf.write("D#\2\u00e0\u00e2\3\2\2\2\u00e1\u00d6\3\2\2\2\u00e1\u00da")
        buf.write("\3\2\2\2\u00e1\u00de\3\2\2\2\u00e2#\3\2\2\2\u00e3\u00e8")
        buf.write("\5&\24\2\u00e4\u00e8\5(\25\2\u00e5\u00e8\58\35\2\u00e6")
        buf.write("\u00e8\5*\26\2\u00e7\u00e3\3\2\2\2\u00e7\u00e4\3\2\2\2")
        buf.write("\u00e7\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8%\3\2\2")
        buf.write("\2\u00e9\u00ea\7\4\2\2\u00ea\u00eb\5$\23\2\u00eb\'\3\2")
        buf.write("\2\2\u00ec\u00ed\t\4\2\2\u00ed)\3\2\2\2\u00ee\u00f7\5")
        buf.write(",\27\2\u00ef\u00f7\5.\30\2\u00f0\u00f7\5\60\31\2\u00f1")
        buf.write("\u00f7\5\62\32\2\u00f2\u00f7\5\64\33\2\u00f3\u00f7\5\66")
        buf.write("\34\2\u00f4\u00f7\5> \2\u00f5\u00f7\5@!\2\u00f6\u00ee")
        buf.write("\3\2\2\2\u00f6\u00ef\3\2\2\2\u00f6\u00f0\3\2\2\2\u00f6")
        buf.write("\u00f1\3\2\2\2\u00f6\u00f2\3\2\2\2\u00f6\u00f3\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7+\3\2\2")
        buf.write("\2\u00f8\u00f9\t\5\2\2\u00f9-\3\2\2\2\u00fa\u00fb\7\64")
        buf.write("\2\2\u00fb\u00fc\5B\"\2\u00fc/\3\2\2\2\u00fd\u00fe\7\67")
        buf.write("\2\2\u00fe\61\3\2\2\2\u00ff\u0100\7\62\2\2\u0100\63\3")
        buf.write("\2\2\2\u0101\u0102\7\17\2\2\u0102\u0103\5\b\5\2\u0103")
        buf.write("\u0104\7\17\2\2\u0104\65\3\2\2\2\u0105\u0106\5@!\2\u0106")
        buf.write("\u0107\7=\2\2\u0107\u010f\3\2\2\2\u0108\u0109\5\62\32")
        buf.write("\2\u0109\u010a\7=\2\2\u010a\u010f\3\2\2\2\u010b\u010c")
        buf.write("\5,\27\2\u010c\u010d\7=\2\2\u010d\u010f\3\2\2\2\u010e")
        buf.write("\u0105\3\2\2\2\u010e\u0108\3\2\2\2\u010e\u010b\3\2\2\2")
        buf.write("\u010f\67\3\2\2\2\u0110\u0111\5:\36\2\u0111\u0112\5<\37")
        buf.write("\2\u0112\u011f\3\2\2\2\u0113\u0114\5:\36\2\u0114\u0115")
        buf.write("\5@!\2\u0115\u011f\3\2\2\2\u0116\u0117\7?\2\2\u0117\u0118")
        buf.write("\5\b\5\2\u0118\u0119\7\n\2\2\u0119\u011f\3\2\2\2\u011a")
        buf.write("\u011b\7@\2\2\u011b\u011c\5\b\5\2\u011c\u011d\7\b\2\2")
        buf.write("\u011d\u011f\3\2\2\2\u011e\u0110\3\2\2\2\u011e\u0113\3")
        buf.write("\2\2\2\u011e\u0116\3\2\2\2\u011e\u011a\3\2\2\2\u011f9")
        buf.write("\3\2\2\2\u0120\u0121\t\6\2\2\u0121;\3\2\2\2\u0122\u0123")
        buf.write("\7\t\2\2\u0123\u0124\5\b\5\2\u0124\u0125\7\n\2\2\u0125")
        buf.write("=\3\2\2\2\u0126\u0127\7\13\2\2\u0127\u0128\5\b\5\2\u0128")
        buf.write("\u0129\7\f\2\2\u0129?\3\2\2\2\u012a\u012b\7\7\2\2\u012b")
        buf.write("\u012c\5\b\5\2\u012c\u012d\7\b\2\2\u012dA\3\2\2\2\u012e")
        buf.write("\u012f\7.\2\2\u012f\u0130\5<\37\2\u0130C\3\2\2\2\u0131")
        buf.write("\u0132\7/\2\2\u0132\u0133\5<\37\2\u0133E\3\2\2\2\u0134")
        buf.write("\u0135\7.\2\2\u0135\u0136\7\t\2\2\u0136\u0137\5H%\2\u0137")
        buf.write("\u0138\7\n\2\2\u0138G\3\2\2\2\u0139\u013a\5,\27\2\u013a")
        buf.write("\u013b\78\2\2\u013b\u013c\5\b\5\2\u013cI\3\2\2\2\u013d")
        buf.write("\u013e\t\7\2\2\u013eK\3\2\2\2\27RTY]hjpu\u0085\u0091\u009e")
        buf.write("\u00a9\u00b4\u00bf\u00ca\u00d4\u00e1\u00e7\u00f6\u010e")
        buf.write("\u011e")
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
                      "BANG", "GREEKLETTER", "GREEKFUNCTIONBRACE", "GREEKFUNCTIONPAREN", 
                      "WS" ]

    RULE_math = 0
    RULE_megaExpr = 1
    RULE_specialExpr = 2
    RULE_expr = 3
    RULE_integralExpr = 4
    RULE_summationExpr = 5
    RULE_productExpr = 6
    RULE_tailExpr = 7
    RULE_funcParams = 8
    RULE_implicitMultiplicationExpr = 9
    RULE_subtractionExpr = 10
    RULE_additionExpr = 11
    RULE_divisionExpr = 12
    RULE_multiplicationExpr = 13
    RULE_fracExpr = 14
    RULE_powExpr = 15
    RULE_exponentiationExpr = 16
    RULE_signedAtom = 17
    RULE_negateAtom = 18
    RULE_localMultiplication = 19
    RULE_atom = 20
    RULE_variable = 21
    RULE_indexedVariable = 22
    RULE_constant = 23
    RULE_number = 24
    RULE_absolute = 25
    RULE_factorial = 26
    RULE_func = 27
    RULE_funcname = 28
    RULE_bracedExpr = 29
    RULE_brackExpr = 30
    RULE_parenExpr = 31
    RULE_subexpr = 32
    RULE_supexpr = 33
    RULE_subeq = 34
    RULE_equality = 35
    RULE_relop = 36

    ruleNames =  [ "math", "megaExpr", "specialExpr", "expr", "integralExpr", 
                   "summationExpr", "productExpr", "tailExpr", "funcParams", 
                   "implicitMultiplicationExpr", "subtractionExpr", "additionExpr", 
                   "divisionExpr", "multiplicationExpr", "fracExpr", "powExpr", 
                   "exponentiationExpr", "signedAtom", "negateAtom", "localMultiplication", 
                   "atom", "variable", "indexedVariable", "constant", "number", 
                   "absolute", "factorial", "func", "funcname", "bracedExpr", 
                   "brackExpr", "parenExpr", "subexpr", "supexpr", "subeq", 
                   "equality", "relop" ]

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
    GREEKFUNCTIONBRACE=61
    GREEKFUNCTIONPAREN=62
    WS=63

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
            self.state = 74
            self.expr()
            self.state = 75
            self.match(MatexParser.EOF)
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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_megaExpr, _p)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MINUS) | (1 << MatexParser.L_PAREN) | (1 << MatexParser.L_BRACKET) | (1 << MatexParser.BAR) | (1 << MatexParser.FUNC_LOG) | (1 << MatexParser.FUNC_LN) | (1 << MatexParser.FUNC_SIN) | (1 << MatexParser.FUNC_COS) | (1 << MatexParser.FUNC_TAN) | (1 << MatexParser.FUNC_CSC) | (1 << MatexParser.FUNC_SEC) | (1 << MatexParser.FUNC_COT) | (1 << MatexParser.FUNC_ARCSIN) | (1 << MatexParser.FUNC_ARCCOS) | (1 << MatexParser.FUNC_ARCTAN) | (1 << MatexParser.FUNC_ARCCSC) | (1 << MatexParser.FUNC_ARCSEC) | (1 << MatexParser.FUNC_ARCCOT) | (1 << MatexParser.FUNC_SINH) | (1 << MatexParser.FUNC_COSH) | (1 << MatexParser.FUNC_TANH) | (1 << MatexParser.FUNC_ARCSINH) | (1 << MatexParser.FUNC_ARCCOSH) | (1 << MatexParser.FUNC_ARCTANH) | (1 << MatexParser.FUNC_SQRT) | (1 << MatexParser.CMD_FRAC) | (1 << MatexParser.NUMBER) | (1 << MatexParser.DERIVATIVE) | (1 << MatexParser.VARIABLE) | (1 << MatexParser.MIXNUMBER) | (1 << MatexParser.WORD) | (1 << MatexParser.INFINITY) | (1 << MatexParser.GREEKLETTER) | (1 << MatexParser.GREEKFUNCTIONBRACE) | (1 << MatexParser.GREEKFUNCTIONPAREN))) != 0):
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
        self.enterRule(localctx, 4, self.RULE_specialExpr)
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
        self.enterRule(localctx, 6, self.RULE_expr)
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
        self.enterRule(localctx, 8, self.RULE_integralExpr)
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
        self.enterRule(localctx, 10, self.RULE_summationExpr)
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
        self.enterRule(localctx, 12, self.RULE_productExpr)
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


        def bracedExpr(self):
            return self.getTypedRuleContext(MatexParser.BracedExprContext,0)


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
        self.enterRule(localctx, 14, self.RULE_tailExpr)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS, MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_INT, MatexParser.FUNC_SUM, MatexParser.FUNC_PROD, MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_SQRT, MatexParser.CMD_FRAC, MatexParser.NUMBER, MatexParser.DERIVATIVE, MatexParser.VARIABLE, MatexParser.MIXNUMBER, MatexParser.WORD, MatexParser.INFINITY, MatexParser.GREEKLETTER, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.expr()
                pass
            elif token in [MatexParser.L_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.bracedExpr()
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
        self.enterRule(localctx, 16, self.RULE_funcParams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.subeq()
            self.state = 146
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_implicitMultiplicationExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.subtractionExpr(0)
            self.state = 150
            self.subtractionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.ImplicitMultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_implicitMultiplicationExpr)
                    self.state = 152
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 153
                    self.subtractionExpr(0) 
                self.state = 158
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_subtractionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.additionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.SubtractionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_subtractionExpr)
                    self.state = 162
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 163
                    self.match(MatexParser.MINUS)
                    self.state = 164
                    self.additionExpr(0) 
                self.state = 169
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_additionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.divisionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.AdditionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additionExpr)
                    self.state = 173
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 174
                    self.match(MatexParser.PLUS)
                    self.state = 175
                    self.divisionExpr(0) 
                self.state = 180
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_divisionExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.multiplicationExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.DivisionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_divisionExpr)
                    self.state = 184
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 185
                    _la = self._input.LA(1)
                    if not(_la==MatexParser.DIV or _la==MatexParser.CMD_DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 186
                    self.multiplicationExpr(0) 
                self.state = 191
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_multiplicationExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                    self.state = 195
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 196
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MUL) | (1 << MatexParser.CMD_TIMES) | (1 << MatexParser.CMD_CDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 197
                    self.powExpr() 
                self.state = 202
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

        def bracedExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatexParser.BracedExprContext)
            else:
                return self.getTypedRuleContext(MatexParser.BracedExprContext,i)


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
        self.enterRule(localctx, 28, self.RULE_fracExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(MatexParser.CMD_FRAC)
            self.state = 204
            self.bracedExpr()
            self.state = 205
            self.bracedExpr()
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
        self.enterRule(localctx, 30, self.RULE_powExpr)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.signedAtom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.fracExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
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
        self.enterRule(localctx, 32, self.RULE_exponentiationExpr)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.signedAtom()
                self.state = 213
                self.match(MatexParser.CARET)
                self.state = 214
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.signedAtom()
                self.state = 217
                self.match(MatexParser.CARET)
                self.state = 218
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.signedAtom()
                self.state = 221
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
        self.enterRule(localctx, 34, self.RULE_signedAtom)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.negateAtom()
                pass
            elif token in [MatexParser.DERIVATIVE, MatexParser.MIXNUMBER, MatexParser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.localMultiplication()
                pass
            elif token in [MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_SQRT, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.func()
                pass
            elif token in [MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.NUMBER, MatexParser.VARIABLE, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
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
        self.enterRule(localctx, 36, self.RULE_negateAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MatexParser.MINUS)
            self.state = 232
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
        self.enterRule(localctx, 38, self.RULE_localMultiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
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


        def brackExpr(self):
            return self.getTypedRuleContext(MatexParser.BrackExprContext,0)


        def parenExpr(self):
            return self.getTypedRuleContext(MatexParser.ParenExprContext,0)


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
        self.enterRule(localctx, 40, self.RULE_atom)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.indexedVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.absolute()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 241
                self.factorial()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 242
                self.brackExpr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 243
                self.parenExpr()
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
        self.enterRule(localctx, 42, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
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
        self.enterRule(localctx, 44, self.RULE_indexedVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MatexParser.VARIABLE)
            self.state = 249
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
        self.enterRule(localctx, 46, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
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
        self.enterRule(localctx, 48, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
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
        self.enterRule(localctx, 50, self.RULE_absolute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(MatexParser.BAR)
            self.state = 256
            self.expr()
            self.state = 257
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

        def parenExpr(self):
            return self.getTypedRuleContext(MatexParser.ParenExprContext,0)


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
        self.enterRule(localctx, 52, self.RULE_factorial)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.parenExpr()
                self.state = 260
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.number()
                self.state = 263
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.variable()
                self.state = 266
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


        def bracedExpr(self):
            return self.getTypedRuleContext(MatexParser.BracedExprContext,0)


        def parenExpr(self):
            return self.getTypedRuleContext(MatexParser.ParenExprContext,0)


        def GREEKFUNCTIONBRACE(self):
            return self.getToken(MatexParser.GREEKFUNCTIONBRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def GREEKFUNCTIONPAREN(self):
            return self.getToken(MatexParser.GREEKFUNCTIONPAREN, 0)

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
        self.enterRule(localctx, 54, self.RULE_func)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.funcname()
                self.state = 271
                self.bracedExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.funcname()
                self.state = 274
                self.parenExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.match(MatexParser.GREEKFUNCTIONBRACE)
                self.state = 277
                self.expr()
                self.state = 278
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.match(MatexParser.GREEKFUNCTIONPAREN)
                self.state = 281
                self.expr()
                self.state = 282
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
        self.enterRule(localctx, 56, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
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

    class BracedExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_bracedExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracedExpr" ):
                listener.enterBracedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracedExpr" ):
                listener.exitBracedExpr(self)




    def bracedExpr(self):

        localctx = MatexParser.BracedExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_bracedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(MatexParser.L_BRACE)
            self.state = 289
            self.expr()
            self.state = 290
            self.match(MatexParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BrackExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MatexParser.L_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_BRACKET(self):
            return self.getToken(MatexParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_brackExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackExpr" ):
                listener.enterBrackExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackExpr" ):
                listener.exitBrackExpr(self)




    def brackExpr(self):

        localctx = MatexParser.BrackExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_brackExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(MatexParser.L_BRACKET)
            self.state = 293
            self.expr()
            self.state = 294
            self.match(MatexParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParenExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MatexParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(MatexParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_parenExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)




    def parenExpr(self):

        localctx = MatexParser.ParenExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_parenExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(MatexParser.L_PAREN)
            self.state = 297
            self.expr()
            self.state = 298
            self.match(MatexParser.R_PAREN)
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

        def bracedExpr(self):
            return self.getTypedRuleContext(MatexParser.BracedExprContext,0)


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
        self.enterRule(localctx, 64, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(MatexParser.UNDERSCORE)
            self.state = 301
            self.bracedExpr()
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

        def bracedExpr(self):
            return self.getTypedRuleContext(MatexParser.BracedExprContext,0)


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
        self.enterRule(localctx, 66, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MatexParser.CARET)
            self.state = 304
            self.bracedExpr()
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
        self.enterRule(localctx, 68, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MatexParser.UNDERSCORE)
            self.state = 307
            self.match(MatexParser.L_BRACE)
            self.state = 308
            self.equality()
            self.state = 309
            self.match(MatexParser.R_BRACE)
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

        def variable(self):
            return self.getTypedRuleContext(MatexParser.VariableContext,0)


        def EQ(self):
            return self.getToken(MatexParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


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
        self.enterRule(localctx, 70, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.variable()
            self.state = 312
            self.match(MatexParser.EQ)
            self.state = 313
            self.expr()
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
        self.enterRule(localctx, 72, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
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
        self._predicates[1] = self.megaExpr_sempred
        self._predicates[9] = self.implicitMultiplicationExpr_sempred
        self._predicates[10] = self.subtractionExpr_sempred
        self._predicates[11] = self.additionExpr_sempred
        self._predicates[12] = self.divisionExpr_sempred
        self._predicates[13] = self.multiplicationExpr_sempred
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
         




