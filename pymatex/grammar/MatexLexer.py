# Generated from .\pymatex\grammar\MatexLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u03c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u012a\n\24\3\25\3\25\3\25\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\31\5\31\u0141\n\31\3\31\3\31\3\31\3")
        buf.write("\31\3\32\5\32\u0148\n\32\3\32\3\32\3\32\3\33\5\33\u014e")
        buf.write("\n\33\3\33\3\33\3\33\3\33\3\34\5\34\u0155\n\34\3\34\3")
        buf.write("\34\3\34\3\34\3\35\5\35\u015c\n\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\5\36\u0163\n\36\3\36\3\36\3\36\3\36\3\37\5\37\u016a")
        buf.write("\n\37\3\37\3\37\3\37\3\37\3 \5 \u0171\n \3 \3 \3 \3 \3")
        buf.write("!\5!\u0178\n!\3!\3!\3!\3\"\5\"\u017e\n\"\3\"\3\"\3\"\3")
        buf.write("#\5#\u0184\n#\3#\3#\3#\3$\5$\u018a\n$\3$\3$\3$\3%\5%\u0190")
        buf.write("\n%\3%\3%\3%\3&\5&\u0196\n&\3&\3&\3&\3\'\5\'\u019c\n\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3(\5(\u01a4\n(\3(\3(\3(\3(\3(\3)")
        buf.write("\5)\u01ac\n)\3)\3)\3)\3)\3)\3*\5*\u01b4\n*\3*\3*\3*\3")
        buf.write("+\5+\u01ba\n+\3+\3+\3+\3,\5,\u01c0\n,\3,\3,\3,\3-\5-\u01c6")
        buf.write("\n-\3-\3-\3-\3.\5.\u01cc\n.\3.\3.\3.\3/\5/\u01d2\n/\3")
        buf.write("/\3/\3/\3\60\5\60\u01d8\n\60\3\60\3\60\3\60\3\61\5\61")
        buf.write("\u01de\n\61\3\61\3\61\3\61\3\62\5\62\u01e4\n\62\3\62\3")
        buf.write("\62\3\62\3\63\5\63\u01ea\n\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\5\64\u01f2\n\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38")
        buf.write("\39\39\3:\3:\3;\7;\u0217\n;\f;\16;\u021a\13;\3;\5;\u021d")
        buf.write("\n;\3;\6;\u0220\n;\r;\16;\u0221\3;\3;\5;\u0226\n;\3;\6")
        buf.write(";\u0229\n;\r;\16;\u022a\5;\u022d\n;\3<\3<\3<\3=\3=\3>")
        buf.write("\3>\6>\u0236\n>\r>\16>\u0237\3?\6?\u023b\n?\r?\16?\u023c")
        buf.write("\3@\3@\3@\3@\3@\3@\3@\3A\3A\3B\3B\3C\3C\3C\3C\3C\3D\3")
        buf.write("D\3E\3E\3E\3E\3E\3F\3F\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3")
        buf.write("G\3G\5G\u0264\nG\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\5H\u0270")
        buf.write("\nH\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u027e\nI\3")
        buf.write("J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u028c\nJ\3K\3K\3")
        buf.write("K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\5K\u029e\nK\3")
        buf.write("L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u02aa\nL\3M\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\5M\u02b4\nM\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3")
        buf.write("N\3N\5N\u02c2\nN\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u02ce")
        buf.write("\nO\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u02dc\nP\3")
        buf.write("Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u02ec\nQ\3")
        buf.write("R\3R\3R\3R\3R\3R\5R\u02f4\nR\3S\3S\3S\3S\3S\3S\5S\u02fc")
        buf.write("\nS\3T\3T\3T\3T\3T\3T\5T\u0304\nT\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\3U\3U\3U\3U\5U\u0316\nU\3V\3V\3V\3V\3")
        buf.write("V\3V\5V\u031e\nV\3W\3W\3W\3W\3W\3W\3W\3W\5W\u0328\nW\3")
        buf.write("X\3X\3X\3X\3X\3X\3X\3X\3X\3X\3X\3X\5X\u0336\nX\3Y\3Y\3")
        buf.write("Y\3Y\3Y\3Y\3Y\3Y\5Y\u0340\nY\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3")
        buf.write("Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\5Z\u0352\nZ\3[\3[\3[\3[\3[\3[\3")
        buf.write("[\3[\5[\u035c\n[\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\5\\\u0366")
        buf.write("\n\\\3]\3]\3]\3]\3]\3]\3]\3]\5]\u0370\n]\3^\3^\3^\3^\3")
        buf.write("^\3^\3^\3^\3^\3^\3^\3^\5^\u037e\n^\3_\3_\3_\3_\3_\3_\3")
        buf.write("_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\5")
        buf.write("_\u0398\n_\3`\3`\3`\3`\3`\5`\u039f\n`\3`\3`\3a\3a\5a\u03a5")
        buf.write("\na\3a\3a\3b\3b\5b\u03ab\nb\3b\3b\3c\3c\5c\u03b1\nc\3")
        buf.write("c\3c\3d\3d\5d\u03b7\nd\3d\3d\3e\6e\u03bc\ne\re\16e\u03bd")
        buf.write("\3e\3e\2\2f\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\2%\23\'\24)\25+\26")
        buf.write("-\27/\2\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"")
        buf.write("G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66")
        buf.write("o\67q\2s\2u8w9y:{;}<\177=\u0081>\u0083?\u0085@\u0087A")
        buf.write("\u0089B\u008bC\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2")
        buf.write("\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3")
        buf.write("\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1")
        buf.write("\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bdD\u00bf")
        buf.write("\2\u00c1E\u00c3F\u00c5G\u00c7H\u00c9I\3\2\7\4\2C\\c|\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2\u0401\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3")
        buf.write("\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u00bd\3\2\2\2\2\u00c1")
        buf.write("\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2")
        buf.write("\2\2\u00c9\3\2\2\2\3\u00cb\3\2\2\2\5\u00cd\3\2\2\2\7\u00cf")
        buf.write("\3\2\2\2\t\u00d1\3\2\2\2\13\u00d3\3\2\2\2\r\u00d5\3\2")
        buf.write("\2\2\17\u00d7\3\2\2\2\21\u00d9\3\2\2\2\23\u00db\3\2\2")
        buf.write("\2\25\u00dd\3\2\2\2\27\u00df\3\2\2\2\31\u00e1\3\2\2\2")
        buf.write("\33\u00e3\3\2\2\2\35\u00e5\3\2\2\2\37\u00e7\3\2\2\2!\u00e9")
        buf.write("\3\2\2\2#\u00eb\3\2\2\2%\u00ed\3\2\2\2\'\u0129\3\2\2\2")
        buf.write(")\u012b\3\2\2\2+\u0130\3\2\2\2-\u0135\3\2\2\2/\u013b\3")
        buf.write("\2\2\2\61\u0140\3\2\2\2\63\u0147\3\2\2\2\65\u014d\3\2")
        buf.write("\2\2\67\u0154\3\2\2\29\u015b\3\2\2\2;\u0162\3\2\2\2=\u0169")
        buf.write("\3\2\2\2?\u0170\3\2\2\2A\u0177\3\2\2\2C\u017d\3\2\2\2")
        buf.write("E\u0183\3\2\2\2G\u0189\3\2\2\2I\u018f\3\2\2\2K\u0195\3")
        buf.write("\2\2\2M\u019b\3\2\2\2O\u01a3\3\2\2\2Q\u01ab\3\2\2\2S\u01b3")
        buf.write("\3\2\2\2U\u01b9\3\2\2\2W\u01bf\3\2\2\2Y\u01c5\3\2\2\2")
        buf.write("[\u01cb\3\2\2\2]\u01d1\3\2\2\2_\u01d7\3\2\2\2a\u01dd\3")
        buf.write("\2\2\2c\u01e3\3\2\2\2e\u01e9\3\2\2\2g\u01f1\3\2\2\2i\u01f9")
        buf.write("\3\2\2\2k\u0200\3\2\2\2m\u0206\3\2\2\2o\u020b\3\2\2\2")
        buf.write("q\u0211\3\2\2\2s\u0213\3\2\2\2u\u0218\3\2\2\2w\u022e\3")
        buf.write("\2\2\2y\u0231\3\2\2\2{\u0233\3\2\2\2}\u023a\3\2\2\2\177")
        buf.write("\u023e\3\2\2\2\u0081\u0245\3\2\2\2\u0083\u0247\3\2\2\2")
        buf.write("\u0085\u0249\3\2\2\2\u0087\u024e\3\2\2\2\u0089\u0250\3")
        buf.write("\2\2\2\u008b\u0255\3\2\2\2\u008d\u0263\3\2\2\2\u008f\u026f")
        buf.write("\3\2\2\2\u0091\u027d\3\2\2\2\u0093\u028b\3\2\2\2\u0095")
        buf.write("\u029d\3\2\2\2\u0097\u02a9\3\2\2\2\u0099\u02b3\3\2\2\2")
        buf.write("\u009b\u02c1\3\2\2\2\u009d\u02cd\3\2\2\2\u009f\u02db\3")
        buf.write("\2\2\2\u00a1\u02eb\3\2\2\2\u00a3\u02f3\3\2\2\2\u00a5\u02fb")
        buf.write("\3\2\2\2\u00a7\u0303\3\2\2\2\u00a9\u0315\3\2\2\2\u00ab")
        buf.write("\u031d\3\2\2\2\u00ad\u0327\3\2\2\2\u00af\u0335\3\2\2\2")
        buf.write("\u00b1\u033f\3\2\2\2\u00b3\u0351\3\2\2\2\u00b5\u035b\3")
        buf.write("\2\2\2\u00b7\u0365\3\2\2\2\u00b9\u036f\3\2\2\2\u00bb\u037d")
        buf.write("\3\2\2\2\u00bd\u0397\3\2\2\2\u00bf\u0399\3\2\2\2\u00c1")
        buf.write("\u03a2\3\2\2\2\u00c3\u03a8\3\2\2\2\u00c5\u03ae\3\2\2\2")
        buf.write("\u00c7\u03b4\3\2\2\2\u00c9\u03bb\3\2\2\2\u00cb\u00cc\7")
        buf.write("-\2\2\u00cc\4\3\2\2\2\u00cd\u00ce\7/\2\2\u00ce\6\3\2\2")
        buf.write("\2\u00cf\u00d0\7,\2\2\u00d0\b\3\2\2\2\u00d1\u00d2\7\61")
        buf.write("\2\2\u00d2\n\3\2\2\2\u00d3\u00d4\7*\2\2\u00d4\f\3\2\2")
        buf.write("\2\u00d5\u00d6\7+\2\2\u00d6\16\3\2\2\2\u00d7\u00d8\7}")
        buf.write("\2\2\u00d8\20\3\2\2\2\u00d9\u00da\7\177\2\2\u00da\22\3")
        buf.write("\2\2\2\u00db\u00dc\7]\2\2\u00dc\24\3\2\2\2\u00dd\u00de")
        buf.write("\7_\2\2\u00de\26\3\2\2\2\u00df\u00e0\7.\2\2\u00e0\30\3")
        buf.write("\2\2\2\u00e1\u00e2\7\60\2\2\u00e2\32\3\2\2\2\u00e3\u00e4")
        buf.write("\7~\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\7a\2\2\u00e6\36\3")
        buf.write("\2\2\2\u00e7\u00e8\7`\2\2\u00e8 \3\2\2\2\u00e9\u00ea\7")
        buf.write("<\2\2\u00ea\"\3\2\2\2\u00eb\u00ec\7^\2\2\u00ec$\3\2\2")
        buf.write("\2\u00ed\u00ee\7^\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0\7")
        buf.write("k\2\2\u00f0\u00f1\7o\2\2\u00f1&\3\2\2\2\u00f2\u00f3\7")
        buf.write("^\2\2\u00f3\u00f4\7v\2\2\u00f4\u012a\7q\2\2\u00f5\u00f6")
        buf.write("\7^\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9")
        buf.write("\7i\2\2\u00f9\u00fa\7j\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc")
        buf.write("\7c\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u012a\7y\2\2\u0100\u0101\7^\2\2\u0101\u0102")
        buf.write("\7T\2\2\u0102\u0103\7k\2\2\u0103\u0104\7i\2\2\u0104\u0105")
        buf.write("\7j\2\2\u0105\u0106\7v\2\2\u0106\u0107\7c\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108\u0109\7t\2\2\u0109\u010a\7q\2\2\u010a\u012a")
        buf.write("\7y\2\2\u010b\u010c\7^\2\2\u010c\u010d\7n\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e\u010f\7p\2\2\u010f\u0110\7i\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111\u0112\7k\2\2\u0112\u0113\7i\2\2\u0113\u0114")
        buf.write("\7j\2\2\u0114\u0115\7v\2\2\u0115\u0116\7c\2\2\u0116\u0117")
        buf.write("\7t\2\2\u0117\u0118\7t\2\2\u0118\u0119\7q\2\2\u0119\u012a")
        buf.write("\7y\2\2\u011a\u011b\7^\2\2\u011b\u011c\7N\2\2\u011c\u011d")
        buf.write("\7q\2\2\u011d\u011e\7p\2\2\u011e\u011f\7i\2\2\u011f\u0120")
        buf.write("\7t\2\2\u0120\u0121\7k\2\2\u0121\u0122\7i\2\2\u0122\u0123")
        buf.write("\7j\2\2\u0123\u0124\7v\2\2\u0124\u0125\7c\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7t\2\2\u0127\u0128\7q\2\2\u0128\u012a")
        buf.write("\7y\2\2\u0129\u00f2\3\2\2\2\u0129\u00f5\3\2\2\2\u0129")
        buf.write("\u0100\3\2\2\2\u0129\u010b\3\2\2\2\u0129\u011a\3\2\2\2")
        buf.write("\u012a(\3\2\2\2\u012b\u012c\7^\2\2\u012c\u012d\7k\2\2")
        buf.write("\u012d\u012e\7p\2\2\u012e\u012f\7v\2\2\u012f*\3\2\2\2")
        buf.write("\u0130\u0131\7^\2\2\u0131\u0132\7u\2\2\u0132\u0133\7w")
        buf.write("\2\2\u0133\u0134\7o\2\2\u0134,\3\2\2\2\u0135\u0136\7^")
        buf.write("\2\2\u0136\u0137\7r\2\2\u0137\u0138\7t\2\2\u0138\u0139")
        buf.write("\7q\2\2\u0139\u013a\7f\2\2\u013a.\3\2\2\2\u013b\u013c")
        buf.write("\7c\2\2\u013c\u013d\7t\2\2\u013d\u013e\7e\2\2\u013e\60")
        buf.write("\3\2\2\2\u013f\u0141\5#\22\2\u0140\u013f\3\2\2\2\u0140")
        buf.write("\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\7n\2\2")
        buf.write("\u0143\u0144\7q\2\2\u0144\u0145\7i\2\2\u0145\62\3\2\2")
        buf.write("\2\u0146\u0148\5#\22\2\u0147\u0146\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\7n\2\2\u014a")
        buf.write("\u014b\7p\2\2\u014b\64\3\2\2\2\u014c\u014e\5#\22\2\u014d")
        buf.write("\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write("\u014f\u0150\7u\2\2\u0150\u0151\7k\2\2\u0151\u0152\7p")
        buf.write("\2\2\u0152\66\3\2\2\2\u0153\u0155\5#\22\2\u0154\u0153")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0157\7e\2\2\u0157\u0158\7q\2\2\u0158\u0159\7u\2\2\u0159")
        buf.write("8\3\2\2\2\u015a\u015c\5#\22\2\u015b\u015a\3\2\2\2\u015b")
        buf.write("\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\7v\2\2")
        buf.write("\u015e\u015f\7c\2\2\u015f\u0160\7p\2\2\u0160:\3\2\2\2")
        buf.write("\u0161\u0163\5#\22\2\u0162\u0161\3\2\2\2\u0162\u0163\3")
        buf.write("\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\7e\2\2\u0165\u0166")
        buf.write("\7u\2\2\u0166\u0167\7e\2\2\u0167<\3\2\2\2\u0168\u016a")
        buf.write("\5#\22\2\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u016c\7u\2\2\u016c\u016d\7g\2\2\u016d")
        buf.write("\u016e\7e\2\2\u016e>\3\2\2\2\u016f\u0171\5#\22\2\u0170")
        buf.write("\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172\3\2\2\2")
        buf.write("\u0172\u0173\7e\2\2\u0173\u0174\7q\2\2\u0174\u0175\7v")
        buf.write("\2\2\u0175@\3\2\2\2\u0176\u0178\5#\22\2\u0177\u0176\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a")
        buf.write("\5/\30\2\u017a\u017b\5\65\33\2\u017bB\3\2\2\2\u017c\u017e")
        buf.write("\5#\22\2\u017d\u017c\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0180\5/\30\2\u0180\u0181\5\67\34")
        buf.write("\2\u0181D\3\2\2\2\u0182\u0184\5#\22\2\u0183\u0182\3\2")
        buf.write("\2\2\u0183\u0184\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186")
        buf.write("\5/\30\2\u0186\u0187\59\35\2\u0187F\3\2\2\2\u0188\u018a")
        buf.write("\5#\22\2\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u018c\5/\30\2\u018c\u018d\5;\36\2")
        buf.write("\u018dH\3\2\2\2\u018e\u0190\5#\22\2\u018f\u018e\3\2\2")
        buf.write("\2\u018f\u0190\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0192")
        buf.write("\5/\30\2\u0192\u0193\5=\37\2\u0193J\3\2\2\2\u0194\u0196")
        buf.write("\5#\22\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0197\3\2\2\2\u0197\u0198\5/\30\2\u0198\u0199\5? \2\u0199")
        buf.write("L\3\2\2\2\u019a\u019c\5#\22\2\u019b\u019a\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\7u\2\2")
        buf.write("\u019e\u019f\7k\2\2\u019f\u01a0\7p\2\2\u01a0\u01a1\7j")
        buf.write("\2\2\u01a1N\3\2\2\2\u01a2\u01a4\5#\22\2\u01a3\u01a2\3")
        buf.write("\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6")
        buf.write("\7e\2\2\u01a6\u01a7\7q\2\2\u01a7\u01a8\7u\2\2\u01a8\u01a9")
        buf.write("\7j\2\2\u01a9P\3\2\2\2\u01aa\u01ac\5#\22\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("\u01ae\7v\2\2\u01ae\u01af\7c\2\2\u01af\u01b0\7p\2\2\u01b0")
        buf.write("\u01b1\7j\2\2\u01b1R\3\2\2\2\u01b2\u01b4\5#\22\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b6\5/\30\2\u01b6\u01b7\5M\'\2\u01b7T\3\2\2\2")
        buf.write("\u01b8\u01ba\5#\22\2\u01b9\u01b8\3\2\2\2\u01b9\u01ba\3")
        buf.write("\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\5/\30\2\u01bc\u01bd")
        buf.write("\5O(\2\u01bdV\3\2\2\2\u01be\u01c0\5#\22\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("\u01c2\5/\30\2\u01c2\u01c3\5Q)\2\u01c3X\3\2\2\2\u01c4")
        buf.write("\u01c6\5#\22\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c7\3\2\2\2\u01c7\u01c8\7e\2\2\u01c8\u01c9\7")
        buf.write("p\2\2\u01c9Z\3\2\2\2\u01ca\u01cc\5#\22\2\u01cb\u01ca\3")
        buf.write("\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce")
        buf.write("\7u\2\2\u01ce\u01cf\7p\2\2\u01cf\\\3\2\2\2\u01d0\u01d2")
        buf.write("\5#\22\2\u01d1\u01d0\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3\u01d4\7f\2\2\u01d4\u01d5\7p\2\2\u01d5")
        buf.write("^\3\2\2\2\u01d6\u01d8\5#\22\2\u01d7\u01d6\3\2\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\5/\30\2")
        buf.write("\u01da\u01db\5Y-\2\u01db`\3\2\2\2\u01dc\u01de\5#\22\2")
        buf.write("\u01dd\u01dc\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\3")
        buf.write("\2\2\2\u01df\u01e0\5/\30\2\u01e0\u01e1\5[.\2\u01e1b\3")
        buf.write("\2\2\2\u01e2\u01e4\5#\22\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4")
        buf.write("\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\5/\30\2\u01e6")
        buf.write("\u01e7\5]/\2\u01e7d\3\2\2\2\u01e8\u01ea\5#\22\2\u01e9")
        buf.write("\u01e8\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\3\2\2\2")
        buf.write("\u01eb\u01ec\7u\2\2\u01ec\u01ed\7s\2\2\u01ed\u01ee\7t")
        buf.write("\2\2\u01ee\u01ef\7v\2\2\u01eff\3\2\2\2\u01f0\u01f2\5#")
        buf.write("\22\2\u01f1\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3")
        buf.write("\3\2\2\2\u01f3\u01f4\7d\2\2\u01f4\u01f5\7k\2\2\u01f5\u01f6")
        buf.write("\7p\2\2\u01f6\u01f7\7q\2\2\u01f7\u01f8\7o\2\2\u01f8h\3")
        buf.write("\2\2\2\u01f9\u01fa\7^\2\2\u01fa\u01fb\7v\2\2\u01fb\u01fc")
        buf.write("\7k\2\2\u01fc\u01fd\7o\2\2\u01fd\u01fe\7g\2\2\u01fe\u01ff")
        buf.write("\7u\2\2\u01ffj\3\2\2\2\u0200\u0201\7^\2\2\u0201\u0202")
        buf.write("\7e\2\2\u0202\u0203\7f\2\2\u0203\u0204\7q\2\2\u0204\u0205")
        buf.write("\7v\2\2\u0205l\3\2\2\2\u0206\u0207\7^\2\2\u0207\u0208")
        buf.write("\7f\2\2\u0208\u0209\7k\2\2\u0209\u020a\7x\2\2\u020an\3")
        buf.write("\2\2\2\u020b\u020c\7^\2\2\u020c\u020d\7h\2\2\u020d\u020e")
        buf.write("\7t\2\2\u020e\u020f\7c\2\2\u020f\u0210\7e\2\2\u0210p\3")
        buf.write("\2\2\2\u0211\u0212\t\2\2\2\u0212r\3\2\2\2\u0213\u0214")
        buf.write("\t\3\2\2\u0214t\3\2\2\2\u0215\u0217\5s:\2\u0216\u0215")
        buf.write("\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3\2\2\2")
        buf.write("\u021b\u021d\7\60\2\2\u021c\u021b\3\2\2\2\u021c\u021d")
        buf.write("\3\2\2\2\u021d\u021f\3\2\2\2\u021e\u0220\5s:\2\u021f\u021e")
        buf.write("\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222\u022c\3\2\2\2\u0223\u0225\t\4\2\2")
        buf.write("\u0224\u0226\t\5\2\2\u0225\u0224\3\2\2\2\u0225\u0226\3")
        buf.write("\2\2\2\u0226\u0228\3\2\2\2\u0227\u0229\5s:\2\u0228\u0227")
        buf.write("\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u0228\3\2\2\2\u022a")
        buf.write("\u022b\3\2\2\2\u022b\u022d\3\2\2\2\u022c\u0223\3\2\2\2")
        buf.write("\u022c\u022d\3\2\2\2\u022dv\3\2\2\2\u022e\u022f\7f\2\2")
        buf.write("\u022f\u0230\5q9\2\u0230x\3\2\2\2\u0231\u0232\5q9\2\u0232")
        buf.write("z\3\2\2\2\u0233\u0235\5u;\2\u0234\u0236\5y=\2\u0235\u0234")
        buf.write("\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0235\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238|\3\2\2\2\u0239\u023b\5y=\2\u023a")
        buf.write("\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023c\u023d\3\2\2\2\u023d~\3\2\2\2\u023e\u023f\7^\2\2")
        buf.write("\u023f\u0240\7k\2\2\u0240\u0241\7p\2\2\u0241\u0242\7h")
        buf.write("\2\2\u0242\u0243\7v\2\2\u0243\u0244\7{\2\2\u0244\u0080")
        buf.write("\3\2\2\2\u0245\u0246\7?\2\2\u0246\u0082\3\2\2\2\u0247")
        buf.write("\u0248\7>\2\2\u0248\u0084\3\2\2\2\u0249\u024a\7^\2\2\u024a")
        buf.write("\u024b\7n\2\2\u024b\u024c\7g\2\2\u024c\u024d\7s\2\2\u024d")
        buf.write("\u0086\3\2\2\2\u024e\u024f\7@\2\2\u024f\u0088\3\2\2\2")
        buf.write("\u0250\u0251\7^\2\2\u0251\u0252\7i\2\2\u0252\u0253\7g")
        buf.write("\2\2\u0253\u0254\7s\2\2\u0254\u008a\3\2\2\2\u0255\u0256")
        buf.write("\7#\2\2\u0256\u008c\3\2\2\2\u0257\u0258\7^\2\2\u0258\u0259")
        buf.write("\7c\2\2\u0259\u025a\7n\2\2\u025a\u025b\7r\2\2\u025b\u025c")
        buf.write("\7j\2\2\u025c\u0264\7c\2\2\u025d\u025e\7^\2\2\u025e\u025f")
        buf.write("\7C\2\2\u025f\u0260\7n\2\2\u0260\u0261\7r\2\2\u0261\u0262")
        buf.write("\7j\2\2\u0262\u0264\7c\2\2\u0263\u0257\3\2\2\2\u0263\u025d")
        buf.write("\3\2\2\2\u0264\u008e\3\2\2\2\u0265\u0266\7^\2\2\u0266")
        buf.write("\u0267\7d\2\2\u0267\u0268\7g\2\2\u0268\u0269\7v\2\2\u0269")
        buf.write("\u0270\7c\2\2\u026a\u026b\7^\2\2\u026b\u026c\7D\2\2\u026c")
        buf.write("\u026d\7g\2\2\u026d\u026e\7v\2\2\u026e\u0270\7c\2\2\u026f")
        buf.write("\u0265\3\2\2\2\u026f\u026a\3\2\2\2\u0270\u0090\3\2\2\2")
        buf.write("\u0271\u0272\7^\2\2\u0272\u0273\7i\2\2\u0273\u0274\7c")
        buf.write("\2\2\u0274\u0275\7o\2\2\u0275\u0276\7o\2\2\u0276\u027e")
        buf.write("\7c\2\2\u0277\u0278\7^\2\2\u0278\u0279\7I\2\2\u0279\u027a")
        buf.write("\7c\2\2\u027a\u027b\7o\2\2\u027b\u027c\7o\2\2\u027c\u027e")
        buf.write("\7c\2\2\u027d\u0271\3\2\2\2\u027d\u0277\3\2\2\2\u027e")
        buf.write("\u0092\3\2\2\2\u027f\u0280\7^\2\2\u0280\u0281\7f\2\2\u0281")
        buf.write("\u0282\7g\2\2\u0282\u0283\7n\2\2\u0283\u0284\7v\2\2\u0284")
        buf.write("\u028c\7c\2\2\u0285\u0286\7^\2\2\u0286\u0287\7F\2\2\u0287")
        buf.write("\u0288\7g\2\2\u0288\u0289\7n\2\2\u0289\u028a\7v\2\2\u028a")
        buf.write("\u028c\7c\2\2\u028b\u027f\3\2\2\2\u028b\u0285\3\2\2\2")
        buf.write("\u028c\u0094\3\2\2\2\u028d\u028e\7^\2\2\u028e\u028f\7")
        buf.write("g\2\2\u028f\u0290\7r\2\2\u0290\u0291\7u\2\2\u0291\u0292")
        buf.write("\7k\2\2\u0292\u0293\7n\2\2\u0293\u0294\7q\2\2\u0294\u029e")
        buf.write("\7p\2\2\u0295\u0296\7^\2\2\u0296\u0297\7G\2\2\u0297\u0298")
        buf.write("\7r\2\2\u0298\u0299\7u\2\2\u0299\u029a\7k\2\2\u029a\u029b")
        buf.write("\7n\2\2\u029b\u029c\7q\2\2\u029c\u029e\7p\2\2\u029d\u028d")
        buf.write("\3\2\2\2\u029d\u0295\3\2\2\2\u029e\u0096\3\2\2\2\u029f")
        buf.write("\u02a0\7^\2\2\u02a0\u02a1\7|\2\2\u02a1\u02a2\7g\2\2\u02a2")
        buf.write("\u02a3\7v\2\2\u02a3\u02aa\7c\2\2\u02a4\u02a5\7^\2\2\u02a5")
        buf.write("\u02a6\7\\\2\2\u02a6\u02a7\7g\2\2\u02a7\u02a8\7v\2\2\u02a8")
        buf.write("\u02aa\7c\2\2\u02a9\u029f\3\2\2\2\u02a9\u02a4\3\2\2\2")
        buf.write("\u02aa\u0098\3\2\2\2\u02ab\u02ac\7^\2\2\u02ac\u02ad\7")
        buf.write("g\2\2\u02ad\u02ae\7v\2\2\u02ae\u02b4\7c\2\2\u02af\u02b0")
        buf.write("\7^\2\2\u02b0\u02b1\7G\2\2\u02b1\u02b2\7v\2\2\u02b2\u02b4")
        buf.write("\7c\2\2\u02b3\u02ab\3\2\2\2\u02b3\u02af\3\2\2\2\u02b4")
        buf.write("\u009a\3\2\2\2\u02b5\u02b6\7^\2\2\u02b6\u02b7\7v\2\2\u02b7")
        buf.write("\u02b8\7j\2\2\u02b8\u02b9\7g\2\2\u02b9\u02ba\7v\2\2\u02ba")
        buf.write("\u02c2\7c\2\2\u02bb\u02bc\7^\2\2\u02bc\u02bd\7V\2\2\u02bd")
        buf.write("\u02be\7j\2\2\u02be\u02bf\7g\2\2\u02bf\u02c0\7v\2\2\u02c0")
        buf.write("\u02c2\7c\2\2\u02c1\u02b5\3\2\2\2\u02c1\u02bb\3\2\2\2")
        buf.write("\u02c2\u009c\3\2\2\2\u02c3\u02c4\7^\2\2\u02c4\u02c5\7")
        buf.write("k\2\2\u02c5\u02c6\7q\2\2\u02c6\u02c7\7v\2\2\u02c7\u02ce")
        buf.write("\7c\2\2\u02c8\u02c9\7^\2\2\u02c9\u02ca\7K\2\2\u02ca\u02cb")
        buf.write("\7q\2\2\u02cb\u02cc\7v\2\2\u02cc\u02ce\7c\2\2\u02cd\u02c3")
        buf.write("\3\2\2\2\u02cd\u02c8\3\2\2\2\u02ce\u009e\3\2\2\2\u02cf")
        buf.write("\u02d0\7^\2\2\u02d0\u02d1\7m\2\2\u02d1\u02d2\7c\2\2\u02d2")
        buf.write("\u02d3\7r\2\2\u02d3\u02d4\7r\2\2\u02d4\u02dc\7c\2\2\u02d5")
        buf.write("\u02d6\7^\2\2\u02d6\u02d7\7M\2\2\u02d7\u02d8\7c\2\2\u02d8")
        buf.write("\u02d9\7r\2\2\u02d9\u02da\7r\2\2\u02da\u02dc\7c\2\2\u02db")
        buf.write("\u02cf\3\2\2\2\u02db\u02d5\3\2\2\2\u02dc\u00a0\3\2\2\2")
        buf.write("\u02dd\u02de\7^\2\2\u02de\u02df\7n\2\2\u02df\u02e0\7c")
        buf.write("\2\2\u02e0\u02e1\7o\2\2\u02e1\u02e2\7d\2\2\u02e2\u02e3")
        buf.write("\7f\2\2\u02e3\u02ec\7c\2\2\u02e4\u02e5\7^\2\2\u02e5\u02e6")
        buf.write("\7N\2\2\u02e6\u02e7\7c\2\2\u02e7\u02e8\7o\2\2\u02e8\u02e9")
        buf.write("\7d\2\2\u02e9\u02ea\7f\2\2\u02ea\u02ec\7c\2\2\u02eb\u02dd")
        buf.write("\3\2\2\2\u02eb\u02e4\3\2\2\2\u02ec\u00a2\3\2\2\2\u02ed")
        buf.write("\u02ee\7^\2\2\u02ee\u02ef\7o\2\2\u02ef\u02f4\7w\2\2\u02f0")
        buf.write("\u02f1\7^\2\2\u02f1\u02f2\7O\2\2\u02f2\u02f4\7w\2\2\u02f3")
        buf.write("\u02ed\3\2\2\2\u02f3\u02f0\3\2\2\2\u02f4\u00a4\3\2\2\2")
        buf.write("\u02f5\u02f6\7^\2\2\u02f6\u02f7\7p\2\2\u02f7\u02fc\7w")
        buf.write("\2\2\u02f8\u02f9\7^\2\2\u02f9\u02fa\7P\2\2\u02fa\u02fc")
        buf.write("\7w\2\2\u02fb\u02f5\3\2\2\2\u02fb\u02f8\3\2\2\2\u02fc")
        buf.write("\u00a6\3\2\2\2\u02fd\u02fe\7^\2\2\u02fe\u02ff\7z\2\2\u02ff")
        buf.write("\u0304\7k\2\2\u0300\u0301\7^\2\2\u0301\u0302\7Z\2\2\u0302")
        buf.write("\u0304\7k\2\2\u0303\u02fd\3\2\2\2\u0303\u0300\3\2\2\2")
        buf.write("\u0304\u00a8\3\2\2\2\u0305\u0306\7^\2\2\u0306\u0307\7")
        buf.write("q\2\2\u0307\u0308\7o\2\2\u0308\u0309\7k\2\2\u0309\u030a")
        buf.write("\7e\2\2\u030a\u030b\7t\2\2\u030b\u030c\7q\2\2\u030c\u0316")
        buf.write("\7p\2\2\u030d\u030e\7^\2\2\u030e\u030f\7Q\2\2\u030f\u0310")
        buf.write("\7o\2\2\u0310\u0311\7k\2\2\u0311\u0312\7e\2\2\u0312\u0313")
        buf.write("\7t\2\2\u0313\u0314\7q\2\2\u0314\u0316\7p\2\2\u0315\u0305")
        buf.write("\3\2\2\2\u0315\u030d\3\2\2\2\u0316\u00aa\3\2\2\2\u0317")
        buf.write("\u0318\7^\2\2\u0318\u0319\7r\2\2\u0319\u031e\7k\2\2\u031a")
        buf.write("\u031b\7^\2\2\u031b\u031c\7R\2\2\u031c\u031e\7k\2\2\u031d")
        buf.write("\u0317\3\2\2\2\u031d\u031a\3\2\2\2\u031e\u00ac\3\2\2\2")
        buf.write("\u031f\u0320\7^\2\2\u0320\u0321\7t\2\2\u0321\u0322\7j")
        buf.write("\2\2\u0322\u0328\7q\2\2\u0323\u0324\7^\2\2\u0324\u0325")
        buf.write("\7T\2\2\u0325\u0326\7j\2\2\u0326\u0328\7q\2\2\u0327\u031f")
        buf.write("\3\2\2\2\u0327\u0323\3\2\2\2\u0328\u00ae\3\2\2\2\u0329")
        buf.write("\u032a\7^\2\2\u032a\u032b\7u\2\2\u032b\u032c\7k\2\2\u032c")
        buf.write("\u032d\7i\2\2\u032d\u032e\7o\2\2\u032e\u0336\7c\2\2\u032f")
        buf.write("\u0330\7^\2\2\u0330\u0331\7U\2\2\u0331\u0332\7k\2\2\u0332")
        buf.write("\u0333\7i\2\2\u0333\u0334\7o\2\2\u0334\u0336\7c\2\2\u0335")
        buf.write("\u0329\3\2\2\2\u0335\u032f\3\2\2\2\u0336\u00b0\3\2\2\2")
        buf.write("\u0337\u0338\7^\2\2\u0338\u0339\7v\2\2\u0339\u033a\7c")
        buf.write("\2\2\u033a\u0340\7w\2\2\u033b\u033c\7^\2\2\u033c\u033d")
        buf.write("\7V\2\2\u033d\u033e\7c\2\2\u033e\u0340\7w\2\2\u033f\u0337")
        buf.write("\3\2\2\2\u033f\u033b\3\2\2\2\u0340\u00b2\3\2\2\2\u0341")
        buf.write("\u0342\7^\2\2\u0342\u0343\7w\2\2\u0343\u0344\7r\2\2\u0344")
        buf.write("\u0345\7u\2\2\u0345\u0346\7k\2\2\u0346\u0347\7n\2\2\u0347")
        buf.write("\u0348\7q\2\2\u0348\u0352\7p\2\2\u0349\u034a\7^\2\2\u034a")
        buf.write("\u034b\7W\2\2\u034b\u034c\7r\2\2\u034c\u034d\7u\2\2\u034d")
        buf.write("\u034e\7k\2\2\u034e\u034f\7n\2\2\u034f\u0350\7q\2\2\u0350")
        buf.write("\u0352\7p\2\2\u0351\u0341\3\2\2\2\u0351\u0349\3\2\2\2")
        buf.write("\u0352\u00b4\3\2\2\2\u0353\u0354\7^\2\2\u0354\u0355\7")
        buf.write("r\2\2\u0355\u0356\7j\2\2\u0356\u035c\7k\2\2\u0357\u0358")
        buf.write("\7^\2\2\u0358\u0359\7R\2\2\u0359\u035a\7j\2\2\u035a\u035c")
        buf.write("\7k\2\2\u035b\u0353\3\2\2\2\u035b\u0357\3\2\2\2\u035c")
        buf.write("\u00b6\3\2\2\2\u035d\u035e\7^\2\2\u035e\u035f\7e\2\2\u035f")
        buf.write("\u0360\7j\2\2\u0360\u0366\7k\2\2\u0361\u0362\7^\2\2\u0362")
        buf.write("\u0363\7E\2\2\u0363\u0364\7j\2\2\u0364\u0366\7k\2\2\u0365")
        buf.write("\u035d\3\2\2\2\u0365\u0361\3\2\2\2\u0366\u00b8\3\2\2\2")
        buf.write("\u0367\u0368\7^\2\2\u0368\u0369\7r\2\2\u0369\u036a\7u")
        buf.write("\2\2\u036a\u0370\7k\2\2\u036b\u036c\7^\2\2\u036c\u036d")
        buf.write("\7R\2\2\u036d\u036e\7u\2\2\u036e\u0370\7k\2\2\u036f\u0367")
        buf.write("\3\2\2\2\u036f\u036b\3\2\2\2\u0370\u00ba\3\2\2\2\u0371")
        buf.write("\u0372\7^\2\2\u0372\u0373\7q\2\2\u0373\u0374\7o\2\2\u0374")
        buf.write("\u0375\7g\2\2\u0375\u0376\7i\2\2\u0376\u037e\7c\2\2\u0377")
        buf.write("\u0378\7^\2\2\u0378\u0379\7Q\2\2\u0379\u037a\7o\2\2\u037a")
        buf.write("\u037b\7g\2\2\u037b\u037c\7i\2\2\u037c\u037e\7c\2\2\u037d")
        buf.write("\u0371\3\2\2\2\u037d\u0377\3\2\2\2\u037e\u00bc\3\2\2\2")
        buf.write("\u037f\u0398\5\u008dG\2\u0380\u0398\5\u008fH\2\u0381\u0398")
        buf.write("\5\u0091I\2\u0382\u0398\5\u0093J\2\u0383\u0398\5\u0095")
        buf.write("K\2\u0384\u0398\5\u0097L\2\u0385\u0398\5\u0099M\2\u0386")
        buf.write("\u0398\5\u009bN\2\u0387\u0398\5\u009dO\2\u0388\u0398\5")
        buf.write("\u009fP\2\u0389\u0398\5\u00a1Q\2\u038a\u0398\5\u00a3R")
        buf.write("\2\u038b\u0398\5\u00a5S\2\u038c\u0398\5\u00a7T\2\u038d")
        buf.write("\u0398\5\u00a9U\2\u038e\u0398\5\u00abV\2\u038f\u0398\5")
        buf.write("\u00adW\2\u0390\u0398\5\u00afX\2\u0391\u0398\5\u00b1Y")
        buf.write("\2\u0392\u0398\5\u00b3Z\2\u0393\u0398\5\u00b5[\2\u0394")
        buf.write("\u0398\5\u00b7\\\2\u0395\u0398\5\u00b9]\2\u0396\u0398")
        buf.write("\5\u00bb^\2\u0397\u037f\3\2\2\2\u0397\u0380\3\2\2\2\u0397")
        buf.write("\u0381\3\2\2\2\u0397\u0382\3\2\2\2\u0397\u0383\3\2\2\2")
        buf.write("\u0397\u0384\3\2\2\2\u0397\u0385\3\2\2\2\u0397\u0386\3")
        buf.write("\2\2\2\u0397\u0387\3\2\2\2\u0397\u0388\3\2\2\2\u0397\u0389")
        buf.write("\3\2\2\2\u0397\u038a\3\2\2\2\u0397\u038b\3\2\2\2\u0397")
        buf.write("\u038c\3\2\2\2\u0397\u038d\3\2\2\2\u0397\u038e\3\2\2\2")
        buf.write("\u0397\u038f\3\2\2\2\u0397\u0390\3\2\2\2\u0397\u0391\3")
        buf.write("\2\2\2\u0397\u0392\3\2\2\2\u0397\u0393\3\2\2\2\u0397\u0394")
        buf.write("\3\2\2\2\u0397\u0395\3\2\2\2\u0397\u0396\3\2\2\2\u0398")
        buf.write("\u00be\3\2\2\2\u0399\u039a\5\35\17\2\u039a\u039e\5\17")
        buf.write("\b\2\u039b\u039f\5y=\2\u039c\u039f\5u;\2\u039d\u039f\5")
        buf.write("\u00bd_\2\u039e\u039b\3\2\2\2\u039e\u039c\3\2\2\2\u039e")
        buf.write("\u039d\3\2\2\2\u039f\u03a0\3\2\2\2\u03a0\u03a1\5\21\t")
        buf.write("\2\u03a1\u00c0\3\2\2\2\u03a2\u03a4\5q9\2\u03a3\u03a5\5")
        buf.write("\u00bf`\2\u03a4\u03a3\3\2\2\2\u03a4\u03a5\3\2\2\2\u03a5")
        buf.write("\u03a6\3\2\2\2\u03a6\u03a7\5\17\b\2\u03a7\u00c2\3\2\2")
        buf.write("\2\u03a8\u03aa\5q9\2\u03a9\u03ab\5\u00bf`\2\u03aa\u03a9")
        buf.write("\3\2\2\2\u03aa\u03ab\3\2\2\2\u03ab\u03ac\3\2\2\2\u03ac")
        buf.write("\u03ad\5\13\6\2\u03ad\u00c4\3\2\2\2\u03ae\u03b0\5\u00bd")
        buf.write("_\2\u03af\u03b1\5\u00bf`\2\u03b0\u03af\3\2\2\2\u03b0\u03b1")
        buf.write("\3\2\2\2\u03b1\u03b2\3\2\2\2\u03b2\u03b3\5\17\b\2\u03b3")
        buf.write("\u00c6\3\2\2\2\u03b4\u03b6\5\u00bd_\2\u03b5\u03b7\5\u00bf")
        buf.write("`\2\u03b6\u03b5\3\2\2\2\u03b6\u03b7\3\2\2\2\u03b7\u03b8")
        buf.write("\3\2\2\2\u03b8\u03b9\5\13\6\2\u03b9\u00c8\3\2\2\2\u03ba")
        buf.write("\u03bc\t\6\2\2\u03bb\u03ba\3\2\2\2\u03bc\u03bd\3\2\2\2")
        buf.write("\u03bd\u03bb\3\2\2\2\u03bd\u03be\3\2\2\2\u03be\u03bf\3")
        buf.write("\2\2\2\u03bf\u03c0\be\2\2\u03c0\u00ca\3\2\2\2G\2\u0129")
        buf.write("\u0140\u0147\u014d\u0154\u015b\u0162\u0169\u0170\u0177")
        buf.write("\u017d\u0183\u0189\u018f\u0195\u019b\u01a3\u01ab\u01b3")
        buf.write("\u01b9\u01bf\u01c5\u01cb\u01d1\u01d7\u01dd\u01e3\u01e9")
        buf.write("\u01f1\u0218\u021c\u0221\u0225\u022a\u022c\u0237\u023c")
        buf.write("\u0263\u026f\u027d\u028b\u029d\u02a9\u02b3\u02c1\u02cd")
        buf.write("\u02db\u02eb\u02f3\u02fb\u0303\u0315\u031d\u0327\u0335")
        buf.write("\u033f\u0351\u035b\u0365\u036f\u037d\u0397\u039e\u03a4")
        buf.write("\u03aa\u03b0\u03b6\u03bd\3\b\2\2")
        return buf.getvalue()


class MatexLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    MUL = 3
    DIV = 4
    L_PAREN = 5
    R_PAREN = 6
    L_BRACE = 7
    R_BRACE = 8
    L_BRACKET = 9
    R_BRACKET = 10
    COMMA = 11
    DOT = 12
    BAR = 13
    UNDERSCORE = 14
    CARET = 15
    COLON = 16
    FUNC_LIM = 17
    LIM_APPROACH_SYM = 18
    FUNC_INT = 19
    FUNC_SUM = 20
    FUNC_PROD = 21
    FUNC_LOG = 22
    FUNC_LN = 23
    FUNC_SIN = 24
    FUNC_COS = 25
    FUNC_TAN = 26
    FUNC_CSC = 27
    FUNC_SEC = 28
    FUNC_COT = 29
    FUNC_ARCSIN = 30
    FUNC_ARCCOS = 31
    FUNC_ARCTAN = 32
    FUNC_ARCCSC = 33
    FUNC_ARCSEC = 34
    FUNC_ARCCOT = 35
    FUNC_SINH = 36
    FUNC_COSH = 37
    FUNC_TANH = 38
    FUNC_ARCSINH = 39
    FUNC_ARCCOSH = 40
    FUNC_ARCTANH = 41
    FUNC_ECOS = 42
    FUNC_ESIN = 43
    FUNC_EDELTAAMPLITUDE = 44
    FUNC_ARCECOS = 45
    FUNC_ARCESIN = 46
    FUNC_ARCEDELTAAMPLITUDE = 47
    FUNC_SQRT = 48
    FUNC_BINOMIAL = 49
    CMD_TIMES = 50
    CMD_CDOT = 51
    CMD_DIV = 52
    CMD_FRAC = 53
    NUMBER = 54
    DERIVATIVE = 55
    VARIABLE = 56
    MIXNUMBER = 57
    WORD = 58
    INFINITY = 59
    EQ = 60
    LT = 61
    LTE = 62
    GT = 63
    GTE = 64
    BANG = 65
    GREEKLETTER = 66
    LETTERFUNCTIONBRACE = 67
    LETTERFUNCTIONPAREN = 68
    GREEKFUNCTIONBRACE = 69
    GREEKFUNCTIONPAREN = 70
    WS = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "'.'", "'|'", "'_'", "'^'", "':'", "'\\lim'", 
            "'\\int'", "'\\sum'", "'\\prod'", "'\\times'", "'\\cdot'", "'\\div'", 
            "'\\frac'", "'\\infty'", "'='", "'<'", "'\\leq'", "'>'", "'\\geq'", 
            "'!'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MUL", "DIV", "L_PAREN", "R_PAREN", "L_BRACE", 
            "R_BRACE", "L_BRACKET", "R_BRACKET", "COMMA", "DOT", "BAR", 
            "UNDERSCORE", "CARET", "COLON", "FUNC_LIM", "LIM_APPROACH_SYM", 
            "FUNC_INT", "FUNC_SUM", "FUNC_PROD", "FUNC_LOG", "FUNC_LN", 
            "FUNC_SIN", "FUNC_COS", "FUNC_TAN", "FUNC_CSC", "FUNC_SEC", 
            "FUNC_COT", "FUNC_ARCSIN", "FUNC_ARCCOS", "FUNC_ARCTAN", "FUNC_ARCCSC", 
            "FUNC_ARCSEC", "FUNC_ARCCOT", "FUNC_SINH", "FUNC_COSH", "FUNC_TANH", 
            "FUNC_ARCSINH", "FUNC_ARCCOSH", "FUNC_ARCTANH", "FUNC_ECOS", 
            "FUNC_ESIN", "FUNC_EDELTAAMPLITUDE", "FUNC_ARCECOS", "FUNC_ARCESIN", 
            "FUNC_ARCEDELTAAMPLITUDE", "FUNC_SQRT", "FUNC_BINOMIAL", "CMD_TIMES", 
            "CMD_CDOT", "CMD_DIV", "CMD_FRAC", "NUMBER", "DERIVATIVE", "VARIABLE", 
            "MIXNUMBER", "WORD", "INFINITY", "EQ", "LT", "LTE", "GT", "GTE", 
            "BANG", "GREEKLETTER", "LETTERFUNCTIONBRACE", "LETTERFUNCTIONPAREN", 
            "GREEKFUNCTIONBRACE", "GREEKFUNCTIONPAREN", "WS" ]

    ruleNames = [ "PLUS", "MINUS", "MUL", "DIV", "L_PAREN", "R_PAREN", "L_BRACE", 
                  "R_BRACE", "L_BRACKET", "R_BRACKET", "COMMA", "DOT", "BAR", 
                  "UNDERSCORE", "CARET", "COLON", "BACKSLASH", "FUNC_LIM", 
                  "LIM_APPROACH_SYM", "FUNC_INT", "FUNC_SUM", "FUNC_PROD", 
                  "ARC", "FUNC_LOG", "FUNC_LN", "FUNC_SIN", "FUNC_COS", 
                  "FUNC_TAN", "FUNC_CSC", "FUNC_SEC", "FUNC_COT", "FUNC_ARCSIN", 
                  "FUNC_ARCCOS", "FUNC_ARCTAN", "FUNC_ARCCSC", "FUNC_ARCSEC", 
                  "FUNC_ARCCOT", "FUNC_SINH", "FUNC_COSH", "FUNC_TANH", 
                  "FUNC_ARCSINH", "FUNC_ARCCOSH", "FUNC_ARCTANH", "FUNC_ECOS", 
                  "FUNC_ESIN", "FUNC_EDELTAAMPLITUDE", "FUNC_ARCECOS", "FUNC_ARCESIN", 
                  "FUNC_ARCEDELTAAMPLITUDE", "FUNC_SQRT", "FUNC_BINOMIAL", 
                  "CMD_TIMES", "CMD_CDOT", "CMD_DIV", "CMD_FRAC", "LETTER", 
                  "DIGIT", "NUMBER", "DERIVATIVE", "VARIABLE", "MIXNUMBER", 
                  "WORD", "INFINITY", "EQ", "LT", "LTE", "GT", "GTE", "BANG", 
                  "ALPHA", "BETA", "GAMMA", "DELTA", "EPSILON", "ZETA", 
                  "ETA", "THETA", "IOTA", "KAPPA", "LAMBDA", "MU", "NU", 
                  "XI", "OMICRON", "PI", "RHO", "SIGMA", "TAU", "UPSILON", 
                  "PHI", "CHI", "PSI", "OMEGA", "GREEKLETTER", "INDICED", 
                  "LETTERFUNCTIONBRACE", "LETTERFUNCTIONPAREN", "GREEKFUNCTIONBRACE", 
                  "GREEKFUNCTIONPAREN", "WS" ]

    grammarFileName = "MatexLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


