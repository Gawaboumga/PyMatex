# Generated from .\pymatex\grammar\MatexParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u0195\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\3\2\3\2\3\3\3\3\3\3\5\3e\n\3\5\3g\n\3\3\3\3\3")
        buf.write("\3\3\5\3l\n\3\3\3\3\3\5\3p\n\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\7\3{\n\3\f\3\16\3~\13\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u0085\n\4\3\5\3\5\3\5\5\5\u008a\n\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u009a")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\5\13\u00ae\n\13\3\f\3\f\3\f\3")
        buf.write("\r\3\r\5\r\u00b5\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16")
        buf.write("\u00bd\n\16\f\16\16\16\u00c0\13\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00c8\n\17\f\17\16\17\u00cb\13\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\7\20\u00d3\n\20\f\20\16\20\u00d6")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00de\n\21\f")
        buf.write("\21\16\21\u00e1\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7")
        buf.write("\22\u00e9\n\22\f\22\16\22\u00ec\13\22\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\5\24\u00f5\n\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0102\n\25\3")
        buf.write("\26\3\26\3\26\3\26\5\26\u0108\n\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0119\n\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3")
        buf.write("\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \5 \u0135\n \3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0149")
        buf.write("\n\"\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\7")
        buf.write("&\u015b\n&\f&\16&\u015e\13&\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3/\3/\3/\5/\u0183\n/\3/\3/\3/\5/\u0188")
        buf.write("\n/\3/\3/\3/\3/\5/\u018e\n/\7/\u0190\n/\f/\16/\u0193\13")
        buf.write("/\3/\2\n\4\32\34\36 \"J\\\60\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("\2\t\4\2\6\6\66\66\4\2\5\5\64\65\4\299;<\4\2::AA\4\2B")
        buf.write("BDD\4\2CCEE\3\2\30\62\2\u0195\2^\3\2\2\2\4o\3\2\2\2\6")
        buf.write("\u0084\3\2\2\2\b\u0089\3\2\2\2\n\u0099\3\2\2\2\f\u009b")
        buf.write("\3\2\2\2\16\u009f\3\2\2\2\20\u00a3\3\2\2\2\22\u00a7\3")
        buf.write("\2\2\2\24\u00ad\3\2\2\2\26\u00af\3\2\2\2\30\u00b2\3\2")
        buf.write("\2\2\32\u00b6\3\2\2\2\34\u00c1\3\2\2\2\36\u00cc\3\2\2")
        buf.write("\2 \u00d7\3\2\2\2\"\u00e2\3\2\2\2$\u00ed\3\2\2\2&\u00f4")
        buf.write("\3\2\2\2(\u0101\3\2\2\2*\u0107\3\2\2\2,\u0109\3\2\2\2")
        buf.write(".\u010c\3\2\2\2\60\u0118\3\2\2\2\62\u011a\3\2\2\2\64\u011c")
        buf.write("\3\2\2\2\66\u011f\3\2\2\28\u0121\3\2\2\2:\u0123\3\2\2")
        buf.write("\2<\u0127\3\2\2\2>\u0134\3\2\2\2@\u0136\3\2\2\2B\u0148")
        buf.write("\3\2\2\2D\u014a\3\2\2\2F\u014c\3\2\2\2H\u0150\3\2\2\2")
        buf.write("J\u0154\3\2\2\2L\u015f\3\2\2\2N\u0163\3\2\2\2P\u0167\3")
        buf.write("\2\2\2R\u016b\3\2\2\2T\u016e\3\2\2\2V\u0171\3\2\2\2X\u0176")
        buf.write("\3\2\2\2Z\u017b\3\2\2\2\\\u017f\3\2\2\2^_\5\b\5\2_`\7")
        buf.write("\2\2\3`\3\3\2\2\2af\b\3\1\2bd\5\34\17\2ce\7\5\2\2dc\3")
        buf.write("\2\2\2de\3\2\2\2eg\3\2\2\2fb\3\2\2\2fg\3\2\2\2gh\3\2\2")
        buf.write("\2hp\5\6\4\2ik\5\32\16\2jl\7\5\2\2kj\3\2\2\2kl\3\2\2\2")
        buf.write("lm\3\2\2\2mn\5\6\4\2np\3\2\2\2oa\3\2\2\2oi\3\2\2\2p|\3")
        buf.write("\2\2\2qr\f\5\2\2rs\7\3\2\2s{\5\6\4\2tu\f\4\2\2uv\7\4\2")
        buf.write("\2v{\5\6\4\2wx\f\3\2\2xy\7\5\2\2y{\5\6\4\2zq\3\2\2\2z")
        buf.write("t\3\2\2\2zw\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\5\3")
        buf.write("\2\2\2~|\3\2\2\2\177\u0085\5\n\6\2\u0080\u0085\5\f\7\2")
        buf.write("\u0081\u0085\5\16\b\2\u0082\u0085\5\20\t\2\u0083\u0085")
        buf.write("\5\22\n\2\u0084\177\3\2\2\2\u0084\u0080\3\2\2\2\u0084")
        buf.write("\u0081\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2")
        buf.write("\u0085\7\3\2\2\2\u0086\u008a\5\34\17\2\u0087\u008a\5\32")
        buf.write("\16\2\u0088\u008a\5\4\3\2\u0089\u0086\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u0089\u0088\3\2\2\2\u008a\t\3\2\2\2\u008b\u008c")
        buf.write("\7\25\2\2\u008c\u008d\5R*\2\u008d\u008e\5T+\2\u008e\u008f")
        buf.write("\7\t\2\2\u008f\u0090\5\b\5\2\u0090\u0091\79\2\2\u0091")
        buf.write("\u0092\7\n\2\2\u0092\u009a\3\2\2\2\u0093\u0094\7\25\2")
        buf.write("\2\u0094\u0095\5R*\2\u0095\u0096\5T+\2\u0096\u0097\5\b")
        buf.write("\5\2\u0097\u0098\79\2\2\u0098\u009a\3\2\2\2\u0099\u008b")
        buf.write("\3\2\2\2\u0099\u0093\3\2\2\2\u009a\13\3\2\2\2\u009b\u009c")
        buf.write("\7\26\2\2\u009c\u009d\5\26\f\2\u009d\u009e\5\24\13\2\u009e")
        buf.write("\r\3\2\2\2\u009f\u00a0\7\26\2\2\u00a0\u00a1\5\30\r\2\u00a1")
        buf.write("\u00a2\5\24\13\2\u00a2\17\3\2\2\2\u00a3\u00a4\7\27\2\2")
        buf.write("\u00a4\u00a5\5\26\f\2\u00a5\u00a6\5\24\13\2\u00a6\21\3")
        buf.write("\2\2\2\u00a7\u00a8\7\27\2\2\u00a8\u00a9\5\30\r\2\u00a9")
        buf.write("\u00aa\5\24\13\2\u00aa\23\3\2\2\2\u00ab\u00ae\5\b\5\2")
        buf.write("\u00ac\u00ae\5L\'\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3")
        buf.write("\2\2\2\u00ae\25\3\2\2\2\u00af\u00b0\5V,\2\u00b0\u00b1")
        buf.write("\5T+\2\u00b1\27\3\2\2\2\u00b2\u00b4\5X-\2\u00b3\u00b5")
        buf.write("\5T+\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\31")
        buf.write("\3\2\2\2\u00b6\u00b7\b\16\1\2\u00b7\u00b8\5\34\17\2\u00b8")
        buf.write("\u00b9\5\34\17\2\u00b9\u00be\3\2\2\2\u00ba\u00bb\f\3\2")
        buf.write("\2\u00bb\u00bd\5\34\17\2\u00bc\u00ba\3\2\2\2\u00bd\u00c0")
        buf.write("\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\33\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c2\b\17\1\2\u00c2")
        buf.write("\u00c3\5\36\20\2\u00c3\u00c9\3\2\2\2\u00c4\u00c5\f\3\2")
        buf.write("\2\u00c5\u00c6\7\4\2\2\u00c6\u00c8\5\36\20\2\u00c7\u00c4")
        buf.write("\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\35\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc")
        buf.write("\u00cd\b\20\1\2\u00cd\u00ce\5 \21\2\u00ce\u00d4\3\2\2")
        buf.write("\2\u00cf\u00d0\f\3\2\2\u00d0\u00d1\7\3\2\2\u00d1\u00d3")
        buf.write("\5 \21\2\u00d2\u00cf\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\37\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d7\u00d8\b\21\1\2\u00d8\u00d9\5\"\22")
        buf.write("\2\u00d9\u00df\3\2\2\2\u00da\u00db\f\3\2\2\u00db\u00dc")
        buf.write("\t\2\2\2\u00dc\u00de\5\"\22\2\u00dd\u00da\3\2\2\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0!\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\b\22\1")
        buf.write("\2\u00e3\u00e4\5&\24\2\u00e4\u00ea\3\2\2\2\u00e5\u00e6")
        buf.write("\f\3\2\2\u00e6\u00e7\t\3\2\2\u00e7\u00e9\5&\24\2\u00e8")
        buf.write("\u00e5\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb#\3\2\2\2\u00ec\u00ea\3\2\2")
        buf.write("\2\u00ed\u00ee\7\67\2\2\u00ee\u00ef\5L\'\2\u00ef\u00f0")
        buf.write("\5L\'\2\u00f0%\3\2\2\2\u00f1\u00f5\5*\26\2\u00f2\u00f5")
        buf.write("\5$\23\2\u00f3\u00f5\5(\25\2\u00f4\u00f1\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\'\3\2\2\2\u00f6")
        buf.write("\u00f7\5*\26\2\u00f7\u00f8\7\21\2\2\u00f8\u00f9\58\35")
        buf.write("\2\u00f9\u0102\3\2\2\2\u00fa\u00fb\5*\26\2\u00fb\u00fc")
        buf.write("\7\21\2\2\u00fc\u00fd\5\62\32\2\u00fd\u0102\3\2\2\2\u00fe")
        buf.write("\u00ff\5*\26\2\u00ff\u0100\5T+\2\u0100\u0102\3\2\2\2\u0101")
        buf.write("\u00f6\3\2\2\2\u0101\u00fa\3\2\2\2\u0101\u00fe\3\2\2\2")
        buf.write("\u0102)\3\2\2\2\u0103\u0108\5,\27\2\u0104\u0108\5.\30")
        buf.write("\2\u0105\u0108\5B\"\2\u0106\u0108\5\60\31\2\u0107\u0103")
        buf.write("\3\2\2\2\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2\u0107")
        buf.write("\u0106\3\2\2\2\u0108+\3\2\2\2\u0109\u010a\7\4\2\2\u010a")
        buf.write("\u010b\5*\26\2\u010b-\3\2\2\2\u010c\u010d\t\4\2\2\u010d")
        buf.write("/\3\2\2\2\u010e\u0119\5\62\32\2\u010f\u0119\5\64\33\2")
        buf.write("\u0110\u0119\5\66\34\2\u0111\u0119\58\35\2\u0112\u0119")
        buf.write("\5:\36\2\u0113\u0119\5<\37\2\u0114\u0119\5> \2\u0115\u0119")
        buf.write("\5@!\2\u0116\u0119\5N(\2\u0117\u0119\5P)\2\u0118\u010e")
        buf.write("\3\2\2\2\u0118\u010f\3\2\2\2\u0118\u0110\3\2\2\2\u0118")
        buf.write("\u0111\3\2\2\2\u0118\u0112\3\2\2\2\u0118\u0113\3\2\2\2")
        buf.write("\u0118\u0114\3\2\2\2\u0118\u0115\3\2\2\2\u0118\u0116\3")
        buf.write("\2\2\2\u0118\u0117\3\2\2\2\u0119\61\3\2\2\2\u011a\u011b")
        buf.write("\t\5\2\2\u011b\63\3\2\2\2\u011c\u011d\7:\2\2\u011d\u011e")
        buf.write("\5R*\2\u011e\65\3\2\2\2\u011f\u0120\7=\2\2\u0120\67\3")
        buf.write("\2\2\2\u0121\u0122\78\2\2\u01229\3\2\2\2\u0123\u0124\7")
        buf.write("\17\2\2\u0124\u0125\5\b\5\2\u0125\u0126\7\17\2\2\u0126")
        buf.write(";\3\2\2\2\u0127\u0128\7:\2\2\u0128\u0129\7\17\2\2\u0129")
        buf.write("\u012a\7:\2\2\u012a=\3\2\2\2\u012b\u012c\5P)\2\u012c\u012d")
        buf.write("\7@\2\2\u012d\u0135\3\2\2\2\u012e\u012f\58\35\2\u012f")
        buf.write("\u0130\7@\2\2\u0130\u0135\3\2\2\2\u0131\u0132\5\62\32")
        buf.write("\2\u0132\u0133\7@\2\2\u0133\u0135\3\2\2\2\u0134\u012b")
        buf.write("\3\2\2\2\u0134\u012e\3\2\2\2\u0134\u0131\3\2\2\2\u0135")
        buf.write("?\3\2\2\2\u0136\u0137\7\63\2\2\u0137\u0138\5L\'\2\u0138")
        buf.write("\u0139\5L\'\2\u0139A\3\2\2\2\u013a\u013b\5D#\2\u013b\u013c")
        buf.write("\5F$\2\u013c\u0149\3\2\2\2\u013d\u013e\5D#\2\u013e\u013f")
        buf.write("\5H%\2\u013f\u0149\3\2\2\2\u0140\u0141\t\6\2\2\u0141\u0142")
        buf.write("\5J&\2\u0142\u0143\7\n\2\2\u0143\u0149\3\2\2\2\u0144\u0145")
        buf.write("\t\7\2\2\u0145\u0146\5J&\2\u0146\u0147\7\b\2\2\u0147\u0149")
        buf.write("\3\2\2\2\u0148\u013a\3\2\2\2\u0148\u013d\3\2\2\2\u0148")
        buf.write("\u0140\3\2\2\2\u0148\u0144\3\2\2\2\u0149C\3\2\2\2\u014a")
        buf.write("\u014b\t\b\2\2\u014bE\3\2\2\2\u014c\u014d\7\t\2\2\u014d")
        buf.write("\u014e\5J&\2\u014e\u014f\7\n\2\2\u014fG\3\2\2\2\u0150")
        buf.write("\u0151\7\7\2\2\u0151\u0152\5J&\2\u0152\u0153\7\b\2\2\u0153")
        buf.write("I\3\2\2\2\u0154\u0155\b&\1\2\u0155\u0156\5\b\5\2\u0156")
        buf.write("\u015c\3\2\2\2\u0157\u0158\f\3\2\2\u0158\u0159\7\r\2\2")
        buf.write("\u0159\u015b\5\b\5\2\u015a\u0157\3\2\2\2\u015b\u015e\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015dK")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\7\t\2\2\u0160")
        buf.write("\u0161\5\b\5\2\u0161\u0162\7\n\2\2\u0162M\3\2\2\2\u0163")
        buf.write("\u0164\7\13\2\2\u0164\u0165\5\b\5\2\u0165\u0166\7\f\2")
        buf.write("\2\u0166O\3\2\2\2\u0167\u0168\7\7\2\2\u0168\u0169\5\b")
        buf.write("\5\2\u0169\u016a\7\b\2\2\u016aQ\3\2\2\2\u016b\u016c\7")
        buf.write("\20\2\2\u016c\u016d\5L\'\2\u016dS\3\2\2\2\u016e\u016f")
        buf.write("\7\21\2\2\u016f\u0170\5L\'\2\u0170U\3\2\2\2\u0171\u0172")
        buf.write("\7\20\2\2\u0172\u0173\7\t\2\2\u0173\u0174\5Z.\2\u0174")
        buf.write("\u0175\7\n\2\2\u0175W\3\2\2\2\u0176\u0177\7\20\2\2\u0177")
        buf.write("\u0178\7\t\2\2\u0178\u0179\5\\/\2\u0179\u017a\7\n\2\2")
        buf.write("\u017aY\3\2\2\2\u017b\u017c\5\62\32\2\u017c\u017d\7>\2")
        buf.write("\2\u017d\u017e\5\b\5\2\u017e[\3\2\2\2\u017f\u0182\b/\1")
        buf.write("\2\u0180\u0183\5\62\32\2\u0181\u0183\58\35\2\u0182\u0180")
        buf.write("\3\2\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0187\7?\2\2\u0185\u0188\5\62\32\2\u0186\u0188\58\35")
        buf.write("\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188\u0191")
        buf.write("\3\2\2\2\u0189\u018a\f\3\2\2\u018a\u018d\7?\2\2\u018b")
        buf.write("\u018e\5\62\32\2\u018c\u018e\58\35\2\u018d\u018b\3\2\2")
        buf.write("\2\u018d\u018c\3\2\2\2\u018e\u0190\3\2\2\2\u018f\u0189")
        buf.write("\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192]\3\2\2\2\u0193\u0191\3\2\2\2\35d")
        buf.write("fkoz|\u0084\u0089\u0099\u00ad\u00b4\u00be\u00c9\u00d4")
        buf.write("\u00df\u00ea\u00f4\u0101\u0107\u0118\u0134\u0148\u015c")
        buf.write("\u0182\u0187\u018d\u0191")
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
                     "<INVALID>", "'\\infty'", "'='", "<INVALID>", "'!'" ]

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
                      "WORD", "INFINITY", "EQ", "INEQUALITIES", "BANG", 
                      "GREEKLETTER", "LETTERFUNCTIONBRACE", "LETTERFUNCTIONPAREN", 
                      "GREEKFUNCTIONBRACE", "GREEKFUNCTIONPAREN", "WS" ]

    RULE_math = 0
    RULE_megaExpr = 1
    RULE_specialExpr = 2
    RULE_expr = 3
    RULE_integralExpr = 4
    RULE_summationExpr = 5
    RULE_summationInequalityExpr = 6
    RULE_productExpr = 7
    RULE_productInequalityExpr = 8
    RULE_tailExpr = 9
    RULE_funcParams = 10
    RULE_funcIneqParams = 11
    RULE_implicitMultiplicationExpr = 12
    RULE_subtractionExpr = 13
    RULE_additionExpr = 14
    RULE_divisionExpr = 15
    RULE_multiplicationExpr = 16
    RULE_fracExpr = 17
    RULE_powExpr = 18
    RULE_exponentiationExpr = 19
    RULE_signedAtom = 20
    RULE_negateAtom = 21
    RULE_localMultiplication = 22
    RULE_atom = 23
    RULE_variable = 24
    RULE_indexedVariable = 25
    RULE_constant = 26
    RULE_number = 27
    RULE_absolute = 28
    RULE_exactDivision = 29
    RULE_factorial = 30
    RULE_binomial = 31
    RULE_func = 32
    RULE_funcname = 33
    RULE_bracedMultiExpr = 34
    RULE_parenMultiExpr = 35
    RULE_multiExpr = 36
    RULE_bracedExpr = 37
    RULE_brackExpr = 38
    RULE_parenExpr = 39
    RULE_subexpr = 40
    RULE_supexpr = 41
    RULE_subeq = 42
    RULE_subIneq = 43
    RULE_equality = 44
    RULE_inequality = 45

    ruleNames =  [ "math", "megaExpr", "specialExpr", "expr", "integralExpr", 
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
    INEQUALITIES=61
    BANG=62
    GREEKLETTER=63
    LETTERFUNCTIONBRACE=64
    LETTERFUNCTIONPAREN=65
    GREEKFUNCTIONBRACE=66
    GREEKFUNCTIONPAREN=67
    WS=68

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
            self.state = 92
            self.expr()
            self.state = 93
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
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MINUS) | (1 << MatexParser.L_PAREN) | (1 << MatexParser.L_BRACKET) | (1 << MatexParser.BAR) | (1 << MatexParser.FUNC_LOG) | (1 << MatexParser.FUNC_LN) | (1 << MatexParser.FUNC_SIN) | (1 << MatexParser.FUNC_COS) | (1 << MatexParser.FUNC_TAN) | (1 << MatexParser.FUNC_CSC) | (1 << MatexParser.FUNC_SEC) | (1 << MatexParser.FUNC_COT) | (1 << MatexParser.FUNC_ARCSIN) | (1 << MatexParser.FUNC_ARCCOS) | (1 << MatexParser.FUNC_ARCTAN) | (1 << MatexParser.FUNC_ARCCSC) | (1 << MatexParser.FUNC_ARCSEC) | (1 << MatexParser.FUNC_ARCCOT) | (1 << MatexParser.FUNC_SINH) | (1 << MatexParser.FUNC_COSH) | (1 << MatexParser.FUNC_TANH) | (1 << MatexParser.FUNC_ARCSINH) | (1 << MatexParser.FUNC_ARCCOSH) | (1 << MatexParser.FUNC_ARCTANH) | (1 << MatexParser.FUNC_ECOS) | (1 << MatexParser.FUNC_ESIN) | (1 << MatexParser.FUNC_EDELTAAMPLITUDE) | (1 << MatexParser.FUNC_ARCECOS) | (1 << MatexParser.FUNC_ARCESIN) | (1 << MatexParser.FUNC_ARCEDELTAAMPLITUDE) | (1 << MatexParser.FUNC_SQRT) | (1 << MatexParser.FUNC_BINOMIAL) | (1 << MatexParser.CMD_FRAC) | (1 << MatexParser.NUMBER) | (1 << MatexParser.DERIVATIVE) | (1 << MatexParser.VARIABLE) | (1 << MatexParser.MIXNUMBER) | (1 << MatexParser.WORD) | (1 << MatexParser.INFINITY) | (1 << MatexParser.GREEKLETTER))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MatexParser.LETTERFUNCTIONBRACE - 64)) | (1 << (MatexParser.LETTERFUNCTIONPAREN - 64)) | (1 << (MatexParser.GREEKFUNCTIONBRACE - 64)) | (1 << (MatexParser.GREEKFUNCTIONPAREN - 64)))) != 0):
                    self.state = 96
                    self.subtractionExpr(0)
                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MatexParser.MUL:
                        self.state = 97
                        self.match(MatexParser.MUL)




                self.state = 102
                self.specialExpr()
                pass

            elif la_ == 2:
                self.state = 103
                self.implicitMultiplicationExpr(0)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MatexParser.MUL:
                    self.state = 104
                    self.match(MatexParser.MUL)


                self.state = 107
                self.specialExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 120
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 111
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 112
                        self.match(MatexParser.PLUS)
                        self.state = 113
                        self.specialExpr()
                        pass

                    elif la_ == 2:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 114
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 115
                        self.match(MatexParser.MINUS)
                        self.state = 116
                        self.specialExpr()
                        pass

                    elif la_ == 3:
                        localctx = MatexParser.MegaExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_megaExpr)
                        self.state = 117
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 118
                        self.match(MatexParser.MUL)
                        self.state = 119
                        self.specialExpr()
                        pass

             
                self.state = 124
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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.integralExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.summationExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.summationInequalityExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.productExpr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.subtractionExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.implicitMultiplicationExpr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
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
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(MatexParser.FUNC_INT)
                self.state = 138
                self.subexpr()
                self.state = 139
                self.supexpr()
                self.state = 140
                self.match(MatexParser.L_BRACE)
                self.state = 141
                self.expr()
                self.state = 142
                self.match(MatexParser.DERIVATIVE)
                self.state = 143
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(MatexParser.FUNC_INT)
                self.state = 146
                self.subexpr()
                self.state = 147
                self.supexpr()
                self.state = 148
                self.expr()
                self.state = 149
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
            self.state = 153
            self.match(MatexParser.FUNC_SUM)
            self.state = 154
            self.funcParams()
            self.state = 155
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
        self.enterRule(localctx, 12, self.RULE_summationInequalityExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(MatexParser.FUNC_SUM)
            self.state = 158
            self.funcIneqParams()
            self.state = 159
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
            self.state = 161
            self.match(MatexParser.FUNC_PROD)
            self.state = 162
            self.funcParams()
            self.state = 163
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
        self.enterRule(localctx, 16, self.RULE_productInequalityExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MatexParser.FUNC_PROD)
            self.state = 166
            self.funcIneqParams()
            self.state = 167
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
        self.enterRule(localctx, 18, self.RULE_tailExpr)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS, MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_INT, MatexParser.FUNC_SUM, MatexParser.FUNC_PROD, MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_ECOS, MatexParser.FUNC_ESIN, MatexParser.FUNC_EDELTAAMPLITUDE, MatexParser.FUNC_ARCECOS, MatexParser.FUNC_ARCESIN, MatexParser.FUNC_ARCEDELTAAMPLITUDE, MatexParser.FUNC_SQRT, MatexParser.FUNC_BINOMIAL, MatexParser.CMD_FRAC, MatexParser.NUMBER, MatexParser.DERIVATIVE, MatexParser.VARIABLE, MatexParser.MIXNUMBER, MatexParser.WORD, MatexParser.INFINITY, MatexParser.GREEKLETTER, MatexParser.LETTERFUNCTIONBRACE, MatexParser.LETTERFUNCTIONPAREN, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.expr()
                pass
            elif token in [MatexParser.L_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
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
        self.enterRule(localctx, 20, self.RULE_funcParams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.subeq()
            self.state = 174
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
        self.enterRule(localctx, 22, self.RULE_funcIneqParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.subIneq()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MatexParser.CARET:
                self.state = 177
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_implicitMultiplicationExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.subtractionExpr(0)
            self.state = 182
            self.subtractionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.ImplicitMultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_implicitMultiplicationExpr)
                    self.state = 184
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 185
                    self.subtractionExpr(0) 
                self.state = 190
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_subtractionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.additionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.SubtractionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_subtractionExpr)
                    self.state = 194
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 195
                    self.match(MatexParser.MINUS)
                    self.state = 196
                    self.additionExpr(0) 
                self.state = 201
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_additionExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.divisionExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.AdditionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additionExpr)
                    self.state = 205
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 206
                    self.match(MatexParser.PLUS)
                    self.state = 207
                    self.divisionExpr(0) 
                self.state = 212
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_divisionExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.multiplicationExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.DivisionExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_divisionExpr)
                    self.state = 216
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 217
                    _la = self._input.LA(1)
                    if not(_la==MatexParser.DIV or _la==MatexParser.CMD_DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    self.multiplicationExpr(0) 
                self.state = 223
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_multiplicationExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiplicationExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicationExpr)
                    self.state = 227
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 228
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MatexParser.MUL) | (1 << MatexParser.CMD_TIMES) | (1 << MatexParser.CMD_CDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 229
                    self.powExpr() 
                self.state = 234
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
        self.enterRule(localctx, 34, self.RULE_fracExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(MatexParser.CMD_FRAC)
            self.state = 236
            self.bracedExpr()
            self.state = 237
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
        self.enterRule(localctx, 36, self.RULE_powExpr)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.signedAtom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.fracExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
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
        self.enterRule(localctx, 38, self.RULE_exponentiationExpr)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.signedAtom()
                self.state = 245
                self.match(MatexParser.CARET)
                self.state = 246
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.signedAtom()
                self.state = 249
                self.match(MatexParser.CARET)
                self.state = 250
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.signedAtom()
                self.state = 253
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
        self.enterRule(localctx, 40, self.RULE_signedAtom)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.negateAtom()
                pass
            elif token in [MatexParser.DERIVATIVE, MatexParser.MIXNUMBER, MatexParser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.localMultiplication()
                pass
            elif token in [MatexParser.FUNC_LOG, MatexParser.FUNC_LN, MatexParser.FUNC_SIN, MatexParser.FUNC_COS, MatexParser.FUNC_TAN, MatexParser.FUNC_CSC, MatexParser.FUNC_SEC, MatexParser.FUNC_COT, MatexParser.FUNC_ARCSIN, MatexParser.FUNC_ARCCOS, MatexParser.FUNC_ARCTAN, MatexParser.FUNC_ARCCSC, MatexParser.FUNC_ARCSEC, MatexParser.FUNC_ARCCOT, MatexParser.FUNC_SINH, MatexParser.FUNC_COSH, MatexParser.FUNC_TANH, MatexParser.FUNC_ARCSINH, MatexParser.FUNC_ARCCOSH, MatexParser.FUNC_ARCTANH, MatexParser.FUNC_ECOS, MatexParser.FUNC_ESIN, MatexParser.FUNC_EDELTAAMPLITUDE, MatexParser.FUNC_ARCECOS, MatexParser.FUNC_ARCESIN, MatexParser.FUNC_ARCEDELTAAMPLITUDE, MatexParser.FUNC_SQRT, MatexParser.LETTERFUNCTIONBRACE, MatexParser.LETTERFUNCTIONPAREN, MatexParser.GREEKFUNCTIONBRACE, MatexParser.GREEKFUNCTIONPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.func()
                pass
            elif token in [MatexParser.L_PAREN, MatexParser.L_BRACKET, MatexParser.BAR, MatexParser.FUNC_BINOMIAL, MatexParser.NUMBER, MatexParser.VARIABLE, MatexParser.INFINITY, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 260
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
        self.enterRule(localctx, 42, self.RULE_negateAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MatexParser.MINUS)
            self.state = 264
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
        self.enterRule(localctx, 44, self.RULE_localMultiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
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
        self.enterRule(localctx, 46, self.RULE_atom)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.indexedVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 271
                self.number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 272
                self.absolute()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 273
                self.exactDivision()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 274
                self.factorial()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 275
                self.binomial()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 276
                self.brackExpr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 277
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
        self.enterRule(localctx, 48, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
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
        self.enterRule(localctx, 50, self.RULE_indexedVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(MatexParser.VARIABLE)
            self.state = 283
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
        self.enterRule(localctx, 52, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
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
        self.enterRule(localctx, 54, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
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
        self.enterRule(localctx, 56, self.RULE_absolute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(MatexParser.BAR)
            self.state = 290
            self.expr()
            self.state = 291
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
        self.enterRule(localctx, 58, self.RULE_exactDivision)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MatexParser.VARIABLE)
            self.state = 294
            self.match(MatexParser.BAR)
            self.state = 295
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
        self.enterRule(localctx, 60, self.RULE_factorial)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.parenExpr()
                self.state = 298
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.number()
                self.state = 301
                self.match(MatexParser.BANG)
                pass
            elif token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.variable()
                self.state = 304
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
        self.enterRule(localctx, 62, self.RULE_binomial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(MatexParser.FUNC_BINOMIAL)
            self.state = 309
            self.bracedExpr()
            self.state = 310
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
        self.enterRule(localctx, 64, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.funcname()
                self.state = 313
                self.bracedMultiExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.funcname()
                self.state = 316
                self.parenMultiExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                _la = self._input.LA(1)
                if not(_la==MatexParser.LETTERFUNCTIONBRACE or _la==MatexParser.GREEKFUNCTIONBRACE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 319
                self.multiExpr(0)
                self.state = 320
                self.match(MatexParser.R_BRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                _la = self._input.LA(1)
                if not(_la==MatexParser.LETTERFUNCTIONPAREN or _la==MatexParser.GREEKFUNCTIONPAREN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 323
                self.multiExpr(0)
                self.state = 324
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
        self.enterRule(localctx, 66, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
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
        self.enterRule(localctx, 68, self.RULE_bracedMultiExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(MatexParser.L_BRACE)
            self.state = 331
            self.multiExpr(0)
            self.state = 332
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
        self.enterRule(localctx, 70, self.RULE_parenMultiExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(MatexParser.L_PAREN)
            self.state = 335
            self.multiExpr(0)
            self.state = 336
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_multiExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.MultiExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiExpr)
                    self.state = 341
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 342
                    self.match(MatexParser.COMMA)
                    self.state = 343
                    self.expr() 
                self.state = 348
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
        self.enterRule(localctx, 74, self.RULE_bracedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(MatexParser.L_BRACE)
            self.state = 350
            self.expr()
            self.state = 351
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
        self.enterRule(localctx, 76, self.RULE_brackExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(MatexParser.L_BRACKET)
            self.state = 354
            self.expr()
            self.state = 355
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
        self.enterRule(localctx, 78, self.RULE_parenExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(MatexParser.L_PAREN)
            self.state = 358
            self.expr()
            self.state = 359
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
        self.enterRule(localctx, 80, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(MatexParser.UNDERSCORE)
            self.state = 362
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
        self.enterRule(localctx, 82, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MatexParser.CARET)
            self.state = 365
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
        self.enterRule(localctx, 84, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(MatexParser.UNDERSCORE)
            self.state = 368
            self.match(MatexParser.L_BRACE)
            self.state = 369
            self.equality()
            self.state = 370
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
        self.enterRule(localctx, 86, self.RULE_subIneq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(MatexParser.UNDERSCORE)
            self.state = 373
            self.match(MatexParser.L_BRACE)
            self.state = 374
            self.inequality(0)
            self.state = 375
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
        self.enterRule(localctx, 88, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.variable()
            self.state = 378
            self.match(MatexParser.EQ)
            self.state = 379
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_inequality, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.state = 382
                self.variable()
                pass
            elif token in [MatexParser.NUMBER]:
                self.state = 383
                self.number()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 386
            self.match(MatexParser.INEQUALITIES)
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                self.state = 387
                self.variable()
                pass
            elif token in [MatexParser.NUMBER]:
                self.state = 388
                self.number()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MatexParser.InequalityContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_inequality)
                    self.state = 391
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 392
                    self.match(MatexParser.INEQUALITIES)
                    self.state = 395
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MatexParser.VARIABLE, MatexParser.GREEKLETTER]:
                        self.state = 393
                        self.variable()
                        pass
                    elif token in [MatexParser.NUMBER]:
                        self.state = 394
                        self.number()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self._predicates[12] = self.implicitMultiplicationExpr_sempred
        self._predicates[13] = self.subtractionExpr_sempred
        self._predicates[14] = self.additionExpr_sempred
        self._predicates[15] = self.divisionExpr_sempred
        self._predicates[16] = self.multiplicationExpr_sempred
        self._predicates[36] = self.multiExpr_sempred
        self._predicates[45] = self.inequality_sempred
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
         

    def inequality_sempred(self, localctx:InequalityContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         




