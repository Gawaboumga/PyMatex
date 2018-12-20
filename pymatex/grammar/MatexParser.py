# Generated from .\pymatex\grammar\MatexParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("\u01dc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\5\3w\n\3\3\3\3\3\3\3\3\3\5\3}\n\3\3\3\3\3\3\3\5")
        buf.write("\3\u0082\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\u008d")
        buf.write("\n\3\f\3\16\3\u0090\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4\u009c\n\4\3\5\3\5\3\5\5\5\u00a1\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u00b1\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\5\20\u00d9\n\20\3\21\3\21\3\21\3\22\3")
        buf.write("\22\5\22\u00e0\n\22\3\23\3\23\5\23\u00e4\n\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\7\24\u00ec\n\24\f\24\16\24\u00ef")
        buf.write("\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00f7\n\25\f")
        buf.write("\25\16\25\u00fa\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u0102\n\26\f\26\16\26\u0105\13\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\7\27\u010d\n\27\f\27\16\27\u0110\13\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\7\30\u0118\n\30\f\30\16\30")
        buf.write("\u011b\13\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\5\32\u0124")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u0131\n\33\3\34\3\34\3\34\3\34\5\34\u0137\n")
        buf.write("\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\5\37\u0148\n\37\3 \3 \3!\3!")
        buf.write("\3!\3\"\3\"\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&")
        buf.write("\3&\3&\3&\3&\3&\5&\u0164\n&\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0178\n(\3)\3)\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\7,\u018a\n,\f,\16")
        buf.write(",\u018d\13,\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\5\66\u01b7\n\66\3\66\3\66\3")
        buf.write("\66\5\66\u01bc\n\66\3\66\3\66\3\66\3\66\5\66\u01c2\n\66")
        buf.write("\7\66\u01c4\n\66\f\66\16\66\u01c7\13\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\5\67\u01d1\n\67\38\38\38\38")
        buf.write("\38\58\u01d8\n8\38\38\38\2\n\4&(*,.Vj9\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjln\2\n\4\2\6\688\4\2\5\5\66\67\4\2")
        buf.write(";;=>\4\2<<CC\4\2DDFF\4\2EEGG\3\2\32\64\4\2\r\r\17\17\2")
        buf.write("\u01db\2p\3\2\2\2\4\u0081\3\2\2\2\6\u009b\3\2\2\2\b\u00a0")
        buf.write("\3\2\2\2\n\u00b0\3\2\2\2\f\u00b2\3\2\2\2\16\u00b6\3\2")
        buf.write("\2\2\20\u00ba\3\2\2\2\22\u00be\3\2\2\2\24\u00c2\3\2\2")
        buf.write("\2\26\u00c6\3\2\2\2\30\u00ca\3\2\2\2\32\u00ce\3\2\2\2")
        buf.write("\34\u00d2\3\2\2\2\36\u00d8\3\2\2\2 \u00da\3\2\2\2\"\u00dd")
        buf.write("\3\2\2\2$\u00e1\3\2\2\2&\u00e5\3\2\2\2(\u00f0\3\2\2\2")
        buf.write("*\u00fb\3\2\2\2,\u0106\3\2\2\2.\u0111\3\2\2\2\60\u011c")
        buf.write("\3\2\2\2\62\u0123\3\2\2\2\64\u0130\3\2\2\2\66\u0136\3")
        buf.write("\2\2\28\u0138\3\2\2\2:\u013b\3\2\2\2<\u0147\3\2\2\2>\u0149")
        buf.write("\3\2\2\2@\u014b\3\2\2\2B\u014e\3\2\2\2D\u0150\3\2\2\2")
        buf.write("F\u0152\3\2\2\2H\u0156\3\2\2\2J\u0163\3\2\2\2L\u0165\3")
        buf.write("\2\2\2N\u0177\3\2\2\2P\u0179\3\2\2\2R\u017b\3\2\2\2T\u017f")
        buf.write("\3\2\2\2V\u0183\3\2\2\2X\u018e\3\2\2\2Z\u0192\3\2\2\2")
        buf.write("\\\u0196\3\2\2\2^\u019a\3\2\2\2`\u019d\3\2\2\2b\u01a0")
        buf.write("\3\2\2\2d\u01a5\3\2\2\2f\u01aa\3\2\2\2h\u01af\3\2\2\2")
        buf.write("j\u01b3\3\2\2\2l\u01d0\3\2\2\2n\u01d2\3\2\2\2pq\5\b\5")
        buf.write("\2qr\7\2\2\3r\3\3\2\2\2st\b\3\1\2tv\5(\25\2uw\7\5\2\2")
        buf.write("vu\3\2\2\2vw\3\2\2\2wx\3\2\2\2xy\5\6\4\2y\u0082\3\2\2")
        buf.write("\2z|\5&\24\2{}\7\5\2\2|{\3\2\2\2|}\3\2\2\2}~\3\2\2\2~")
        buf.write("\177\5\6\4\2\177\u0082\3\2\2\2\u0080\u0082\5\6\4\2\u0081")
        buf.write("s\3\2\2\2\u0081z\3\2\2\2\u0081\u0080\3\2\2\2\u0082\u008e")
        buf.write("\3\2\2\2\u0083\u0084\f\6\2\2\u0084\u0085\7\3\2\2\u0085")
        buf.write("\u008d\5\6\4\2\u0086\u0087\f\5\2\2\u0087\u0088\7\4\2\2")
        buf.write("\u0088\u008d\5\6\4\2\u0089\u008a\f\4\2\2\u008a\u008b\7")
        buf.write("\5\2\2\u008b\u008d\5\6\4\2\u008c\u0083\3\2\2\2\u008c\u0086")
        buf.write("\3\2\2\2\u008c\u0089\3\2\2\2\u008d\u0090\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\5\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0091\u009c\5\n\6\2\u0092\u009c\5\f\7\2")
        buf.write("\u0093\u009c\5\16\b\2\u0094\u009c\5\20\t\2\u0095\u009c")
        buf.write("\5\22\n\2\u0096\u009c\5\24\13\2\u0097\u009c\5\26\f\2\u0098")
        buf.write("\u009c\5\30\r\2\u0099\u009c\5\32\16\2\u009a\u009c\5\34")
        buf.write("\17\2\u009b\u0091\3\2\2\2\u009b\u0092\3\2\2\2\u009b\u0093")
        buf.write("\3\2\2\2\u009b\u0094\3\2\2\2\u009b\u0095\3\2\2\2\u009b")
        buf.write("\u0096\3\2\2\2\u009b\u0097\3\2\2\2\u009b\u0098\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c\7\3\2\2")
        buf.write("\2\u009d\u00a1\5(\25\2\u009e\u00a1\5&\24\2\u009f\u00a1")
        buf.write("\5\4\3\2\u00a0\u009d\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\t\3\2\2\2\u00a2\u00a3\7\27\2\2\u00a3")
        buf.write("\u00a4\5^\60\2\u00a4\u00a5\5`\61\2\u00a5\u00a6\7\t\2\2")
        buf.write("\u00a6\u00a7\5\b\5\2\u00a7\u00a8\7;\2\2\u00a8\u00a9\7")
        buf.write("\n\2\2\u00a9\u00b1\3\2\2\2\u00aa\u00ab\7\27\2\2\u00ab")
        buf.write("\u00ac\5^\60\2\u00ac\u00ad\5`\61\2\u00ad\u00ae\5\b\5\2")
        buf.write("\u00ae\u00af\7;\2\2\u00af\u00b1\3\2\2\2\u00b0\u00a2\3")
        buf.write("\2\2\2\u00b0\u00aa\3\2\2\2\u00b1\13\3\2\2\2\u00b2\u00b3")
        buf.write("\7\26\2\2\u00b3\u00b4\5 \21\2\u00b4\u00b5\5\36\20\2\u00b5")
        buf.write("\r\3\2\2\2\u00b6\u00b7\7\26\2\2\u00b7\u00b8\5\"\22\2\u00b8")
        buf.write("\u00b9\5\36\20\2\u00b9\17\3\2\2\2\u00ba\u00bb\7\26\2\2")
        buf.write("\u00bb\u00bc\5$\23\2\u00bc\u00bd\5\36\20\2\u00bd\21\3")
        buf.write("\2\2\2\u00be\u00bf\7\30\2\2\u00bf\u00c0\5 \21\2\u00c0")
        buf.write("\u00c1\5\36\20\2\u00c1\23\3\2\2\2\u00c2\u00c3\7\30\2\2")
        buf.write("\u00c3\u00c4\5\"\22\2\u00c4\u00c5\5\36\20\2\u00c5\25\3")
        buf.write("\2\2\2\u00c6\u00c7\7\30\2\2\u00c7\u00c8\5$\23\2\u00c8")
        buf.write("\u00c9\5\36\20\2\u00c9\27\3\2\2\2\u00ca\u00cb\7\31\2\2")
        buf.write("\u00cb\u00cc\5 \21\2\u00cc\u00cd\5\36\20\2\u00cd\31\3")
        buf.write("\2\2\2\u00ce\u00cf\7\31\2\2\u00cf\u00d0\5\"\22\2\u00d0")
        buf.write("\u00d1\5\36\20\2\u00d1\33\3\2\2\2\u00d2\u00d3\7\31\2\2")
        buf.write("\u00d3\u00d4\5$\23\2\u00d4\u00d5\5\36\20\2\u00d5\35\3")
        buf.write("\2\2\2\u00d6\u00d9\5\b\5\2\u00d7\u00d9\5X-\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\37\3\2\2\2\u00da\u00db")
        buf.write("\5b\62\2\u00db\u00dc\5`\61\2\u00dc!\3\2\2\2\u00dd\u00df")
        buf.write("\5d\63\2\u00de\u00e0\5`\61\2\u00df\u00de\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0#\3\2\2\2\u00e1\u00e3\5f\64\2\u00e2")
        buf.write("\u00e4\5`\61\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4%\3\2\2\2\u00e5\u00e6\b\24\1\2\u00e6\u00e7\5(\25")
        buf.write("\2\u00e7\u00e8\5(\25\2\u00e8\u00ed\3\2\2\2\u00e9\u00ea")
        buf.write("\f\3\2\2\u00ea\u00ec\5(\25\2\u00eb\u00e9\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\'\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\b\25")
        buf.write("\1\2\u00f1\u00f2\5*\26\2\u00f2\u00f8\3\2\2\2\u00f3\u00f4")
        buf.write("\f\3\2\2\u00f4\u00f5\7\4\2\2\u00f5\u00f7\5*\26\2\u00f6")
        buf.write("\u00f3\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9)\3\2\2\2\u00fa\u00f8\3\2\2")
        buf.write("\2\u00fb\u00fc\b\26\1\2\u00fc\u00fd\5,\27\2\u00fd\u0103")
        buf.write("\3\2\2\2\u00fe\u00ff\f\3\2\2\u00ff\u0100\7\3\2\2\u0100")
        buf.write("\u0102\5,\27\2\u0101\u00fe\3\2\2\2\u0102\u0105\3\2\2\2")
        buf.write("\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104+\3\2\2")
        buf.write("\2\u0105\u0103\3\2\2\2\u0106\u0107\b\27\1\2\u0107\u0108")
        buf.write("\5.\30\2\u0108\u010e\3\2\2\2\u0109\u010a\f\3\2\2\u010a")
        buf.write("\u010b\t\2\2\2\u010b\u010d\5.\30\2\u010c\u0109\3\2\2\2")
        buf.write("\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3")
        buf.write("\2\2\2\u010f-\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112")
        buf.write("\b\30\1\2\u0112\u0113\5\62\32\2\u0113\u0119\3\2\2\2\u0114")
        buf.write("\u0115\f\3\2\2\u0115\u0116\t\3\2\2\u0116\u0118\5\62\32")
        buf.write("\2\u0117\u0114\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a/\3\2\2\2\u011b\u0119")
        buf.write("\3\2\2\2\u011c\u011d\79\2\2\u011d\u011e\5X-\2\u011e\u011f")
        buf.write("\5X-\2\u011f\61\3\2\2\2\u0120\u0124\5\66\34\2\u0121\u0124")
        buf.write("\5\60\31\2\u0122\u0124\5\64\33\2\u0123\u0120\3\2\2\2\u0123")
        buf.write("\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124\63\3\2\2\2\u0125")
        buf.write("\u0126\5\66\34\2\u0126\u0127\7\22\2\2\u0127\u0128\5D#")
        buf.write("\2\u0128\u0131\3\2\2\2\u0129\u012a\5\66\34\2\u012a\u012b")
        buf.write("\7\22\2\2\u012b\u012c\5> \2\u012c\u0131\3\2\2\2\u012d")
        buf.write("\u012e\5\66\34\2\u012e\u012f\5`\61\2\u012f\u0131\3\2\2")
        buf.write("\2\u0130\u0125\3\2\2\2\u0130\u0129\3\2\2\2\u0130\u012d")
        buf.write("\3\2\2\2\u0131\65\3\2\2\2\u0132\u0137\58\35\2\u0133\u0137")
        buf.write("\5:\36\2\u0134\u0137\5N(\2\u0135\u0137\5<\37\2\u0136\u0132")
        buf.write("\3\2\2\2\u0136\u0133\3\2\2\2\u0136\u0134\3\2\2\2\u0136")
        buf.write("\u0135\3\2\2\2\u0137\67\3\2\2\2\u0138\u0139\7\4\2\2\u0139")
        buf.write("\u013a\5\66\34\2\u013a9\3\2\2\2\u013b\u013c\t\4\2\2\u013c")
        buf.write(";\3\2\2\2\u013d\u0148\5> \2\u013e\u0148\5@!\2\u013f\u0148")
        buf.write("\5B\"\2\u0140\u0148\5D#\2\u0141\u0148\5F$\2\u0142\u0148")
        buf.write("\5H%\2\u0143\u0148\5J&\2\u0144\u0148\5L\'\2\u0145\u0148")
        buf.write("\5Z.\2\u0146\u0148\5\\/\2\u0147\u013d\3\2\2\2\u0147\u013e")
        buf.write("\3\2\2\2\u0147\u013f\3\2\2\2\u0147\u0140\3\2\2\2\u0147")
        buf.write("\u0141\3\2\2\2\u0147\u0142\3\2\2\2\u0147\u0143\3\2\2\2")
        buf.write("\u0147\u0144\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0146\3")
        buf.write("\2\2\2\u0148=\3\2\2\2\u0149\u014a\t\5\2\2\u014a?\3\2\2")
        buf.write("\2\u014b\u014c\7<\2\2\u014c\u014d\5^\60\2\u014dA\3\2\2")
        buf.write("\2\u014e\u014f\7?\2\2\u014fC\3\2\2\2\u0150\u0151\7:\2")
        buf.write("\2\u0151E\3\2\2\2\u0152\u0153\7\20\2\2\u0153\u0154\5\b")
        buf.write("\5\2\u0154\u0155\7\20\2\2\u0155G\3\2\2\2\u0156\u0157\7")
        buf.write("<\2\2\u0157\u0158\7\20\2\2\u0158\u0159\7<\2\2\u0159I\3")
        buf.write("\2\2\2\u015a\u015b\5\\/\2\u015b\u015c\7B\2\2\u015c\u0164")
        buf.write("\3\2\2\2\u015d\u015e\5D#\2\u015e\u015f\7B\2\2\u015f\u0164")
        buf.write("\3\2\2\2\u0160\u0161\5> \2\u0161\u0162\7B\2\2\u0162\u0164")
        buf.write("\3\2\2\2\u0163\u015a\3\2\2\2\u0163\u015d\3\2\2\2\u0163")
        buf.write("\u0160\3\2\2\2\u0164K\3\2\2\2\u0165\u0166\7\65\2\2\u0166")
        buf.write("\u0167\5X-\2\u0167\u0168\5X-\2\u0168M\3\2\2\2\u0169\u016a")
        buf.write("\5P)\2\u016a\u016b\5R*\2\u016b\u0178\3\2\2\2\u016c\u016d")
        buf.write("\5P)\2\u016d\u016e\5T+\2\u016e\u0178\3\2\2\2\u016f\u0170")
        buf.write("\t\6\2\2\u0170\u0171\5V,\2\u0171\u0172\7\n\2\2\u0172\u0178")
        buf.write("\3\2\2\2\u0173\u0174\t\7\2\2\u0174\u0175\5V,\2\u0175\u0176")
        buf.write("\7\b\2\2\u0176\u0178\3\2\2\2\u0177\u0169\3\2\2\2\u0177")
        buf.write("\u016c\3\2\2\2\u0177\u016f\3\2\2\2\u0177\u0173\3\2\2\2")
        buf.write("\u0178O\3\2\2\2\u0179\u017a\t\b\2\2\u017aQ\3\2\2\2\u017b")
        buf.write("\u017c\7\t\2\2\u017c\u017d\5V,\2\u017d\u017e\7\n\2\2\u017e")
        buf.write("S\3\2\2\2\u017f\u0180\7\7\2\2\u0180\u0181\5V,\2\u0181")
        buf.write("\u0182\7\b\2\2\u0182U\3\2\2\2\u0183\u0184\b,\1\2\u0184")
        buf.write("\u0185\5\b\5\2\u0185\u018b\3\2\2\2\u0186\u0187\f\3\2\2")
        buf.write("\u0187\u0188\t\t\2\2\u0188\u018a\5\b\5\2\u0189\u0186\3")
        buf.write("\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018cW\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f")
        buf.write("\7\t\2\2\u018f\u0190\5\b\5\2\u0190\u0191\7\n\2\2\u0191")
        buf.write("Y\3\2\2\2\u0192\u0193\7\13\2\2\u0193\u0194\5\b\5\2\u0194")
        buf.write("\u0195\7\f\2\2\u0195[\3\2\2\2\u0196\u0197\7\7\2\2\u0197")
        buf.write("\u0198\5\b\5\2\u0198\u0199\7\b\2\2\u0199]\3\2\2\2\u019a")
        buf.write("\u019b\7\21\2\2\u019b\u019c\5X-\2\u019c_\3\2\2\2\u019d")
        buf.write("\u019e\7\22\2\2\u019e\u019f\5X-\2\u019fa\3\2\2\2\u01a0")
        buf.write("\u01a1\7\21\2\2\u01a1\u01a2\7\t\2\2\u01a2\u01a3\5h\65")
        buf.write("\2\u01a3\u01a4\7\n\2\2\u01a4c\3\2\2\2\u01a5\u01a6\7\21")
        buf.write("\2\2\u01a6\u01a7\7\t\2\2\u01a7\u01a8\5j\66\2\u01a8\u01a9")
        buf.write("\7\n\2\2\u01a9e\3\2\2\2\u01aa\u01ab\7\21\2\2\u01ab\u01ac")
        buf.write("\7\t\2\2\u01ac\u01ad\5l\67\2\u01ad\u01ae\7\n\2\2\u01ae")
        buf.write("g\3\2\2\2\u01af\u01b0\5> \2\u01b0\u01b1\7@\2\2\u01b1\u01b2")
        buf.write("\5\b\5\2\u01b2i\3\2\2\2\u01b3\u01b6\b\66\1\2\u01b4\u01b7")
        buf.write("\5> \2\u01b5\u01b7\5D#\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01bb\7A\2\2\u01b9")
        buf.write("\u01bc\5> \2\u01ba\u01bc\5D#\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write("\u01ba\3\2\2\2\u01bc\u01c5\3\2\2\2\u01bd\u01be\f\3\2\2")
        buf.write("\u01be\u01c1\7A\2\2\u01bf\u01c2\5> \2\u01c0\u01c2\5D#")
        buf.write("\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01bd\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6k\3\2\2\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c8\u01c9\5> \2\u01c9\u01ca\7H\2\2\u01ca")
        buf.write("\u01cb\5> \2\u01cb\u01d1\3\2\2\2\u01cc\u01cd\5> \2\u01cd")
        buf.write("\u01ce\7H\2\2\u01ce\u01cf\5n8\2\u01cf\u01d1\3\2\2\2\u01d0")
        buf.write("\u01c8\3\2\2\2\u01d0\u01cc\3\2\2\2\u01d1m\3\2\2\2\u01d2")
        buf.write("\u01d3\5> \2\u01d3\u01d4\7J\2\2\u01d4\u01d7\7\t\2\2\u01d5")
        buf.write("\u01d8\5D#\2\u01d6\u01d8\5> \2\u01d7\u01d5\3\2\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\7\n\2\2")
        buf.write("\u01dao\3\2\2\2\37v|\u0081\u008c\u008e\u009b\u00a0\u00b0")
        buf.write("\u00d8\u00df\u00e3\u00ed\u00f8\u0103\u010e\u0119\u0123")
        buf.write("\u0130\u0136\u0147\u0163\u0177\u018b\u01b6\u01bb\u01c1")
        buf.write("\u01c5\u01d0\u01d7")
        return buf.getvalue()


class MatexParser ( Parser ):

    grammarFileName = "MatexParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "'.'", "';'", "'|'", 
                     "'_'", "'^'", "':'", "'\\lim'", "<INVALID>", "'K'", 
                     "'\\int'", "'\\sum'", "'\\prod'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\times'", "'\\cdot'", 
                     "'\\div'", "'\\frac'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\infty'", "'='", "<INVALID>", 
                     "'!'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\in'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "L_PAREN", 
                      "R_PAREN", "L_BRACE", "R_BRACE", "L_BRACKET", "R_BRACKET", 
                      "COMMA", "DOT", "SEMICOLON", "BAR", "UNDERSCORE", 
                      "CARET", "COLON", "FUNC_LIM", "LIM_APPROACH_SYM", 
                      "FUNC_FRAC", "FUNC_INT", "FUNC_SUM", "FUNC_PROD", 
                      "FUNC_LOG", "FUNC_LN", "FUNC_SIN", "FUNC_COS", "FUNC_TAN", 
                      "FUNC_CSC", "FUNC_SEC", "FUNC_COT", "FUNC_ARCSIN", 
                      "FUNC_ARCCOS", "FUNC_ARCTAN", "FUNC_ARCCSC", "FUNC_ARCSEC", 
                      "FUNC_ARCCOT", "FUNC_SINH", "FUNC_COSH", "FUNC_TANH", 
                      "FUNC_ARCSINH", "FUNC_ARCCOSH", "FUNC_ARCTANH", "FUNC_ECOS", 
                      "FUNC_ESIN", "FUNC_EDELTAAMPLITUDE", "FUNC_ARCECOS", 
                      "FUNC_ARCESIN", "FUNC_ARCEDELTAAMPLITUDE", "FUNC_SQRT", 
                      "FUNC_BINOMIAL", "CMD_TIMES", "CMD_CDOT", "CMD_DIV", 
                      "CMD_FRAC", "NUMBER", "DERIVATIVE", "VARIABLE", "MIXNUMBER", 
                      "WORD", "INFINITY", "EQ", "INEQUALITIES", "BANG", 
                      "GREEKLETTER", "LETTERFUNCTIONBRACE", "LETTERFUNCTIONPAREN", 
                      "GREEKFUNCTIONBRACE", "GREEKFUNCTIONPAREN", "SET_IN", 
                      "SET_LIKE", "SET_DIFFERENCE", "WS" ]

    RULE_math = 0
    RULE_megaExpr = 1
    RULE_specialExpr = 2
    RULE_expr = 3
    RULE_integralExpr = 4
    RULE_continuedFactionExpr = 5
    RULE_continuedFactionInequalityExpr = 6
    RULE_continuedFactionSetExpr = 7
    RULE_summationExpr = 8
    RULE_summationInequalityExpr = 9
    RULE_summationSetExpr = 10
    RULE_productExpr = 11
    RULE_productInequalityExpr = 12
    RULE_productSetExpr = 13
    RULE_tailExpr = 14
    RULE_funcParams = 15
    RULE_funcIneqParams = 16
    RULE_funcSetParams = 17
    RULE_implicitMultiplicationExpr = 18
    RULE_subtractionExpr = 19
    RULE_additionExpr = 20
    RULE_divisionExpr = 21
    RULE_multiplicationExpr = 22
    RULE_fracExpr = 23
    RULE_powExpr = 24
    RULE_exponentiationExpr = 25
    RULE_signedAtom = 26
    RULE_negateAtom = 27
    RULE_localMultiplication = 28
    RULE_atom = 29
    RULE_variable = 30
    RULE_indexedVariable = 31
    RULE_constant = 32
    RULE_number = 33
    RULE_absolute = 34
    RULE_exactDivision = 35
    RULE_factorial = 36
    RULE_binomial = 37
    RULE_func = 38
    RULE_funcname = 39
    RULE_bracedMultiExpr = 40
    RULE_parenMultiExpr = 41
    RULE_multiExpr = 42
    RULE_bracedExpr = 43
    RULE_brackExpr = 44
    RULE_parenExpr = 45
    RULE_subexpr = 46
    RULE_supexpr = 47
    RULE_subeq = 48
    RULE_subIneq = 49
    RULE_subSet = 50
    RULE_equality = 51
    RULE_inequality = 52
    RULE_setExpr = 53
    RULE_setDifferenceExpr = 54

    ruleNames =  [ "math", "megaExpr", "specialExpr", "expr", "integralExpr", 
                   "continuedFactionExpr", "continuedFactionInequalityExpr", 
                   "continuedFactionSetExpr", "summationExpr", "summationInequalityExpr", 
                   "summationSetExpr", "productExpr", "productInequalityExpr", 
                   "productSetExpr", "tailExpr", "funcParams", "funcIneqParams", 
                   "funcSetParams", "implicitMultiplicationExpr", "subtractionExpr", 
                   "additionExpr", "divisionExpr", "multiplicationExpr", 
                   "fracExpr", "powExpr", "exponentiationExpr", "signedAtom", 
                   "negateAtom", "localMultiplication", "atom", "variable", 
                   "indexedVariable", "constant", "number", "absolute", 
                   "exactDivision", "factorial", "binomial", "func", "funcname", 
                   "bracedMultiExpr", "parenMultiExpr", "multiExpr", "bracedExpr", 
                   "brackExpr", "parenExpr", "subexpr", "supexpr", "subeq", 
                   "subIneq", "subSet", "equality", "inequality", "setExpr", 
                   "setDifferenceExpr" ]

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
    SEMICOLON=13
    BAR=14
    UNDERSCORE=15
    CARET=16
    COLON=17
    FUNC_LIM=18
    LIM_APPROACH_SYM=19
    FUNC_FRAC=20
    FUNC_INT=21
    FUNC_SUM=22
    FUNC_PROD=23
    FUNC_LOG=24
    FUNC_LN=25
    FUNC_SIN=26
    FUNC_COS=27
    FUNC_TAN=28
    FUNC_CSC=29
    FUNC_SEC=30
    FUNC_COT=31
    FUNC_ARCSIN=32
    FUNC_ARCCOS=33
    FUNC_ARCTAN=34
    FUNC_ARCCSC=35
    FUNC_ARCSEC=36
    FUNC_ARCCOT=37
    FUNC_SINH=38
    FUNC_COSH=39
    FUNC_TANH=40
    FUNC_ARCSINH=41
    FUNC_ARCCOSH=42
    FUNC_ARCTANH=43
    FUNC_ECOS=44
    FUNC_ESIN=45
    FUNC_EDELTAAMPLITUDE=46
    FUNC_ARCECOS=47
    FUNC_ARCESIN=48
    FUNC_ARCEDELTAAMPLITUDE=49
    FUNC_SQRT=50
    FUNC_BINOMIAL=51
    CMD_TIMES=52
    CMD_CDOT=53
    CMD_DIV=54
    CMD_FRAC=55
    NUMBER=56
    DERIVATIVE=57
    VARIABLE=58
    MIXNUMBER=59
    WORD=60
    INFINITY=61
    EQ=62
    INEQUALITIES=63
    BANG=64
    GREEKLETTER=65
    LETTERFUNCTIONBRACE=66
    LETTERFUNCTIONPAREN=67
    GREEKFUNCTIONBRACE=68
    GREEKFUNCTIONPAREN=69
    SET_IN=70
    SET_LIKE=71
    SET_DIFFERENCE=72
    WS=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
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
            self.state = 110
            self.expr()
            self.state = 111
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

        def subtractionExpr(self):
            return self.getTypedRuleContext(MatexParser.SubtractionExprContext,0)


        def specialExpr(self):
            return self.getTypedRuleContext(MatexParser.SpecialExprContext,0)


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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 114
                self.subtractionExpr(0)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MatexParser.MUL:
                    self.state = 115
                    self.match(MatexParser.MUL)


                self.state = 118
                self.specialExpr()
                pass

            elif la_ == 2:
                self.state = 120
                self.implicitMultiplicationExpr(0)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MatexParser.MUL:
                    self.state = 121
                    self.match(MatexParser.MUL)


                self.state = 124
                self.specialExpr()
                pass

            elif la_ == 3:
                self.state = 126
                self.specialExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 138
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 129
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 130
                        self.match(MatexParser.PLUS)
                        self.state = 131
                        self.specialExpr()
                        pass

                    elif la_ == 2:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 132
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 133
                        self.match(MatexParser.MINUS)
                        self.state = 134
                        self.specialExpr()
                        pass

                    elif la_ == 3:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 135
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 136
                        self.match(MatexParser.MUL)
                        self.state = 137
                        self.specialExpr()
                        pass

             
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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


        def continuedFactionExpr(self):
            return self.getTypedRuleContext(MatexParser.ContinuedFactionExprContext,0)


        def continuedFactionInequalityExpr(self):
            return self.getTypedRuleContext(MatexParser.ContinuedFactionInequalityExprContext,0)


        def continuedFactionSetExpr(self):
            return self.getTypedRuleContext(MatexParser.ContinuedFactionSetExprContext,0)


        def summationExpr(self):
            return self.getTypedRuleContext(MatexParser.SummationExprContext,0)


        def summationInequalityExpr(self):
            return self.getTypedRuleContext(MatexParser.SummationInequalityExprContext,0)


        def summationSetExpr(self):
            return self.getTypedRuleContext(MatexParser.SummationSetExprContext,0)


        def productExpr(self):
            return self.getTypedRuleContext(MatexParser.ProductExprContext,0)


        def productInequalityExpr(self):
            return self.getTypedRuleContext(MatexParser.ProductInequalityExprContext,0)


        def productSetExpr(self):
            return self.getTypedRuleContext(MatexParser.ProductSetExprContext,0)


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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.integralExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.continuedFactionExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.continuedFactionInequalityExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.continuedFactionSetExpr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.summationExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.summationInequalityExpr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 149
                self.summationSetExpr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 150
                self.productExpr()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 151
                self.productInequalityExpr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 152
                self.productSetExpr()
                pass


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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.subtractionExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.implicitMultiplicationExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
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
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(MatexParser.FUNC_INT)
                self.state = 161
                self.subexpr()
                self.state = 162
                self.supexpr()
                self.state = 163
                self.match(MatexParser.L_BRACE)
                self.state = 164
                self.expr()
                self.state = 165
                self.match(MatexParser.DERIVATIVE)
                self.state = 166
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(MatexParser.FUNC_INT)
                self.state = 169
                self.subexpr()
                self.state = 170
                self.supexpr()
                self.state = 171
                self.expr()
                self.state = 172
                self.match(MatexParser.DERIVATIVE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuedFactionExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_FRAC(self):
            return self.getToken(MatexParser.FUNC_FRAC, 0)

        def funcParams(self):
            return self.getTypedRuleContext(MatexParser.FuncParamsContext,0)


        def tailExpr(self):
            return self.getTypedRuleContext(MatexParser.TailExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_continuedFactionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinuedFactionExpr" ):
                listener.enterContinuedFactionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinuedFactionExpr" ):
                listener.exitContinuedFactionExpr(self)




    def continuedFactionExpr(self):

        localctx = MatexParser.ContinuedFactionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_continuedFactionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(MatexParser.FUNC_FRAC)
            self.state = 177
            self.funcParams()
            self.state = 178
            self.tailExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuedFactionInequalityExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_FRAC(self):
            return self.getToken(MatexParser.FUNC_FRAC, 0)

        def funcIneqParams(self):
            return self.getTypedRuleContext(MatexParser.FuncIneqParamsContext,0)


        def tailExpr(self):
            return self.getTypedRuleContext(MatexParser.TailExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_continuedFactionInequalityExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinuedFactionInequalityExpr" ):
                listener.enterContinuedFactionInequalityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinuedFactionInequalityExpr" ):
                listener.exitContinuedFactionInequalityExpr(self)




    def continuedFactionInequalityExpr(self):

        localctx = MatexParser.ContinuedFactionInequalityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_continuedFactionInequalityExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MatexParser.FUNC_FRAC)
            self.state = 181
            self.funcIneqParams()
            self.state = 182
            self.tailExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuedFactionSetExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_FRAC(self):
            return self.getToken(MatexParser.FUNC_FRAC, 0)

        def funcSetParams(self):
            return self.getTypedRuleContext(MatexParser.FuncSetParamsContext,0)


        def tailExpr(self):
            return self.getTypedRuleContext(MatexParser.TailExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_continuedFactionSetExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinuedFactionSetExpr" ):
                listener.enterContinuedFactionSetExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinuedFactionSetExpr" ):
                listener.exitContinuedFactionSetExpr(self)




    def continuedFactionSetExpr(self):

        localctx = MatexParser.ContinuedFactionSetExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_continuedFactionSetExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MatexParser.FUNC_FRAC)
            self.state = 185
            self.funcSetParams()
            self.state = 186
            self.tailExpr()
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
        self.enterRule(localctx, 16, self.RULE_summationExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MatexParser.FUNC_SUM)
            self.state = 189
            self.funcParams()
            self.state = 190
            self.tailExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummationInequalityExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_SUM(self):
            return self.getToken(MatexParser.FUNC_SUM, 0)

        def funcIneqParams(self):
            return self.getTypedRuleContext(MatexParser.FuncIneqParamsContext,0)


        def tailExpr(self):
            return self.getTypedRuleContext(MatexParser.TailExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_summationInequalityExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummationInequalityExpr" ):
                listener.enterSummationInequalityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummationInequalityExpr" ):
                listener.exitSummationInequalityExpr(self)




    def summationInequalityExpr(self):

        localctx = MatexParser.SummationInequalityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_summationInequalityExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(MatexParser.FUNC_SUM)
            self.state = 193
            self.funcIneqParams()
            self.state = 194
            self.tailExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummationSetExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_SUM(self):
            return self.getToken(MatexParser.FUNC_SUM, 0)

        def funcSetParams(self):
            return self.getTypedRuleContext(MatexParser.FuncSetParamsContext,0)


        def tailExpr(self):
            return self.getTypedRuleContext(MatexParser.TailExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_summationSetExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummationSetExpr" ):
                listener.enterSummationSetExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummationSetExpr" ):
                listener.exitSummationSetExpr(self)




    def summationSetExpr(self):

        localctx = MatexParser.SummationSetExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_summationSetExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MatexParser.FUNC_SUM)
            self.state = 197
            self.funcSetParams()
            self.state = 198
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
        self.enterRule(localctx, 22, self.RULE_productExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MatexParser.FUNC_PROD)
            self.state = 201
            self.funcParams()
            self.state = 202
            self.tailExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProductInequalityExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_PROD(self):
            return self.getToken(MatexParser.FUNC_PROD, 0)

        def funcIneqParams(self):
            return self.getTypedRuleContext(MatexParser.FuncIneqParamsContext,0)


        def tailExpr(self):
            return self.getTypedRuleContext(MatexParser.TailExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_productInequalityExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProductInequalityExpr" ):
                listener.enterProductInequalityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProductInequalityExpr" ):
                listener.exitProductInequalityExpr(self)




    def productInequalityExpr(self):

        localctx = MatexParser.ProductInequalityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_productInequalityExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MatexParser.FUNC_PROD)
            self.state = 205
            self.funcIneqParams()
            self.state = 206
            self.tailExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProductSetExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_PROD(self):
            return self.getToken(MatexParser.FUNC_PROD, 0)

        def funcSetParams(self):
            return self.getTypedRuleContext(MatexParser.FuncSetParamsContext,0)


        def tailExpr(self):
            return self.getTypedRuleContext(MatexParser.TailExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_productSetExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProductSetExpr" ):
                listener.enterProductSetExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProductSetExpr" ):
                listener.exitProductSetExpr(self)




    def productSetExpr(self):

        localctx = MatexParser.ProductSetExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_productSetExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MatexParser.FUNC_PROD)
            self.state = 209
            self.funcSetParams()
            self.state = 210
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
        self.enterRule(localctx, 28, self.RULE_tailExpr)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS, MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_FRAC, MatexParser.FUNC_INT, MatexParser.FUNC_SUM, MatexParser.FUNC_PROD, MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_ECOS, MatexParser.FUNC_ESIN, MatexParser.FUNC_EDELTAAMPLITUDE, MatexParser.FUNC_ARCECOS, MatexParser.FUNC_ARCESIN, MatexParser.FUNC_ARCEDELTAAMPLITUDE, MatexParser.FUNC_SQRT, MatexParser.FUNC_BINOMIAL, MatexParser.CMD_FRAC, MatexParser.NUMBER, MatexParser.DERIVATIVE, MatexParser.VARIABLE, MatexParser.MIXNUMBER, MatexParser.WORD, MatexParser.INFINITY, MatexParser.GREEKLETTER, MatexParser.LETTERFUNCTIONBRACE, MatexParser.LETTERFUNCTIONPAREN, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.expr()
                pass
            elif token in [MatexParser.L_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
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
        self.enterRule(localctx, 30, self.RULE_funcParams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.subeq()
            self.state = 217
            self.supexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncIneqParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subIneq(self):
            return self.getTypedRuleContext(MatexParser.SubIneqContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(MatexParser.SupexprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_funcIneqParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncIneqParams" ):
                listener.enterFuncIneqParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncIneqParams" ):
                listener.exitFuncIneqParams(self)




    def funcIneqParams(self):

        localctx = MatexParser.FuncIneqParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funcIneqParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.subIneq()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MatexParser.CARET:
                self.state = 220
                self.supexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncSetParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subSet(self):
            return self.getTypedRuleContext(MatexParser.SubSetContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(MatexParser.SupexprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_funcSetParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncSetParams" ):
                listener.enterFuncSetParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncSetParams" ):
                listener.exitFuncSetParams(self)




    def funcSetParams(self):

        localctx = MatexParser.FuncSetParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcSetParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.subSet()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MatexParser.CARET:
                self.state = 224
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_implicitMultiplicationExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.subtractionExpr(0)
            self.state = 229
            self.subtractionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.ImplicitMultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_implicitMultiplicationExpr)
                    self.state = 231
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 232
                    self.subtractionExpr(0) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_subtractionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.additionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.SubtractionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_subtractionExpr)
                    self.state = 241
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 242
                    self.match(MatexParser.MINUS)
                    self.state = 243
                    self.additionExpr(0) 
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_additionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.divisionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.AdditionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additionExpr)
                    self.state = 252
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 253
                    self.match(MatexParser.PLUS)
                    self.state = 254
                    self.divisionExpr(0) 
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_divisionExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.multiplicationExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.DivisionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_divisionExpr)
                    self.state = 263
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 264
                    _la = self._input.LA(1)
                    if not(_la==MatexParser.DIV or _la==MatexParser.CMD_DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 265
                    self.multiplicationExpr(0) 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_multiplicationExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                    self.state = 274
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 275
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MUL) | (1 << MatexParser.CMD_TIMES) | (1 << MatexParser.CMD_CDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 276
                    self.powExpr() 
                self.state = 281
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_fracExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(MatexParser.CMD_FRAC)
            self.state = 283
            self.bracedExpr()
            self.state = 284
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
        self.enterRule(localctx, 48, self.RULE_powExpr)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.signedAtom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.fracExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
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
        self.enterRule(localctx, 50, self.RULE_exponentiationExpr)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.signedAtom()
                self.state = 292
                self.match(MatexParser.CARET)
                self.state = 293
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.signedAtom()
                self.state = 296
                self.match(MatexParser.CARET)
                self.state = 297
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 299
                self.signedAtom()
                self.state = 300
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
        self.enterRule(localctx, 52, self.RULE_signedAtom)
        try:
            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.negateAtom()
                pass
            elif token in [MatexParser.DERIVATIVE, MatexParser.MIXNUMBER, MatexParser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.localMultiplication()
                pass
            elif token in [MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_ECOS, MatexParser.FUNC_ESIN, MatexParser.FUNC_EDELTAAMPLITUDE, MatexParser.FUNC_ARCECOS, MatexParser.FUNC_ARCESIN, MatexParser.FUNC_ARCEDELTAAMPLITUDE, MatexParser.FUNC_SQRT, MatexParser.LETTERFUNCTIONBRACE, MatexParser.LETTERFUNCTIONPAREN, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.func()
                pass
            elif token in [MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_BINOMIAL, MatexParser.NUMBER, MatexParser.VARIABLE, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
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
        self.enterRule(localctx, 54, self.RULE_negateAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(MatexParser.MINUS)
            self.state = 311
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
        self.enterRule(localctx, 56, self.RULE_localMultiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
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
        self.enterRule(localctx, 58, self.RULE_atom)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.indexedVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 318
                self.number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 319
                self.absolute()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 320
                self.exactDivision()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 321
                self.factorial()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 322
                self.binomial()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 323
                self.brackExpr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 324
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
        self.enterRule(localctx, 60, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
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
        self.enterRule(localctx, 62, self.RULE_indexedVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(MatexParser.VARIABLE)
            self.state = 330
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
        self.enterRule(localctx, 64, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
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
        self.enterRule(localctx, 66, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
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
        self.enterRule(localctx, 68, self.RULE_absolute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MatexParser.BAR)
            self.state = 337
            self.expr()
            self.state = 338
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
        self.enterRule(localctx, 70, self.RULE_exactDivision)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MatexParser.VARIABLE)
            self.state = 341
            self.match(MatexParser.BAR)
            self.state = 342
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
        self.enterRule(localctx, 72, self.RULE_factorial)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.parenExpr()
                self.state = 345
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.number()
                self.state = 348
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.variable()
                self.state = 351
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
        self.enterRule(localctx, 74, self.RULE_binomial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(MatexParser.FUNC_BINOMIAL)
            self.state = 356
            self.bracedExpr()
            self.state = 357
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


        def multiExpr(self):
            return self.getTypedRuleContext(MatexParser.MultiExprContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def LETTERFUNCTIONBRACE(self):
            return self.getToken(MatexParser.LETTERFUNCTIONBRACE, 0)

        def GREEKFUNCTIONBRACE(self):
            return self.getToken(MatexParser.GREEKFUNCTIONBRACE, 0)

        def R_PAREN(self):
            return self.getToken(MatexParser.R_PAREN, 0)

        def LETTERFUNCTIONPAREN(self):
            return self.getToken(MatexParser.LETTERFUNCTIONPAREN, 0)

        def GREEKFUNCTIONPAREN(self):
            return self.getToken(MatexParser.GREEKFUNCTIONPAREN, 0)

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
        self.enterRule(localctx, 76, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.funcname()
                self.state = 360
                self.bracedMultiExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.funcname()
                self.state = 363
                self.parenMultiExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 365
                _la = self._input.LA(1)
                if not(_la==MatexParser.LETTERFUNCTIONBRACE or _la==MatexParser.GREEKFUNCTIONBRACE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 366
                self.multiExpr(0)
                self.state = 367
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 369
                _la = self._input.LA(1)
                if not(_la==MatexParser.LETTERFUNCTIONPAREN or _la==MatexParser.GREEKFUNCTIONPAREN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 370
                self.multiExpr(0)
                self.state = 371
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
        self.enterRule(localctx, 78, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
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
        self.enterRule(localctx, 80, self.RULE_bracedMultiExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(MatexParser.L_BRACE)
            self.state = 378
            self.multiExpr(0)
            self.state = 379
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
        self.enterRule(localctx, 82, self.RULE_parenMultiExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(MatexParser.L_PAREN)
            self.state = 382
            self.multiExpr(0)
            self.state = 383
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

        def SEMICOLON(self):
            return self.getToken(MatexParser.SEMICOLON, 0)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_multiExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiExpr)
                    self.state = 388
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 389
                    _la = self._input.LA(1)
                    if not(_la==MatexParser.COMMA or _la==MatexParser.SEMICOLON):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 390
                    self.expr() 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_bracedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(MatexParser.L_BRACE)
            self.state = 397
            self.expr()
            self.state = 398
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
        self.enterRule(localctx, 88, self.RULE_brackExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(MatexParser.L_BRACKET)
            self.state = 401
            self.expr()
            self.state = 402
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
        self.enterRule(localctx, 90, self.RULE_parenExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(MatexParser.L_PAREN)
            self.state = 405
            self.expr()
            self.state = 406
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
        self.enterRule(localctx, 92, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MatexParser.UNDERSCORE)
            self.state = 409
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
        self.enterRule(localctx, 94, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(MatexParser.CARET)
            self.state = 412
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
        self.enterRule(localctx, 96, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(MatexParser.UNDERSCORE)
            self.state = 415
            self.match(MatexParser.L_BRACE)
            self.state = 416
            self.equality()
            self.state = 417
            self.match(MatexParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubIneqContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(MatexParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def inequality(self):
            return self.getTypedRuleContext(MatexParser.InequalityContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_subIneq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubIneq" ):
                listener.enterSubIneq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubIneq" ):
                listener.exitSubIneq(self)




    def subIneq(self):

        localctx = MatexParser.SubIneqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_subIneq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(MatexParser.UNDERSCORE)
            self.state = 420
            self.match(MatexParser.L_BRACE)
            self.state = 421
            self.inequality(0)
            self.state = 422
            self.match(MatexParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(MatexParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def setExpr(self):
            return self.getTypedRuleContext(MatexParser.SetExprContext,0)


        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MatexParser.RULE_subSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubSet" ):
                listener.enterSubSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubSet" ):
                listener.exitSubSet(self)




    def subSet(self):

        localctx = MatexParser.SubSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_subSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(MatexParser.UNDERSCORE)
            self.state = 425
            self.match(MatexParser.L_BRACE)
            self.state = 426
            self.setExpr()
            self.state = 427
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
        self.enterRule(localctx, 102, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.variable()
            self.state = 430
            self.match(MatexParser.EQ)
            self.state = 431
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InequalityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INEQUALITIES(self):
            return self.getToken(MatexParser.INEQUALITIES, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatexParser.VariableContext)
            else:
                return self.getTypedRuleContext(MatexParser.VariableContext,i)


        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatexParser.NumberContext)
            else:
                return self.getTypedRuleContext(MatexParser.NumberContext,i)


        def inequality(self):
            return self.getTypedRuleContext(MatexParser.InequalityContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_inequality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInequality" ):
                listener.enterInequality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInequality" ):
                listener.exitInequality(self)



    def inequality(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatexParser.InequalityContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_inequality, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.state = 434
                self.variable()
                pass
            elif token in [MatexParser.NUMBER]:
                self.state = 435
                self.number()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 438
            self.match(MatexParser.INEQUALITIES)
            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.state = 439
                self.variable()
                pass
            elif token in [MatexParser.NUMBER]:
                self.state = 440
                self.number()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 451
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.InequalityContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_inequality)
                    self.state = 443
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 444
                    self.match(MatexParser.INEQUALITIES)
                    self.state = 447
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                        self.state = 445
                        self.variable()
                        pass
                    elif token in [MatexParser.NUMBER]:
                        self.state = 446
                        self.number()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SetExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatexParser.VariableContext)
            else:
                return self.getTypedRuleContext(MatexParser.VariableContext,i)


        def SET_IN(self):
            return self.getToken(MatexParser.SET_IN, 0)

        def setDifferenceExpr(self):
            return self.getTypedRuleContext(MatexParser.SetDifferenceExprContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_setExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetExpr" ):
                listener.enterSetExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetExpr" ):
                listener.exitSetExpr(self)




    def setExpr(self):

        localctx = MatexParser.SetExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_setExpr)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.variable()
                self.state = 455
                self.match(MatexParser.SET_IN)
                self.state = 456
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.variable()
                self.state = 459
                self.match(MatexParser.SET_IN)
                self.state = 460
                self.setDifferenceExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetDifferenceExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatexParser.VariableContext)
            else:
                return self.getTypedRuleContext(MatexParser.VariableContext,i)


        def SET_DIFFERENCE(self):
            return self.getToken(MatexParser.SET_DIFFERENCE, 0)

        def L_BRACE(self):
            return self.getToken(MatexParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(MatexParser.R_BRACE, 0)

        def number(self):
            return self.getTypedRuleContext(MatexParser.NumberContext,0)


        def getRuleIndex(self):
            return MatexParser.RULE_setDifferenceExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetDifferenceExpr" ):
                listener.enterSetDifferenceExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetDifferenceExpr" ):
                listener.exitSetDifferenceExpr(self)




    def setDifferenceExpr(self):

        localctx = MatexParser.SetDifferenceExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_setDifferenceExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.variable()

            self.state = 465
            self.match(MatexParser.SET_DIFFERENCE)
            self.state = 466
            self.match(MatexParser.L_BRACE)
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.NUMBER]:
                self.state = 467
                self.number()
                pass
            elif token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.state = 468
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 471
            self.match(MatexParser.R_BRACE)
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
        self._predicates[18] = self.implicitMultiplicationExpr_sempred
        self._predicates[19] = self.subtractionExpr_sempred
        self._predicates[20] = self.additionExpr_sempred
        self._predicates[21] = self.divisionExpr_sempred
        self._predicates[22] = self.multiplicationExpr_sempred
        self._predicates[42] = self.multiExpr_sempred
        self._predicates[52] = self.inequality_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def megaExpr_sempred(self, localctx:MegaExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

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
         

    def inequality_sempred(self, localctx:InequalityContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         




