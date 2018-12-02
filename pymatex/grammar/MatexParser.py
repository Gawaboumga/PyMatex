# Generated from .\pymatex\grammar\MatexParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u0167\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\5\3]\n\3\5\3_\n\3\3\3\3\3\3\3\5\3d\n\3\3\3\3\3\5")
        buf.write("\3h\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3s\n\3\f")
        buf.write("\3\16\3v\13\3\3\4\3\4\3\4\5\4{\n\4\3\5\3\5\3\5\5\5\u0080")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6\u0090\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\5\t\u009c\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\7\13\u00a7\n\13\f\13\16\13\u00aa\13\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\7\f\u00b2\n\f\f\f\16\f\u00b5\13\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\7\r\u00bd\n\r\f\r\16\r\u00c0\13")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00c8\n\16\f\16")
        buf.write("\16\16\u00cb\13\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17")
        buf.write("\u00d3\n\17\f\17\16\17\u00d6\13\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\5\21\u00df\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ec\n\22\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00f2\n\23\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u0103\n\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u011f\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0133\n")
        buf.write("\37\3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("#\7#\u0145\n#\f#\16#\u0148\13#\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\2\t\4\24\26\30\32\34D,\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRT\2\b\4\2\6\6\66\66\4\2\5\5\64\65\4\299;<\4\2::")
        buf.write("DD\3\2\30\62\3\2>B\2\u0164\2V\3\2\2\2\4g\3\2\2\2\6z\3")
        buf.write("\2\2\2\b\177\3\2\2\2\n\u008f\3\2\2\2\f\u0091\3\2\2\2\16")
        buf.write("\u0095\3\2\2\2\20\u009b\3\2\2\2\22\u009d\3\2\2\2\24\u00a0")
        buf.write("\3\2\2\2\26\u00ab\3\2\2\2\30\u00b6\3\2\2\2\32\u00c1\3")
        buf.write("\2\2\2\34\u00cc\3\2\2\2\36\u00d7\3\2\2\2 \u00de\3\2\2")
        buf.write("\2\"\u00eb\3\2\2\2$\u00f1\3\2\2\2&\u00f3\3\2\2\2(\u00f6")
        buf.write("\3\2\2\2*\u0102\3\2\2\2,\u0104\3\2\2\2.\u0106\3\2\2\2")
        buf.write("\60\u0109\3\2\2\2\62\u010b\3\2\2\2\64\u010d\3\2\2\2\66")
        buf.write("\u0111\3\2\2\28\u011e\3\2\2\2:\u0120\3\2\2\2<\u0132\3")
        buf.write("\2\2\2>\u0134\3\2\2\2@\u0136\3\2\2\2B\u013a\3\2\2\2D\u013e")
        buf.write("\3\2\2\2F\u0149\3\2\2\2H\u014d\3\2\2\2J\u0151\3\2\2\2")
        buf.write("L\u0155\3\2\2\2N\u0158\3\2\2\2P\u015b\3\2\2\2R\u0160\3")
        buf.write("\2\2\2T\u0164\3\2\2\2VW\5\b\5\2WX\7\2\2\3X\3\3\2\2\2Y")
        buf.write("^\b\3\1\2Z\\\5\26\f\2[]\7\5\2\2\\[\3\2\2\2\\]\3\2\2\2")
        buf.write("]_\3\2\2\2^Z\3\2\2\2^_\3\2\2\2_`\3\2\2\2`h\5\6\4\2ac\5")
        buf.write("\24\13\2bd\7\5\2\2cb\3\2\2\2cd\3\2\2\2de\3\2\2\2ef\5\6")
        buf.write("\4\2fh\3\2\2\2gY\3\2\2\2ga\3\2\2\2ht\3\2\2\2ij\f\5\2\2")
        buf.write("jk\7\3\2\2ks\5\6\4\2lm\f\4\2\2mn\7\4\2\2ns\5\6\4\2op\f")
        buf.write("\3\2\2pq\7\5\2\2qs\5\6\4\2ri\3\2\2\2rl\3\2\2\2ro\3\2\2")
        buf.write("\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\5\3\2\2\2vt\3\2\2\2")
        buf.write("w{\5\n\6\2x{\5\f\7\2y{\5\16\b\2zw\3\2\2\2zx\3\2\2\2zy")
        buf.write("\3\2\2\2{\7\3\2\2\2|\u0080\5\26\f\2}\u0080\5\24\13\2~")
        buf.write("\u0080\5\4\3\2\177|\3\2\2\2\177}\3\2\2\2\177~\3\2\2\2")
        buf.write("\u0080\t\3\2\2\2\u0081\u0082\7\25\2\2\u0082\u0083\5L\'")
        buf.write("\2\u0083\u0084\5N(\2\u0084\u0085\7\t\2\2\u0085\u0086\5")
        buf.write("\b\5\2\u0086\u0087\79\2\2\u0087\u0088\7\n\2\2\u0088\u0090")
        buf.write("\3\2\2\2\u0089\u008a\7\25\2\2\u008a\u008b\5L\'\2\u008b")
        buf.write("\u008c\5N(\2\u008c\u008d\5\b\5\2\u008d\u008e\79\2\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f\u0081\3\2\2\2\u008f\u0089\3\2\2\2")
        buf.write("\u0090\13\3\2\2\2\u0091\u0092\7\26\2\2\u0092\u0093\5\22")
        buf.write("\n\2\u0093\u0094\5\20\t\2\u0094\r\3\2\2\2\u0095\u0096")
        buf.write("\7\27\2\2\u0096\u0097\5\22\n\2\u0097\u0098\5\20\t\2\u0098")
        buf.write("\17\3\2\2\2\u0099\u009c\5\b\5\2\u009a\u009c\5F$\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c\21\3\2\2\2\u009d")
        buf.write("\u009e\5P)\2\u009e\u009f\5N(\2\u009f\23\3\2\2\2\u00a0")
        buf.write("\u00a1\b\13\1\2\u00a1\u00a2\5\26\f\2\u00a2\u00a3\5\26")
        buf.write("\f\2\u00a3\u00a8\3\2\2\2\u00a4\u00a5\f\3\2\2\u00a5\u00a7")
        buf.write("\5\26\f\2\u00a6\u00a4\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\25\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00ab\u00ac\b\f\1\2\u00ac\u00ad\5\30\r")
        buf.write("\2\u00ad\u00b3\3\2\2\2\u00ae\u00af\f\3\2\2\u00af\u00b0")
        buf.write("\7\4\2\2\u00b0\u00b2\5\30\r\2\u00b1\u00ae\3\2\2\2\u00b2")
        buf.write("\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\27\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\b\r")
        buf.write("\1\2\u00b7\u00b8\5\32\16\2\u00b8\u00be\3\2\2\2\u00b9\u00ba")
        buf.write("\f\3\2\2\u00ba\u00bb\7\3\2\2\u00bb\u00bd\5\32\16\2\u00bc")
        buf.write("\u00b9\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\31\3\2\2\2\u00c0\u00be\3\2")
        buf.write("\2\2\u00c1\u00c2\b\16\1\2\u00c2\u00c3\5\34\17\2\u00c3")
        buf.write("\u00c9\3\2\2\2\u00c4\u00c5\f\3\2\2\u00c5\u00c6\t\2\2\2")
        buf.write("\u00c6\u00c8\5\34\17\2\u00c7\u00c4\3\2\2\2\u00c8\u00cb")
        buf.write("\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\33\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\b\17\1\2\u00cd")
        buf.write("\u00ce\5 \21\2\u00ce\u00d4\3\2\2\2\u00cf\u00d0\f\3\2\2")
        buf.write("\u00d0\u00d1\t\3\2\2\u00d1\u00d3\5 \21\2\u00d2\u00cf\3")
        buf.write("\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\35\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8")
        buf.write("\7\67\2\2\u00d8\u00d9\5F$\2\u00d9\u00da\5F$\2\u00da\37")
        buf.write("\3\2\2\2\u00db\u00df\5$\23\2\u00dc\u00df\5\36\20\2\u00dd")
        buf.write("\u00df\5\"\22\2\u00de\u00db\3\2\2\2\u00de\u00dc\3\2\2")
        buf.write("\2\u00de\u00dd\3\2\2\2\u00df!\3\2\2\2\u00e0\u00e1\5$\23")
        buf.write("\2\u00e1\u00e2\7\21\2\2\u00e2\u00e3\5\62\32\2\u00e3\u00ec")
        buf.write("\3\2\2\2\u00e4\u00e5\5$\23\2\u00e5\u00e6\7\21\2\2\u00e6")
        buf.write("\u00e7\5,\27\2\u00e7\u00ec\3\2\2\2\u00e8\u00e9\5$\23\2")
        buf.write("\u00e9\u00ea\5N(\2\u00ea\u00ec\3\2\2\2\u00eb\u00e0\3\2")
        buf.write("\2\2\u00eb\u00e4\3\2\2\2\u00eb\u00e8\3\2\2\2\u00ec#\3")
        buf.write("\2\2\2\u00ed\u00f2\5&\24\2\u00ee\u00f2\5(\25\2\u00ef\u00f2")
        buf.write("\5<\37\2\u00f0\u00f2\5*\26\2\u00f1\u00ed\3\2\2\2\u00f1")
        buf.write("\u00ee\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2")
        buf.write("\u00f2%\3\2\2\2\u00f3\u00f4\7\4\2\2\u00f4\u00f5\5$\23")
        buf.write("\2\u00f5\'\3\2\2\2\u00f6\u00f7\t\4\2\2\u00f7)\3\2\2\2")
        buf.write("\u00f8\u0103\5,\27\2\u00f9\u0103\5.\30\2\u00fa\u0103\5")
        buf.write("\60\31\2\u00fb\u0103\5\62\32\2\u00fc\u0103\5\64\33\2\u00fd")
        buf.write("\u0103\5\66\34\2\u00fe\u0103\58\35\2\u00ff\u0103\5:\36")
        buf.write("\2\u0100\u0103\5H%\2\u0101\u0103\5J&\2\u0102\u00f8\3\2")
        buf.write("\2\2\u0102\u00f9\3\2\2\2\u0102\u00fa\3\2\2\2\u0102\u00fb")
        buf.write("\3\2\2\2\u0102\u00fc\3\2\2\2\u0102\u00fd\3\2\2\2\u0102")
        buf.write("\u00fe\3\2\2\2\u0102\u00ff\3\2\2\2\u0102\u0100\3\2\2\2")
        buf.write("\u0102\u0101\3\2\2\2\u0103+\3\2\2\2\u0104\u0105\t\5\2")
        buf.write("\2\u0105-\3\2\2\2\u0106\u0107\7:\2\2\u0107\u0108\5L\'")
        buf.write("\2\u0108/\3\2\2\2\u0109\u010a\7=\2\2\u010a\61\3\2\2\2")
        buf.write("\u010b\u010c\78\2\2\u010c\63\3\2\2\2\u010d\u010e\7\17")
        buf.write("\2\2\u010e\u010f\5\b\5\2\u010f\u0110\7\17\2\2\u0110\65")
        buf.write("\3\2\2\2\u0111\u0112\7:\2\2\u0112\u0113\7\17\2\2\u0113")
        buf.write("\u0114\7:\2\2\u0114\67\3\2\2\2\u0115\u0116\5J&\2\u0116")
        buf.write("\u0117\7C\2\2\u0117\u011f\3\2\2\2\u0118\u0119\5\62\32")
        buf.write("\2\u0119\u011a\7C\2\2\u011a\u011f\3\2\2\2\u011b\u011c")
        buf.write("\5,\27\2\u011c\u011d\7C\2\2\u011d\u011f\3\2\2\2\u011e")
        buf.write("\u0115\3\2\2\2\u011e\u0118\3\2\2\2\u011e\u011b\3\2\2\2")
        buf.write("\u011f9\3\2\2\2\u0120\u0121\7\63\2\2\u0121\u0122\5F$\2")
        buf.write("\u0122\u0123\5F$\2\u0123;\3\2\2\2\u0124\u0125\5> \2\u0125")
        buf.write("\u0126\5@!\2\u0126\u0133\3\2\2\2\u0127\u0128\5> \2\u0128")
        buf.write("\u0129\5B\"\2\u0129\u0133\3\2\2\2\u012a\u012b\7E\2\2\u012b")
        buf.write("\u012c\5D#\2\u012c\u012d\7\n\2\2\u012d\u0133\3\2\2\2\u012e")
        buf.write("\u012f\7F\2\2\u012f\u0130\5D#\2\u0130\u0131\7\b\2\2\u0131")
        buf.write("\u0133\3\2\2\2\u0132\u0124\3\2\2\2\u0132\u0127\3\2\2\2")
        buf.write("\u0132\u012a\3\2\2\2\u0132\u012e\3\2\2\2\u0133=\3\2\2")
        buf.write("\2\u0134\u0135\t\6\2\2\u0135?\3\2\2\2\u0136\u0137\7\t")
        buf.write("\2\2\u0137\u0138\5D#\2\u0138\u0139\7\n\2\2\u0139A\3\2")
        buf.write("\2\2\u013a\u013b\7\7\2\2\u013b\u013c\5D#\2\u013c\u013d")
        buf.write("\7\b\2\2\u013dC\3\2\2\2\u013e\u013f\b#\1\2\u013f\u0140")
        buf.write("\5\b\5\2\u0140\u0146\3\2\2\2\u0141\u0142\f\3\2\2\u0142")
        buf.write("\u0143\7\r\2\2\u0143\u0145\5\b\5\2\u0144\u0141\3\2\2\2")
        buf.write("\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3")
        buf.write("\2\2\2\u0147E\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a")
        buf.write("\7\t\2\2\u014a\u014b\5\b\5\2\u014b\u014c\7\n\2\2\u014c")
        buf.write("G\3\2\2\2\u014d\u014e\7\13\2\2\u014e\u014f\5\b\5\2\u014f")
        buf.write("\u0150\7\f\2\2\u0150I\3\2\2\2\u0151\u0152\7\7\2\2\u0152")
        buf.write("\u0153\5\b\5\2\u0153\u0154\7\b\2\2\u0154K\3\2\2\2\u0155")
        buf.write("\u0156\7\20\2\2\u0156\u0157\5F$\2\u0157M\3\2\2\2\u0158")
        buf.write("\u0159\7\21\2\2\u0159\u015a\5F$\2\u015aO\3\2\2\2\u015b")
        buf.write("\u015c\7\20\2\2\u015c\u015d\7\t\2\2\u015d\u015e\5R*\2")
        buf.write("\u015e\u015f\7\n\2\2\u015fQ\3\2\2\2\u0160\u0161\5,\27")
        buf.write("\2\u0161\u0162\7>\2\2\u0162\u0163\5\b\5\2\u0163S\3\2\2")
        buf.write("\2\u0164\u0165\t\7\2\2\u0165U\3\2\2\2\30\\^cgrtz\177\u008f")
        buf.write("\u009b\u00a8\u00b3\u00be\u00c9\u00d4\u00de\u00eb\u00f1")
        buf.write("\u0102\u011e\u0132\u0146")
        return buf.getvalue()


class MatexParser ( Parser ):

    grammarFileName = "MatexParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "'.'", "'|'", "'_'", 
                     "'^'", "':'", "'\\lim'", "<INVALID>", "'\\int'", "'\\sum'", 
                     "'\\prod'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\times'", "'\\cdot'", "'\\div'", "'\\frac'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\infty'", "'='", "'<'", "'\\leq'", 
                     "'>'", "'\\geq'", "'!'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "L_PAREN", 
                      "R_PAREN", "L_BRACE", "R_BRACE", "L_BRACKET", "R_BRACKET", 
                      "COMMA", "DOT", "BAR", "UNDERSCORE", "CARET", "COLON", 
                      "FUNC_LIM", "LIM_APPROACH_SYM", "FUNC_INT", "FUNC_SUM", 
                      "FUNC_PROD", "FUNC_LOG", "FUNC_LN", "FUNC_SIN", "FUNC_COS", 
                      "FUNC_TAN", "FUNC_CSC", "FUNC_SEC", "FUNC_COT", "FUNC_ARCSIN", 
                      "FUNC_ARCCOS", "FUNC_ARCTAN", "FUNC_ARCCSC", "FUNC_ARCSEC", 
                      "FUNC_ARCCOT", "FUNC_SINH", "FUNC_COSH", "FUNC_TANH", 
                      "FUNC_ARCSINH", "FUNC_ARCCOSH", "FUNC_ARCTANH", "FUNC_ECOS", 
                      "FUNC_ESIN", "FUNC_EDELTAAMPLITUDE", "FUNC_ARCECOS", 
                      "FUNC_ARCESIN", "FUNC_ARCEDELTAAMPLITUDE", "FUNC_SQRT", 
                      "FUNC_BINOMIAL", "CMD_TIMES", "CMD_CDOT", "CMD_DIV", 
                      "CMD_FRAC", "NUMBER", "DERIVATIVE", "VARIABLE", "MIXNUMBER", 
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
    RULE_exactDivision = 26
    RULE_factorial = 27
    RULE_binomial = 28
    RULE_func = 29
    RULE_funcname = 30
    RULE_bracedMultiExpr = 31
    RULE_parenMultiExpr = 32
    RULE_multiExpr = 33
    RULE_bracedExpr = 34
    RULE_brackExpr = 35
    RULE_parenExpr = 36
    RULE_subexpr = 37
    RULE_supexpr = 38
    RULE_subeq = 39
    RULE_equality = 40
    RULE_relop = 41

    ruleNames =  [ "math", "megaExpr", "specialExpr", "expr", "integralExpr", 
                   "summationExpr", "productExpr", "tailExpr", "funcParams", 
                   "implicitMultiplicationExpr", "subtractionExpr", "additionExpr", 
                   "divisionExpr", "multiplicationExpr", "fracExpr", "powExpr", 
                   "exponentiationExpr", "signedAtom", "negateAtom", "localMultiplication", 
                   "atom", "variable", "indexedVariable", "constant", "number", 
                   "absolute", "exactDivision", "factorial", "binomial", 
                   "func", "funcname", "bracedMultiExpr", "parenMultiExpr", 
                   "multiExpr", "bracedExpr", "brackExpr", "parenExpr", 
                   "subexpr", "supexpr", "subeq", "equality", "relop" ]

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
    UNDERSCORE=14
    CARET=15
    COLON=16
    FUNC_LIM=17
    LIM_APPROACH_SYM=18
    FUNC_INT=19
    FUNC_SUM=20
    FUNC_PROD=21
    FUNC_LOG=22
    FUNC_LN=23
    FUNC_SIN=24
    FUNC_COS=25
    FUNC_TAN=26
    FUNC_CSC=27
    FUNC_SEC=28
    FUNC_COT=29
    FUNC_ARCSIN=30
    FUNC_ARCCOS=31
    FUNC_ARCTAN=32
    FUNC_ARCCSC=33
    FUNC_ARCSEC=34
    FUNC_ARCCOT=35
    FUNC_SINH=36
    FUNC_COSH=37
    FUNC_TANH=38
    FUNC_ARCSINH=39
    FUNC_ARCCOSH=40
    FUNC_ARCTANH=41
    FUNC_ECOS=42
    FUNC_ESIN=43
    FUNC_EDELTAAMPLITUDE=44
    FUNC_ARCECOS=45
    FUNC_ARCESIN=46
    FUNC_ARCEDELTAAMPLITUDE=47
    FUNC_SQRT=48
    FUNC_BINOMIAL=49
    CMD_TIMES=50
    CMD_CDOT=51
    CMD_DIV=52
    CMD_FRAC=53
    NUMBER=54
    DERIVATIVE=55
    VARIABLE=56
    MIXNUMBER=57
    WORD=58
    INFINITY=59
    EQ=60
    LT=61
    LTE=62
    GT=63
    GTE=64
    BANG=65
    GREEKLETTER=66
    GREEKFUNCTIONBRACE=67
    GREEKFUNCTIONPAREN=68
    WS=69

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
            self.state = 84
            self.expr()
            self.state = 85
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
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MINUS) | (1 << MatexParser.L_PAREN) | (1 << MatexParser.L_BRACKET) | (1 << MatexParser.BAR) | (1 << MatexParser.FUNC_LOG) | (1 << MatexParser.FUNC_LN) | (1 << MatexParser.FUNC_SIN) | (1 << MatexParser.FUNC_COS) | (1 << MatexParser.FUNC_TAN) | (1 << MatexParser.FUNC_CSC) | (1 << MatexParser.FUNC_SEC) | (1 << MatexParser.FUNC_COT) | (1 << MatexParser.FUNC_ARCSIN) | (1 << MatexParser.FUNC_ARCCOS) | (1 << MatexParser.FUNC_ARCTAN) | (1 << MatexParser.FUNC_ARCCSC) | (1 << MatexParser.FUNC_ARCSEC) | (1 << MatexParser.FUNC_ARCCOT) | (1 << MatexParser.FUNC_SINH) | (1 << MatexParser.FUNC_COSH) | (1 << MatexParser.FUNC_TANH) | (1 << MatexParser.FUNC_ARCSINH) | (1 << MatexParser.FUNC_ARCCOSH) | (1 << MatexParser.FUNC_ARCTANH) | (1 << MatexParser.FUNC_ECOS) | (1 << MatexParser.FUNC_ESIN) | (1 << MatexParser.FUNC_EDELTAAMPLITUDE) | (1 << MatexParser.FUNC_ARCECOS) | (1 << MatexParser.FUNC_ARCESIN) | (1 << MatexParser.FUNC_ARCEDELTAAMPLITUDE) | (1 << MatexParser.FUNC_SQRT) | (1 << MatexParser.FUNC_BINOMIAL) | (1 << MatexParser.CMD_FRAC) | (1 << MatexParser.NUMBER) | (1 << MatexParser.DERIVATIVE) | (1 << MatexParser.VARIABLE) | (1 << MatexParser.MIXNUMBER) | (1 << MatexParser.WORD) | (1 << MatexParser.INFINITY))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (MatexParser.GREEKLETTER - 66)) | (1 << (MatexParser.GREEKFUNCTIONBRACE - 66)) | (1 << (MatexParser.GREEKFUNCTIONPAREN - 66)))) != 0):
                    self.state = 88
                    self.subtractionExpr(0)
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MatexParser.MUL:
                        self.state = 89
                        self.match(MatexParser.MUL)




                self.state = 94
                self.specialExpr()
                pass

            elif la_ == 2:
                self.state = 95
                self.implicitMultiplicationExpr(0)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MatexParser.MUL:
                    self.state = 96
                    self.match(MatexParser.MUL)


                self.state = 99
                self.specialExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 112
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 103
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 104
                        self.match(MatexParser.PLUS)
                        self.state = 105
                        self.specialExpr()
                        pass

                    elif la_ == 2:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 106
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 107
                        self.match(MatexParser.MINUS)
                        self.state = 108
                        self.specialExpr()
                        pass

                    elif la_ == 3:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 109
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 110
                        self.match(MatexParser.MUL)
                        self.state = 111
                        self.specialExpr()
                        pass

             
                self.state = 116
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
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.FUNC_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.integralExpr()
                pass
            elif token in [MatexParser.FUNC_SUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.summationExpr()
                pass
            elif token in [MatexParser.FUNC_PROD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
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
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.subtractionExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.implicitMultiplicationExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(MatexParser.FUNC_INT)
                self.state = 128
                self.subexpr()
                self.state = 129
                self.supexpr()
                self.state = 130
                self.match(MatexParser.L_BRACE)
                self.state = 131
                self.expr()
                self.state = 132
                self.match(MatexParser.DERIVATIVE)
                self.state = 133
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(MatexParser.FUNC_INT)
                self.state = 136
                self.subexpr()
                self.state = 137
                self.supexpr()
                self.state = 138
                self.expr()
                self.state = 139
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
            self.state = 143
            self.match(MatexParser.FUNC_SUM)
            self.state = 144
            self.funcParams()
            self.state = 145
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
            self.state = 147
            self.match(MatexParser.FUNC_PROD)
            self.state = 148
            self.funcParams()
            self.state = 149
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
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS, MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_INT, MatexParser.FUNC_SUM, MatexParser.FUNC_PROD, MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_ECOS, MatexParser.FUNC_ESIN, MatexParser.FUNC_EDELTAAMPLITUDE, MatexParser.FUNC_ARCECOS, MatexParser.FUNC_ARCESIN, MatexParser.FUNC_ARCEDELTAAMPLITUDE, MatexParser.FUNC_SQRT, MatexParser.FUNC_BINOMIAL, MatexParser.CMD_FRAC, MatexParser.NUMBER, MatexParser.DERIVATIVE, MatexParser.VARIABLE, MatexParser.MIXNUMBER, MatexParser.WORD, MatexParser.INFINITY, MatexParser.GREEKLETTER, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.expr()
                pass
            elif token in [MatexParser.L_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
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
            self.state = 155
            self.subeq()
            self.state = 156
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
            self.state = 159
            self.subtractionExpr(0)
            self.state = 160
            self.subtractionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.ImplicitMultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_implicitMultiplicationExpr)
                    self.state = 162
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 163
                    self.subtractionExpr(0) 
                self.state = 168
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
            self.state = 170
            self.additionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.SubtractionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_subtractionExpr)
                    self.state = 172
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 173
                    self.match(MatexParser.MINUS)
                    self.state = 174
                    self.additionExpr(0) 
                self.state = 179
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
            self.state = 181
            self.divisionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.AdditionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additionExpr)
                    self.state = 183
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 184
                    self.match(MatexParser.PLUS)
                    self.state = 185
                    self.divisionExpr(0) 
                self.state = 190
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
            self.state = 192
            self.multiplicationExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.DivisionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_divisionExpr)
                    self.state = 194
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 195
                    _la = self._input.LA(1)
                    if not(_la==MatexParser.DIV or _la==MatexParser.CMD_DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 196
                    self.multiplicationExpr(0) 
                self.state = 201
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
            self.state = 203
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                    self.state = 205
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 206
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MUL) | (1 << MatexParser.CMD_TIMES) | (1 << MatexParser.CMD_CDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 207
                    self.powExpr() 
                self.state = 212
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
            self.state = 213
            self.match(MatexParser.CMD_FRAC)
            self.state = 214
            self.bracedExpr()
            self.state = 215
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
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.signedAtom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.fracExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.signedAtom()
                self.state = 223
                self.match(MatexParser.CARET)
                self.state = 224
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.signedAtom()
                self.state = 227
                self.match(MatexParser.CARET)
                self.state = 228
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.signedAtom()
                self.state = 231
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
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.negateAtom()
                pass
            elif token in [MatexParser.DERIVATIVE, MatexParser.MIXNUMBER, MatexParser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.localMultiplication()
                pass
            elif token in [MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_ECOS, MatexParser.FUNC_ESIN, MatexParser.FUNC_EDELTAAMPLITUDE, MatexParser.FUNC_ARCECOS, MatexParser.FUNC_ARCESIN, MatexParser.FUNC_ARCEDELTAAMPLITUDE, MatexParser.FUNC_SQRT, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.func()
                pass
            elif token in [MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_BINOMIAL, MatexParser.NUMBER, MatexParser.VARIABLE, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
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
            self.state = 241
            self.match(MatexParser.MINUS)
            self.state = 242
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
            self.state = 244
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


        def exactDivision(self):
            return self.getTypedRuleContext(MatexParser.ExactDivisionContext,0)


        def factorial(self):
            return self.getTypedRuleContext(MatexParser.FactorialContext,0)


        def binomial(self):
            return self.getTypedRuleContext(MatexParser.BinomialContext,0)


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
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.indexedVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 250
                self.absolute()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 251
                self.exactDivision()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 252
                self.factorial()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 253
                self.binomial()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 254
                self.brackExpr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 255
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
            self.state = 258
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
            self.state = 260
            self.match(MatexParser.VARIABLE)
            self.state = 261
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
            self.state = 263
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
            self.state = 265
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
            self.state = 267
            self.match(MatexParser.BAR)
            self.state = 268
            self.expr()
            self.state = 269
            self.match(MatexParser.BAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExactDivisionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(MatexParser.VARIABLE)
            else:
                return self.getToken(MatexParser.VARIABLE, i)

        def BAR(self):
            return self.getToken(MatexParser.BAR, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_exactDivision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExactDivision" ):
                listener.enterExactDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExactDivision" ):
                listener.exitExactDivision(self)




    def exactDivision(self):

        localctx = MatexParser.ExactDivisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exactDivision)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MatexParser.VARIABLE)
            self.state = 272
            self.match(MatexParser.BAR)
            self.state = 273
            self.match(MatexParser.VARIABLE)
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
        self.enterRule(localctx, 54, self.RULE_factorial)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.parenExpr()
                self.state = 276
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.number()
                self.state = 279
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.variable()
                self.state = 282
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

    class BinomialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_BINOMIAL(self):
            return self.getToken(MatexParser.FUNC_BINOMIAL, 0)

        def bracedExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatexParser.BracedExprContext)
            else:
                return self.getTypedRuleContext(MatexParser.BracedExprContext,i)


        def getRuleIndex(self):
            return MatexParser.RULE_binomial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinomial" ):
                listener.enterBinomial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinomial" ):
                listener.exitBinomial(self)




    def binomial(self):

        localctx = MatexParser.BinomialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_binomial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(MatexParser.FUNC_BINOMIAL)
            self.state = 287
            self.bracedExpr()
            self.state = 288
            self.bracedExpr()
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


        def bracedMultiExpr(self):
            return self.getTypedRuleContext(MatexParser.BracedMultiExprContext,0)


        def parenMultiExpr(self):
            return self.getTypedRuleContext(MatexParser.ParenMultiExprContext,0)


        def GREEKFUNCTIONBRACE(self):
            return self.getToken(MatexParser.GREEKFUNCTIONBRACE, 0)

        def multiExpr(self):
            return self.getTypedRuleContext(MatexParser.MultiExprContext,0)


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
        self.enterRule(localctx, 58, self.RULE_func)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.funcname()
                self.state = 291
                self.bracedMultiExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.funcname()
                self.state = 294
                self.parenMultiExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.match(MatexParser.GREEKFUNCTIONBRACE)
                self.state = 297
                self.multiExpr(0)
                self.state = 298
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 300
                self.match(MatexParser.GREEKFUNCTIONPAREN)
                self.state = 301
                self.multiExpr(0)
                self.state = 302
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

        def FUNC_ECOS(self):
            return self.getToken(MatexParser.FUNC_ECOS, 0)

        def FUNC_EDELTAAMPLITUDE(self):
            return self.getToken(MatexParser.FUNC_EDELTAAMPLITUDE, 0)

        def FUNC_ESIN(self):
            return self.getToken(MatexParser.FUNC_ESIN, 0)

        def FUNC_ARCECOS(self):
            return self.getToken(MatexParser.FUNC_ARCECOS, 0)

        def FUNC_ARCEDELTAAMPLITUDE(self):
            return self.getToken(MatexParser.FUNC_ARCEDELTAAMPLITUDE, 0)

        def FUNC_ARCESIN(self):
            return self.getToken(MatexParser.FUNC_ARCESIN, 0)

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
        self.enterRule(localctx, 60, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.FUNC_LOG) | (1 << MatexParser.FUNC_LN) | (1 << MatexParser.FUNC_SIN) | (1 << MatexParser.FUNC_COS) | (1 << MatexParser.FUNC_TAN) | (1 << MatexParser.FUNC_CSC) | (1 << MatexParser.FUNC_SEC) | (1 << MatexParser.FUNC_COT) | (1 << MatexParser.FUNC_ARCSIN) | (1 << MatexParser.FUNC_ARCCOS) | (1 << MatexParser.FUNC_ARCTAN) | (1 << MatexParser.FUNC_ARCCSC) | (1 << MatexParser.FUNC_ARCSEC) | (1 << MatexParser.FUNC_ARCCOT) | (1 << MatexParser.FUNC_SINH) | (1 << MatexParser.FUNC_COSH) | (1 << MatexParser.FUNC_TANH) | (1 << MatexParser.FUNC_ARCSINH) | (1 << MatexParser.FUNC_ARCCOSH) | (1 << MatexParser.FUNC_ARCTANH) | (1 << MatexParser.FUNC_ECOS) | (1 << MatexParser.FUNC_ESIN) | (1 << MatexParser.FUNC_EDELTAAMPLITUDE) | (1 << MatexParser.FUNC_ARCECOS) | (1 << MatexParser.FUNC_ARCESIN) | (1 << MatexParser.FUNC_ARCEDELTAAMPLITUDE) | (1 << MatexParser.FUNC_SQRT))) != 0)):
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

    class BracedMultiExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def multiExpr(self):
            return self.getTypedRuleContext(MatexParser.MultiExprContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_bracedMultiExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracedMultiExpr" ):
                listener.enterBracedMultiExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracedMultiExpr" ):
                listener.exitBracedMultiExpr(self)




    def bracedMultiExpr(self):

        localctx = MatexParser.BracedMultiExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_bracedMultiExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(MatexParser.L_BRACE)
            self.state = 309
            self.multiExpr(0)
            self.state = 310
            self.match(MatexParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParenMultiExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MatexParser.L_PAREN, 0)

        def multiExpr(self):
            return self.getTypedRuleContext(MatexParser.MultiExprContext,0)


        def R_PAREN(self):
            return self.getToken(MatexParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_parenMultiExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenMultiExpr" ):
                listener.enterParenMultiExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenMultiExpr" ):
                listener.exitParenMultiExpr(self)




    def parenMultiExpr(self):

        localctx = MatexParser.ParenMultiExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_parenMultiExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(MatexParser.L_PAREN)
            self.state = 313
            self.multiExpr(0)
            self.state = 314
            self.match(MatexParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MatexParser.ExprContext,0)


        def multiExpr(self):
            return self.getTypedRuleContext(MatexParser.MultiExprContext,0)


        def COMMA(self):
            return self.getToken(MatexParser.COMMA, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_multiExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiExpr" ):
                listener.enterMultiExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiExpr" ):
                listener.exitMultiExpr(self)



    def multiExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatexParser.MultiExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_multiExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiExpr)
                    self.state = 319
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 320
                    self.match(MatexParser.COMMA)
                    self.state = 321
                    self.expr() 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 68, self.RULE_bracedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MatexParser.L_BRACE)
            self.state = 328
            self.expr()
            self.state = 329
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
        self.enterRule(localctx, 70, self.RULE_brackExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MatexParser.L_BRACKET)
            self.state = 332
            self.expr()
            self.state = 333
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
        self.enterRule(localctx, 72, self.RULE_parenExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MatexParser.L_PAREN)
            self.state = 336
            self.expr()
            self.state = 337
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
        self.enterRule(localctx, 74, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(MatexParser.UNDERSCORE)
            self.state = 340
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
        self.enterRule(localctx, 76, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(MatexParser.CARET)
            self.state = 343
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
        self.enterRule(localctx, 78, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(MatexParser.UNDERSCORE)
            self.state = 346
            self.match(MatexParser.L_BRACE)
            self.state = 347
            self.equality()
            self.state = 348
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
        self.enterRule(localctx, 80, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.variable()
            self.state = 351
            self.match(MatexParser.EQ)
            self.state = 352
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
        self.enterRule(localctx, 82, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not(((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & ((1 << (MatexParser.EQ - 60)) | (1 << (MatexParser.LT - 60)) | (1 << (MatexParser.LTE - 60)) | (1 << (MatexParser.GT - 60)) | (1 << (MatexParser.GTE - 60)))) != 0)):
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
        self._predicates[33] = self.multiExpr_sempred
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
         

    def multiExpr_sempred(self, localctx:MultiExprContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         




