# Generated from .\pymatex\grammar\MatexParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u01a3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3\5\3i")
        buf.write("\n\3\3\3\3\3\3\3\3\3\5\3o\n\3\3\3\3\3\3\3\5\3t\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\177\n\3\f\3\16\3")
        buf.write("\u0082\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u008b\n\4")
        buf.write("\3\5\3\5\3\5\5\5\u0090\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00a0\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u00bc\n")
        buf.write("\r\3\16\3\16\3\16\3\17\3\17\5\17\u00c3\n\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\7\20\u00cb\n\20\f\20\16\20\u00ce")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00d6\n\21\f")
        buf.write("\21\16\21\u00d9\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7")
        buf.write("\22\u00e1\n\22\f\22\16\22\u00e4\13\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\7\23\u00ec\n\23\f\23\16\23\u00ef\13\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\7\24\u00f7\n\24\f\24\16\24")
        buf.write("\u00fa\13\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u0103")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u0110\n\27\3\30\3\30\3\30\3\30\5\30\u0116\n")
        buf.write("\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u0127\n\33\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0143\n\"")
        buf.write("\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\5$\u0157\n$\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(")
        buf.write("\3(\3(\3(\3(\7(\u0169\n(\f(\16(\u016c\13(\3)\3)\3)\3)")
        buf.write("\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\5\61\u0191\n\61\3\61\3\61\3\61\5\61\u0196\n\61\3\61\3")
        buf.write("\61\3\61\3\61\5\61\u019c\n\61\7\61\u019e\n\61\f\61\16")
        buf.write("\61\u01a1\13\61\3\61\2\n\4\36 \"$&N`\62\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`\2\t\4\2\6\6\67\67\4\2\5\5\65\66\4\2::<")
        buf.write("=\4\2;;BB\4\2CCEE\4\2DDFF\3\2\31\63\2\u01a3\2b\3\2\2\2")
        buf.write("\4s\3\2\2\2\6\u008a\3\2\2\2\b\u008f\3\2\2\2\n\u009f\3")
        buf.write("\2\2\2\f\u00a1\3\2\2\2\16\u00a5\3\2\2\2\20\u00a9\3\2\2")
        buf.write("\2\22\u00ad\3\2\2\2\24\u00b1\3\2\2\2\26\u00b5\3\2\2\2")
        buf.write("\30\u00bb\3\2\2\2\32\u00bd\3\2\2\2\34\u00c0\3\2\2\2\36")
        buf.write("\u00c4\3\2\2\2 \u00cf\3\2\2\2\"\u00da\3\2\2\2$\u00e5\3")
        buf.write("\2\2\2&\u00f0\3\2\2\2(\u00fb\3\2\2\2*\u0102\3\2\2\2,\u010f")
        buf.write("\3\2\2\2.\u0115\3\2\2\2\60\u0117\3\2\2\2\62\u011a\3\2")
        buf.write("\2\2\64\u0126\3\2\2\2\66\u0128\3\2\2\28\u012a\3\2\2\2")
        buf.write(":\u012d\3\2\2\2<\u012f\3\2\2\2>\u0131\3\2\2\2@\u0135\3")
        buf.write("\2\2\2B\u0142\3\2\2\2D\u0144\3\2\2\2F\u0156\3\2\2\2H\u0158")
        buf.write("\3\2\2\2J\u015a\3\2\2\2L\u015e\3\2\2\2N\u0162\3\2\2\2")
        buf.write("P\u016d\3\2\2\2R\u0171\3\2\2\2T\u0175\3\2\2\2V\u0179\3")
        buf.write("\2\2\2X\u017c\3\2\2\2Z\u017f\3\2\2\2\\\u0184\3\2\2\2^")
        buf.write("\u0189\3\2\2\2`\u018d\3\2\2\2bc\5\b\5\2cd\7\2\2\3d\3\3")
        buf.write("\2\2\2ef\b\3\1\2fh\5 \21\2gi\7\5\2\2hg\3\2\2\2hi\3\2\2")
        buf.write("\2ij\3\2\2\2jk\5\6\4\2kt\3\2\2\2ln\5\36\20\2mo\7\5\2\2")
        buf.write("nm\3\2\2\2no\3\2\2\2op\3\2\2\2pq\5\6\4\2qt\3\2\2\2rt\5")
        buf.write("\6\4\2se\3\2\2\2sl\3\2\2\2sr\3\2\2\2t\u0080\3\2\2\2uv")
        buf.write("\f\6\2\2vw\7\3\2\2w\177\5\6\4\2xy\f\5\2\2yz\7\4\2\2z\177")
        buf.write("\5\6\4\2{|\f\4\2\2|}\7\5\2\2}\177\5\6\4\2~u\3\2\2\2~x")
        buf.write("\3\2\2\2~{\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\5\3\2\2\2\u0082\u0080\3\2\2\2\u0083")
        buf.write("\u008b\5\n\6\2\u0084\u008b\5\f\7\2\u0085\u008b\5\16\b")
        buf.write("\2\u0086\u008b\5\20\t\2\u0087\u008b\5\22\n\2\u0088\u008b")
        buf.write("\5\24\13\2\u0089\u008b\5\26\f\2\u008a\u0083\3\2\2\2\u008a")
        buf.write("\u0084\3\2\2\2\u008a\u0085\3\2\2\2\u008a\u0086\3\2\2\2")
        buf.write("\u008a\u0087\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u0089\3")
        buf.write("\2\2\2\u008b\7\3\2\2\2\u008c\u0090\5 \21\2\u008d\u0090")
        buf.write("\5\36\20\2\u008e\u0090\5\4\3\2\u008f\u008c\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090\t\3\2\2\2\u0091")
        buf.write("\u0092\7\26\2\2\u0092\u0093\5V,\2\u0093\u0094\5X-\2\u0094")
        buf.write("\u0095\7\t\2\2\u0095\u0096\5\b\5\2\u0096\u0097\7:\2\2")
        buf.write("\u0097\u0098\7\n\2\2\u0098\u00a0\3\2\2\2\u0099\u009a\7")
        buf.write("\26\2\2\u009a\u009b\5V,\2\u009b\u009c\5X-\2\u009c\u009d")
        buf.write("\5\b\5\2\u009d\u009e\7:\2\2\u009e\u00a0\3\2\2\2\u009f")
        buf.write("\u0091\3\2\2\2\u009f\u0099\3\2\2\2\u00a0\13\3\2\2\2\u00a1")
        buf.write("\u00a2\7\25\2\2\u00a2\u00a3\5\32\16\2\u00a3\u00a4\5\30")
        buf.write("\r\2\u00a4\r\3\2\2\2\u00a5\u00a6\7\25\2\2\u00a6\u00a7")
        buf.write("\5\34\17\2\u00a7\u00a8\5\30\r\2\u00a8\17\3\2\2\2\u00a9")
        buf.write("\u00aa\7\27\2\2\u00aa\u00ab\5\32\16\2\u00ab\u00ac\5\30")
        buf.write("\r\2\u00ac\21\3\2\2\2\u00ad\u00ae\7\27\2\2\u00ae\u00af")
        buf.write("\5\34\17\2\u00af\u00b0\5\30\r\2\u00b0\23\3\2\2\2\u00b1")
        buf.write("\u00b2\7\30\2\2\u00b2\u00b3\5\32\16\2\u00b3\u00b4\5\30")
        buf.write("\r\2\u00b4\25\3\2\2\2\u00b5\u00b6\7\30\2\2\u00b6\u00b7")
        buf.write("\5\34\17\2\u00b7\u00b8\5\30\r\2\u00b8\27\3\2\2\2\u00b9")
        buf.write("\u00bc\5\b\5\2\u00ba\u00bc\5P)\2\u00bb\u00b9\3\2\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bc\31\3\2\2\2\u00bd\u00be\5Z.\2\u00be")
        buf.write("\u00bf\5X-\2\u00bf\33\3\2\2\2\u00c0\u00c2\5\\/\2\u00c1")
        buf.write("\u00c3\5X-\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\35\3\2\2\2\u00c4\u00c5\b\20\1\2\u00c5\u00c6\5 \21\2\u00c6")
        buf.write("\u00c7\5 \21\2\u00c7\u00cc\3\2\2\2\u00c8\u00c9\f\3\2\2")
        buf.write("\u00c9\u00cb\5 \21\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce\3")
        buf.write("\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\37")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\b\21\1\2\u00d0")
        buf.write("\u00d1\5\"\22\2\u00d1\u00d7\3\2\2\2\u00d2\u00d3\f\3\2")
        buf.write("\2\u00d3\u00d4\7\4\2\2\u00d4\u00d6\5\"\22\2\u00d5\u00d2")
        buf.write("\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8!\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da")
        buf.write("\u00db\b\22\1\2\u00db\u00dc\5$\23\2\u00dc\u00e2\3\2\2")
        buf.write("\2\u00dd\u00de\f\3\2\2\u00de\u00df\7\3\2\2\u00df\u00e1")
        buf.write("\5$\23\2\u00e0\u00dd\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3#\3\2\2\2\u00e4")
        buf.write("\u00e2\3\2\2\2\u00e5\u00e6\b\23\1\2\u00e6\u00e7\5&\24")
        buf.write("\2\u00e7\u00ed\3\2\2\2\u00e8\u00e9\f\3\2\2\u00e9\u00ea")
        buf.write("\t\2\2\2\u00ea\u00ec\5&\24\2\u00eb\u00e8\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee%\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\b\24\1")
        buf.write("\2\u00f1\u00f2\5*\26\2\u00f2\u00f8\3\2\2\2\u00f3\u00f4")
        buf.write("\f\3\2\2\u00f4\u00f5\t\3\2\2\u00f5\u00f7\5*\26\2\u00f6")
        buf.write("\u00f3\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\'\3\2\2\2\u00fa\u00f8\3\2\2")
        buf.write("\2\u00fb\u00fc\78\2\2\u00fc\u00fd\5P)\2\u00fd\u00fe\5")
        buf.write("P)\2\u00fe)\3\2\2\2\u00ff\u0103\5.\30\2\u0100\u0103\5")
        buf.write("(\25\2\u0101\u0103\5,\27\2\u0102\u00ff\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0102\u0101\3\2\2\2\u0103+\3\2\2\2\u0104\u0105")
        buf.write("\5.\30\2\u0105\u0106\7\21\2\2\u0106\u0107\5<\37\2\u0107")
        buf.write("\u0110\3\2\2\2\u0108\u0109\5.\30\2\u0109\u010a\7\21\2")
        buf.write("\2\u010a\u010b\5\66\34\2\u010b\u0110\3\2\2\2\u010c\u010d")
        buf.write("\5.\30\2\u010d\u010e\5X-\2\u010e\u0110\3\2\2\2\u010f\u0104")
        buf.write("\3\2\2\2\u010f\u0108\3\2\2\2\u010f\u010c\3\2\2\2\u0110")
        buf.write("-\3\2\2\2\u0111\u0116\5\60\31\2\u0112\u0116\5\62\32\2")
        buf.write("\u0113\u0116\5F$\2\u0114\u0116\5\64\33\2\u0115\u0111\3")
        buf.write("\2\2\2\u0115\u0112\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0114")
        buf.write("\3\2\2\2\u0116/\3\2\2\2\u0117\u0118\7\4\2\2\u0118\u0119")
        buf.write("\5.\30\2\u0119\61\3\2\2\2\u011a\u011b\t\4\2\2\u011b\63")
        buf.write("\3\2\2\2\u011c\u0127\5\66\34\2\u011d\u0127\58\35\2\u011e")
        buf.write("\u0127\5:\36\2\u011f\u0127\5<\37\2\u0120\u0127\5> \2\u0121")
        buf.write("\u0127\5@!\2\u0122\u0127\5B\"\2\u0123\u0127\5D#\2\u0124")
        buf.write("\u0127\5R*\2\u0125\u0127\5T+\2\u0126\u011c\3\2\2\2\u0126")
        buf.write("\u011d\3\2\2\2\u0126\u011e\3\2\2\2\u0126\u011f\3\2\2\2")
        buf.write("\u0126\u0120\3\2\2\2\u0126\u0121\3\2\2\2\u0126\u0122\3")
        buf.write("\2\2\2\u0126\u0123\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0125")
        buf.write("\3\2\2\2\u0127\65\3\2\2\2\u0128\u0129\t\5\2\2\u0129\67")
        buf.write("\3\2\2\2\u012a\u012b\7;\2\2\u012b\u012c\5V,\2\u012c9\3")
        buf.write("\2\2\2\u012d\u012e\7>\2\2\u012e;\3\2\2\2\u012f\u0130\7")
        buf.write("9\2\2\u0130=\3\2\2\2\u0131\u0132\7\17\2\2\u0132\u0133")
        buf.write("\5\b\5\2\u0133\u0134\7\17\2\2\u0134?\3\2\2\2\u0135\u0136")
        buf.write("\7;\2\2\u0136\u0137\7\17\2\2\u0137\u0138\7;\2\2\u0138")
        buf.write("A\3\2\2\2\u0139\u013a\5T+\2\u013a\u013b\7A\2\2\u013b\u0143")
        buf.write("\3\2\2\2\u013c\u013d\5<\37\2\u013d\u013e\7A\2\2\u013e")
        buf.write("\u0143\3\2\2\2\u013f\u0140\5\66\34\2\u0140\u0141\7A\2")
        buf.write("\2\u0141\u0143\3\2\2\2\u0142\u0139\3\2\2\2\u0142\u013c")
        buf.write("\3\2\2\2\u0142\u013f\3\2\2\2\u0143C\3\2\2\2\u0144\u0145")
        buf.write("\7\64\2\2\u0145\u0146\5P)\2\u0146\u0147\5P)\2\u0147E\3")
        buf.write("\2\2\2\u0148\u0149\5H%\2\u0149\u014a\5J&\2\u014a\u0157")
        buf.write("\3\2\2\2\u014b\u014c\5H%\2\u014c\u014d\5L\'\2\u014d\u0157")
        buf.write("\3\2\2\2\u014e\u014f\t\6\2\2\u014f\u0150\5N(\2\u0150\u0151")
        buf.write("\7\n\2\2\u0151\u0157\3\2\2\2\u0152\u0153\t\7\2\2\u0153")
        buf.write("\u0154\5N(\2\u0154\u0155\7\b\2\2\u0155\u0157\3\2\2\2\u0156")
        buf.write("\u0148\3\2\2\2\u0156\u014b\3\2\2\2\u0156\u014e\3\2\2\2")
        buf.write("\u0156\u0152\3\2\2\2\u0157G\3\2\2\2\u0158\u0159\t\b\2")
        buf.write("\2\u0159I\3\2\2\2\u015a\u015b\7\t\2\2\u015b\u015c\5N(")
        buf.write("\2\u015c\u015d\7\n\2\2\u015dK\3\2\2\2\u015e\u015f\7\7")
        buf.write("\2\2\u015f\u0160\5N(\2\u0160\u0161\7\b\2\2\u0161M\3\2")
        buf.write("\2\2\u0162\u0163\b(\1\2\u0163\u0164\5\b\5\2\u0164\u016a")
        buf.write("\3\2\2\2\u0165\u0166\f\3\2\2\u0166\u0167\7\r\2\2\u0167")
        buf.write("\u0169\5\b\5\2\u0168\u0165\3\2\2\2\u0169\u016c\3\2\2\2")
        buf.write("\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016bO\3\2\2")
        buf.write("\2\u016c\u016a\3\2\2\2\u016d\u016e\7\t\2\2\u016e\u016f")
        buf.write("\5\b\5\2\u016f\u0170\7\n\2\2\u0170Q\3\2\2\2\u0171\u0172")
        buf.write("\7\13\2\2\u0172\u0173\5\b\5\2\u0173\u0174\7\f\2\2\u0174")
        buf.write("S\3\2\2\2\u0175\u0176\7\7\2\2\u0176\u0177\5\b\5\2\u0177")
        buf.write("\u0178\7\b\2\2\u0178U\3\2\2\2\u0179\u017a\7\20\2\2\u017a")
        buf.write("\u017b\5P)\2\u017bW\3\2\2\2\u017c\u017d\7\21\2\2\u017d")
        buf.write("\u017e\5P)\2\u017eY\3\2\2\2\u017f\u0180\7\20\2\2\u0180")
        buf.write("\u0181\7\t\2\2\u0181\u0182\5^\60\2\u0182\u0183\7\n\2\2")
        buf.write("\u0183[\3\2\2\2\u0184\u0185\7\20\2\2\u0185\u0186\7\t\2")
        buf.write("\2\u0186\u0187\5`\61\2\u0187\u0188\7\n\2\2\u0188]\3\2")
        buf.write("\2\2\u0189\u018a\5\66\34\2\u018a\u018b\7?\2\2\u018b\u018c")
        buf.write("\5\b\5\2\u018c_\3\2\2\2\u018d\u0190\b\61\1\2\u018e\u0191")
        buf.write("\5\66\34\2\u018f\u0191\5<\37\2\u0190\u018e\3\2\2\2\u0190")
        buf.write("\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0195\7@\2\2")
        buf.write("\u0193\u0196\5\66\34\2\u0194\u0196\5<\37\2\u0195\u0193")
        buf.write("\3\2\2\2\u0195\u0194\3\2\2\2\u0196\u019f\3\2\2\2\u0197")
        buf.write("\u0198\f\3\2\2\u0198\u019b\7@\2\2\u0199\u019c\5\66\34")
        buf.write("\2\u019a\u019c\5<\37\2\u019b\u0199\3\2\2\2\u019b\u019a")
        buf.write("\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u0197\3\2\2\2\u019e")
        buf.write("\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0a\3\2\2\2\u01a1\u019f\3\2\2\2\34hns~\u0080\u008a")
        buf.write("\u008f\u009f\u00bb\u00c2\u00cc\u00d7\u00e2\u00ed\u00f8")
        buf.write("\u0102\u010f\u0115\u0126\u0142\u0156\u016a\u0190\u0195")
        buf.write("\u019b\u019f")
        return buf.getvalue()


class MatexParser ( Parser ):

    grammarFileName = "MatexParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "'.'", "'|'", "'_'", 
                     "'^'", "':'", "'\\lim'", "<INVALID>", "'K'", "'\\int'", 
                     "'\\sum'", "'\\prod'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\times'", "'\\cdot'", "'\\div'", "'\\frac'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\infty'", "'='", "<INVALID>", "'!'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "L_PAREN", 
                      "R_PAREN", "L_BRACE", "R_BRACE", "L_BRACKET", "R_BRACKET", 
                      "COMMA", "DOT", "BAR", "UNDERSCORE", "CARET", "COLON", 
                      "FUNC_LIM", "LIM_APPROACH_SYM", "FUNC_FRAC", "FUNC_INT", 
                      "FUNC_SUM", "FUNC_PROD", "FUNC_LOG", "FUNC_LN", "FUNC_SIN", 
                      "FUNC_COS", "FUNC_TAN", "FUNC_CSC", "FUNC_SEC", "FUNC_COT", 
                      "FUNC_ARCSIN", "FUNC_ARCCOS", "FUNC_ARCTAN", "FUNC_ARCCSC", 
                      "FUNC_ARCSEC", "FUNC_ARCCOT", "FUNC_SINH", "FUNC_COSH", 
                      "FUNC_TANH", "FUNC_ARCSINH", "FUNC_ARCCOSH", "FUNC_ARCTANH", 
                      "FUNC_ECOS", "FUNC_ESIN", "FUNC_EDELTAAMPLITUDE", 
                      "FUNC_ARCECOS", "FUNC_ARCESIN", "FUNC_ARCEDELTAAMPLITUDE", 
                      "FUNC_SQRT", "FUNC_BINOMIAL", "CMD_TIMES", "CMD_CDOT", 
                      "CMD_DIV", "CMD_FRAC", "NUMBER", "DERIVATIVE", "VARIABLE", 
                      "MIXNUMBER", "WORD", "INFINITY", "EQ", "INEQUALITIES", 
                      "BANG", "GREEKLETTER", "LETTERFUNCTIONBRACE", "LETTERFUNCTIONPAREN", 
                      "GREEKFUNCTIONBRACE", "GREEKFUNCTIONPAREN", "WS" ]

    RULE_math = 0
    RULE_megaExpr = 1
    RULE_specialExpr = 2
    RULE_expr = 3
    RULE_integralExpr = 4
    RULE_continuedFactionExpr = 5
    RULE_continuedFactionInequalityExpr = 6
    RULE_summationExpr = 7
    RULE_summationInequalityExpr = 8
    RULE_productExpr = 9
    RULE_productInequalityExpr = 10
    RULE_tailExpr = 11
    RULE_funcParams = 12
    RULE_funcIneqParams = 13
    RULE_implicitMultiplicationExpr = 14
    RULE_subtractionExpr = 15
    RULE_additionExpr = 16
    RULE_divisionExpr = 17
    RULE_multiplicationExpr = 18
    RULE_fracExpr = 19
    RULE_powExpr = 20
    RULE_exponentiationExpr = 21
    RULE_signedAtom = 22
    RULE_negateAtom = 23
    RULE_localMultiplication = 24
    RULE_atom = 25
    RULE_variable = 26
    RULE_indexedVariable = 27
    RULE_constant = 28
    RULE_number = 29
    RULE_absolute = 30
    RULE_exactDivision = 31
    RULE_factorial = 32
    RULE_binomial = 33
    RULE_func = 34
    RULE_funcname = 35
    RULE_bracedMultiExpr = 36
    RULE_parenMultiExpr = 37
    RULE_multiExpr = 38
    RULE_bracedExpr = 39
    RULE_brackExpr = 40
    RULE_parenExpr = 41
    RULE_subexpr = 42
    RULE_supexpr = 43
    RULE_subeq = 44
    RULE_subIneq = 45
    RULE_equality = 46
    RULE_inequality = 47

    ruleNames =  [ "math", "megaExpr", "specialExpr", "expr", "integralExpr", 
                   "continuedFactionExpr", "continuedFactionInequalityExpr", 
                   "summationExpr", "summationInequalityExpr", "productExpr", 
                   "productInequalityExpr", "tailExpr", "funcParams", "funcIneqParams", 
                   "implicitMultiplicationExpr", "subtractionExpr", "additionExpr", 
                   "divisionExpr", "multiplicationExpr", "fracExpr", "powExpr", 
                   "exponentiationExpr", "signedAtom", "negateAtom", "localMultiplication", 
                   "atom", "variable", "indexedVariable", "constant", "number", 
                   "absolute", "exactDivision", "factorial", "binomial", 
                   "func", "funcname", "bracedMultiExpr", "parenMultiExpr", 
                   "multiExpr", "bracedExpr", "brackExpr", "parenExpr", 
                   "subexpr", "supexpr", "subeq", "subIneq", "equality", 
                   "inequality" ]

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
    FUNC_FRAC=19
    FUNC_INT=20
    FUNC_SUM=21
    FUNC_PROD=22
    FUNC_LOG=23
    FUNC_LN=24
    FUNC_SIN=25
    FUNC_COS=26
    FUNC_TAN=27
    FUNC_CSC=28
    FUNC_SEC=29
    FUNC_COT=30
    FUNC_ARCSIN=31
    FUNC_ARCCOS=32
    FUNC_ARCTAN=33
    FUNC_ARCCSC=34
    FUNC_ARCSEC=35
    FUNC_ARCCOT=36
    FUNC_SINH=37
    FUNC_COSH=38
    FUNC_TANH=39
    FUNC_ARCSINH=40
    FUNC_ARCCOSH=41
    FUNC_ARCTANH=42
    FUNC_ECOS=43
    FUNC_ESIN=44
    FUNC_EDELTAAMPLITUDE=45
    FUNC_ARCECOS=46
    FUNC_ARCESIN=47
    FUNC_ARCEDELTAAMPLITUDE=48
    FUNC_SQRT=49
    FUNC_BINOMIAL=50
    CMD_TIMES=51
    CMD_CDOT=52
    CMD_DIV=53
    CMD_FRAC=54
    NUMBER=55
    DERIVATIVE=56
    VARIABLE=57
    MIXNUMBER=58
    WORD=59
    INFINITY=60
    EQ=61
    INEQUALITIES=62
    BANG=63
    GREEKLETTER=64
    LETTERFUNCTIONBRACE=65
    LETTERFUNCTIONPAREN=66
    GREEKFUNCTIONBRACE=67
    GREEKFUNCTIONPAREN=68
    WS=69

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
            self.state = 96
            self.expr()
            self.state = 97
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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 100
                self.subtractionExpr(0)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MatexParser.MUL:
                    self.state = 101
                    self.match(MatexParser.MUL)


                self.state = 104
                self.specialExpr()
                pass

            elif la_ == 2:
                self.state = 106
                self.implicitMultiplicationExpr(0)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MatexParser.MUL:
                    self.state = 107
                    self.match(MatexParser.MUL)


                self.state = 110
                self.specialExpr()
                pass

            elif la_ == 3:
                self.state = 112
                self.specialExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 124
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 115
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 116
                        self.match(MatexParser.PLUS)
                        self.state = 117
                        self.specialExpr()
                        pass

                    elif la_ == 2:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 118
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 119
                        self.match(MatexParser.MINUS)
                        self.state = 120
                        self.specialExpr()
                        pass

                    elif la_ == 3:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 121
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 122
                        self.match(MatexParser.MUL)
                        self.state = 123
                        self.specialExpr()
                        pass

             
                self.state = 128
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


        def summationExpr(self):
            return self.getTypedRuleContext(MatexParser.SummationExprContext,0)


        def summationInequalityExpr(self):
            return self.getTypedRuleContext(MatexParser.SummationInequalityExprContext,0)


        def productExpr(self):
            return self.getTypedRuleContext(MatexParser.ProductExprContext,0)


        def productInequalityExpr(self):
            return self.getTypedRuleContext(MatexParser.ProductInequalityExprContext,0)


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
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.integralExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.continuedFactionExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.continuedFactionInequalityExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.summationExpr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.summationInequalityExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.productExpr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 135
                self.productInequalityExpr()
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.subtractionExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.implicitMultiplicationExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(MatexParser.FUNC_INT)
                self.state = 144
                self.subexpr()
                self.state = 145
                self.supexpr()
                self.state = 146
                self.match(MatexParser.L_BRACE)
                self.state = 147
                self.expr()
                self.state = 148
                self.match(MatexParser.DERIVATIVE)
                self.state = 149
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(MatexParser.FUNC_INT)
                self.state = 152
                self.subexpr()
                self.state = 153
                self.supexpr()
                self.state = 154
                self.expr()
                self.state = 155
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
            self.state = 159
            self.match(MatexParser.FUNC_FRAC)
            self.state = 160
            self.funcParams()
            self.state = 161
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
            self.state = 163
            self.match(MatexParser.FUNC_FRAC)
            self.state = 164
            self.funcIneqParams()
            self.state = 165
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
        self.enterRule(localctx, 14, self.RULE_summationExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MatexParser.FUNC_SUM)
            self.state = 168
            self.funcParams()
            self.state = 169
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
        self.enterRule(localctx, 16, self.RULE_summationInequalityExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MatexParser.FUNC_SUM)
            self.state = 172
            self.funcIneqParams()
            self.state = 173
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
        self.enterRule(localctx, 18, self.RULE_productExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MatexParser.FUNC_PROD)
            self.state = 176
            self.funcParams()
            self.state = 177
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
        self.enterRule(localctx, 20, self.RULE_productInequalityExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(MatexParser.FUNC_PROD)
            self.state = 180
            self.funcIneqParams()
            self.state = 181
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
        self.enterRule(localctx, 22, self.RULE_tailExpr)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS, MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_FRAC, MatexParser.FUNC_INT, MatexParser.FUNC_SUM, MatexParser.FUNC_PROD, MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_ECOS, MatexParser.FUNC_ESIN, MatexParser.FUNC_EDELTAAMPLITUDE, MatexParser.FUNC_ARCECOS, MatexParser.FUNC_ARCESIN, MatexParser.FUNC_ARCEDELTAAMPLITUDE, MatexParser.FUNC_SQRT, MatexParser.FUNC_BINOMIAL, MatexParser.CMD_FRAC, MatexParser.NUMBER, MatexParser.DERIVATIVE, MatexParser.VARIABLE, MatexParser.MIXNUMBER, MatexParser.WORD, MatexParser.INFINITY, MatexParser.GREEKLETTER, MatexParser.LETTERFUNCTIONBRACE, MatexParser.LETTERFUNCTIONPAREN, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.expr()
                pass
            elif token in [MatexParser.L_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
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
        self.enterRule(localctx, 24, self.RULE_funcParams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.subeq()
            self.state = 188
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
        self.enterRule(localctx, 26, self.RULE_funcIneqParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.subIneq()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MatexParser.CARET:
                self.state = 191
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_implicitMultiplicationExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.subtractionExpr(0)
            self.state = 196
            self.subtractionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.ImplicitMultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_implicitMultiplicationExpr)
                    self.state = 198
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 199
                    self.subtractionExpr(0) 
                self.state = 204
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_subtractionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.additionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.SubtractionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_subtractionExpr)
                    self.state = 208
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 209
                    self.match(MatexParser.MINUS)
                    self.state = 210
                    self.additionExpr(0) 
                self.state = 215
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_additionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.divisionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.AdditionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additionExpr)
                    self.state = 219
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 220
                    self.match(MatexParser.PLUS)
                    self.state = 221
                    self.divisionExpr(0) 
                self.state = 226
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_divisionExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.multiplicationExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.DivisionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_divisionExpr)
                    self.state = 230
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 231
                    _la = self._input.LA(1)
                    if not(_la==MatexParser.DIV or _la==MatexParser.CMD_DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 232
                    self.multiplicationExpr(0) 
                self.state = 237
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_multiplicationExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                    self.state = 241
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 242
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MUL) | (1 << MatexParser.CMD_TIMES) | (1 << MatexParser.CMD_CDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 243
                    self.powExpr() 
                self.state = 248
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
        self.enterRule(localctx, 38, self.RULE_fracExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(MatexParser.CMD_FRAC)
            self.state = 250
            self.bracedExpr()
            self.state = 251
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
        self.enterRule(localctx, 40, self.RULE_powExpr)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.signedAtom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.fracExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
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
        self.enterRule(localctx, 42, self.RULE_exponentiationExpr)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.signedAtom()
                self.state = 259
                self.match(MatexParser.CARET)
                self.state = 260
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.signedAtom()
                self.state = 263
                self.match(MatexParser.CARET)
                self.state = 264
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.signedAtom()
                self.state = 267
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
        self.enterRule(localctx, 44, self.RULE_signedAtom)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.negateAtom()
                pass
            elif token in [MatexParser.DERIVATIVE, MatexParser.MIXNUMBER, MatexParser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.localMultiplication()
                pass
            elif token in [MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_ECOS, MatexParser.FUNC_ESIN, MatexParser.FUNC_EDELTAAMPLITUDE, MatexParser.FUNC_ARCECOS, MatexParser.FUNC_ARCESIN, MatexParser.FUNC_ARCEDELTAAMPLITUDE, MatexParser.FUNC_SQRT, MatexParser.LETTERFUNCTIONBRACE, MatexParser.LETTERFUNCTIONPAREN, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.func()
                pass
            elif token in [MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_BINOMIAL, MatexParser.NUMBER, MatexParser.VARIABLE, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 274
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
        self.enterRule(localctx, 46, self.RULE_negateAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MatexParser.MINUS)
            self.state = 278
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
        self.enterRule(localctx, 48, self.RULE_localMultiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
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
        self.enterRule(localctx, 50, self.RULE_atom)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.indexedVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 285
                self.number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 286
                self.absolute()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 287
                self.exactDivision()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 288
                self.factorial()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 289
                self.binomial()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 290
                self.brackExpr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 291
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
        self.enterRule(localctx, 52, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
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
        self.enterRule(localctx, 54, self.RULE_indexedVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(MatexParser.VARIABLE)
            self.state = 297
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
        self.enterRule(localctx, 56, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
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
        self.enterRule(localctx, 58, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
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
        self.enterRule(localctx, 60, self.RULE_absolute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MatexParser.BAR)
            self.state = 304
            self.expr()
            self.state = 305
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
        self.enterRule(localctx, 62, self.RULE_exactDivision)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(MatexParser.VARIABLE)
            self.state = 308
            self.match(MatexParser.BAR)
            self.state = 309
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
        self.enterRule(localctx, 64, self.RULE_factorial)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.parenExpr()
                self.state = 312
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.number()
                self.state = 315
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                self.variable()
                self.state = 318
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
        self.enterRule(localctx, 66, self.RULE_binomial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(MatexParser.FUNC_BINOMIAL)
            self.state = 323
            self.bracedExpr()
            self.state = 324
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
        self.enterRule(localctx, 68, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.funcname()
                self.state = 327
                self.bracedMultiExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.funcname()
                self.state = 330
                self.parenMultiExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                _la = self._input.LA(1)
                if not(_la==MatexParser.LETTERFUNCTIONBRACE or _la==MatexParser.GREEKFUNCTIONBRACE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 333
                self.multiExpr(0)
                self.state = 334
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 336
                _la = self._input.LA(1)
                if not(_la==MatexParser.LETTERFUNCTIONPAREN or _la==MatexParser.GREEKFUNCTIONPAREN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 337
                self.multiExpr(0)
                self.state = 338
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
        self.enterRule(localctx, 70, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
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
        self.enterRule(localctx, 72, self.RULE_bracedMultiExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MatexParser.L_BRACE)
            self.state = 345
            self.multiExpr(0)
            self.state = 346
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
        self.enterRule(localctx, 74, self.RULE_parenMultiExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(MatexParser.L_PAREN)
            self.state = 349
            self.multiExpr(0)
            self.state = 350
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_multiExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiExpr)
                    self.state = 355
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 356
                    self.match(MatexParser.COMMA)
                    self.state = 357
                    self.expr() 
                self.state = 362
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
        self.enterRule(localctx, 78, self.RULE_bracedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(MatexParser.L_BRACE)
            self.state = 364
            self.expr()
            self.state = 365
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
        self.enterRule(localctx, 80, self.RULE_brackExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(MatexParser.L_BRACKET)
            self.state = 368
            self.expr()
            self.state = 369
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
        self.enterRule(localctx, 82, self.RULE_parenExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(MatexParser.L_PAREN)
            self.state = 372
            self.expr()
            self.state = 373
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
        self.enterRule(localctx, 84, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(MatexParser.UNDERSCORE)
            self.state = 376
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
        self.enterRule(localctx, 86, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(MatexParser.CARET)
            self.state = 379
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
        self.enterRule(localctx, 88, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(MatexParser.UNDERSCORE)
            self.state = 382
            self.match(MatexParser.L_BRACE)
            self.state = 383
            self.equality()
            self.state = 384
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
        self.enterRule(localctx, 90, self.RULE_subIneq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(MatexParser.UNDERSCORE)
            self.state = 387
            self.match(MatexParser.L_BRACE)
            self.state = 388
            self.inequality(0)
            self.state = 389
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
        self.enterRule(localctx, 92, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.variable()
            self.state = 392
            self.match(MatexParser.EQ)
            self.state = 393
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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_inequality, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.state = 396
                self.variable()
                pass
            elif token in [MatexParser.NUMBER]:
                self.state = 397
                self.number()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 400
            self.match(MatexParser.INEQUALITIES)
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.state = 401
                self.variable()
                pass
            elif token in [MatexParser.NUMBER]:
                self.state = 402
                self.number()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.InequalityContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_inequality)
                    self.state = 405
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 406
                    self.match(MatexParser.INEQUALITIES)
                    self.state = 409
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                        self.state = 407
                        self.variable()
                        pass
                    elif token in [MatexParser.NUMBER]:
                        self.state = 408
                        self.number()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.megaExpr_sempred
        self._predicates[14] = self.implicitMultiplicationExpr_sempred
        self._predicates[15] = self.subtractionExpr_sempred
        self._predicates[16] = self.additionExpr_sempred
        self._predicates[17] = self.divisionExpr_sempred
        self._predicates[18] = self.multiplicationExpr_sempred
        self._predicates[38] = self.multiExpr_sempred
        self._predicates[47] = self.inequality_sempred
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
         




