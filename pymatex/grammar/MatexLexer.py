# Generated from .\pymatex\grammar\MatexLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u03a0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0124\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\5\31\u013b\n\31\3\31\3\31\3\31\3\31\3\32\5\32\u0142\n")
        buf.write("\32\3\32\3\32\3\32\3\33\5\33\u0148\n\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\5\34\u014f\n\34\3\34\3\34\3\34\3\34\3\35\5")
        buf.write("\35\u0156\n\35\3\35\3\35\3\35\3\35\3\36\5\36\u015d\n\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\5\37\u0164\n\37\3\37\3\37\3")
        buf.write("\37\3\37\3 \5 \u016b\n \3 \3 \3 \3 \3!\5!\u0172\n!\3!")
        buf.write("\3!\3!\3\"\5\"\u0178\n\"\3\"\3\"\3\"\3#\5#\u017e\n#\3")
        buf.write("#\3#\3#\3$\5$\u0184\n$\3$\3$\3$\3%\5%\u018a\n%\3%\3%\3")
        buf.write("%\3&\5&\u0190\n&\3&\3&\3&\3\'\5\'\u0196\n\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3(\5(\u019e\n(\3(\3(\3(\3(\3(\3)\5)\u01a6\n")
        buf.write(")\3)\3)\3)\3)\3)\3*\5*\u01ae\n*\3*\3*\3*\3+\5+\u01b4\n")
        buf.write("+\3+\3+\3+\3,\5,\u01ba\n,\3,\3,\3,\3-\5-\u01c0\n-\3-\3")
        buf.write("-\3-\3.\5.\u01c6\n.\3.\3.\3.\3/\5/\u01cc\n/\3/\3/\3/\3")
        buf.write("\60\5\60\u01d2\n\60\3\60\3\60\3\60\3\61\5\61\u01d8\n\61")
        buf.write("\3\61\3\61\3\61\3\62\5\62\u01de\n\62\3\62\3\62\3\62\3")
        buf.write("\63\5\63\u01e4\n\63\3\63\3\63\3\63\3\63\3\63\3\64\5\64")
        buf.write("\u01ec\n\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\39\39\3:\3")
        buf.write(":\3;\7;\u0211\n;\f;\16;\u0214\13;\3;\5;\u0217\n;\3;\6")
        buf.write(";\u021a\n;\r;\16;\u021b\3;\3;\5;\u0220\n;\3;\6;\u0223")
        buf.write("\n;\r;\16;\u0224\5;\u0227\n;\3<\3<\3<\3=\3=\3>\3>\6>\u0230")
        buf.write("\n>\r>\16>\u0231\3?\6?\u0235\n?\r?\16?\u0236\3@\3@\3@")
        buf.write("\3@\3@\3@\3@\3A\3A\3B\3B\3C\3C\3C\3C\3C\3D\3D\3E\3E\3")
        buf.write("E\3E\3E\3F\3F\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u025e")
        buf.write("\nG\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\5H\u026a\nH\3I\3I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u0278\nI\3J\3J\3J\3J\3")
        buf.write("J\3J\3J\3J\3J\3J\3J\3J\5J\u0286\nJ\3K\3K\3K\3K\3K\3K\3")
        buf.write("K\3K\3K\3K\3K\3K\3K\3K\3K\3K\5K\u0298\nK\3L\3L\3L\3L\3")
        buf.write("L\3L\3L\3L\3L\3L\5L\u02a4\nL\3M\3M\3M\3M\3M\3M\3M\3M\5")
        buf.write("M\u02ae\nM\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\5N\u02bc")
        buf.write("\nN\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u02c8\nO\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u02d6\nP\3Q\3Q\3Q\3Q\3")
        buf.write("Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u02e6\nQ\3R\3R\3R\3R\3")
        buf.write("R\3R\5R\u02ee\nR\3S\3S\3S\3S\3S\3S\5S\u02f6\nS\3T\3T\3")
        buf.write("T\3T\3T\3T\5T\u02fe\nT\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\5U\u0310\nU\3V\3V\3V\3V\3V\3V\5V\u0318")
        buf.write("\nV\3W\3W\3W\3W\3W\3W\3W\3W\5W\u0322\nW\3X\3X\3X\3X\3")
        buf.write("X\3X\3X\3X\3X\3X\3X\3X\5X\u0330\nX\3Y\3Y\3Y\3Y\3Y\3Y\3")
        buf.write("Y\3Y\5Y\u033a\nY\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3")
        buf.write("Z\3Z\3Z\3Z\5Z\u034c\nZ\3[\3[\3[\3[\3[\3[\3[\3[\5[\u0356")
        buf.write("\n[\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\5\\\u0360\n\\\3]\3")
        buf.write("]\3]\3]\3]\3]\3]\3]\5]\u036a\n]\3^\3^\3^\3^\3^\3^\3^\3")
        buf.write("^\3^\3^\3^\3^\5^\u0378\n^\3_\3_\3_\3_\3_\3_\3_\3_\3_\3")
        buf.write("_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\5_\u0392\n")
        buf.write("_\3`\3`\3`\3a\3a\3a\3b\6b\u039b\nb\rb\16b\u039c\3b\3b")
        buf.write("\2\2c\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\2%\23\'\24)\25+\26-\27")
        buf.write("/\2\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I")
        buf.write("$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o")
        buf.write("\67q\2s\2u8w9y:{;}<\177=\u0081>\u0083?\u0085@\u0087A\u0089")
        buf.write("B\u008bC\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5")
        buf.write("\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3")
        buf.write("\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bdD\u00bfE\u00c1")
        buf.write("F\u00c3G\3\2\7\4\2C\\c|\3\2\62;\4\2GGgg\4\2--//\5\2\13")
        buf.write("\f\17\17\"\"\2\u03db\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2u\3\2")
        buf.write("\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u00bd")
        buf.write("\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2")
        buf.write("\2\3\u00c5\3\2\2\2\5\u00c7\3\2\2\2\7\u00c9\3\2\2\2\t\u00cb")
        buf.write("\3\2\2\2\13\u00cd\3\2\2\2\r\u00cf\3\2\2\2\17\u00d1\3\2")
        buf.write("\2\2\21\u00d3\3\2\2\2\23\u00d5\3\2\2\2\25\u00d7\3\2\2")
        buf.write("\2\27\u00d9\3\2\2\2\31\u00db\3\2\2\2\33\u00dd\3\2\2\2")
        buf.write("\35\u00df\3\2\2\2\37\u00e1\3\2\2\2!\u00e3\3\2\2\2#\u00e5")
        buf.write("\3\2\2\2%\u00e7\3\2\2\2\'\u0123\3\2\2\2)\u0125\3\2\2\2")
        buf.write("+\u012a\3\2\2\2-\u012f\3\2\2\2/\u0135\3\2\2\2\61\u013a")
        buf.write("\3\2\2\2\63\u0141\3\2\2\2\65\u0147\3\2\2\2\67\u014e\3")
        buf.write("\2\2\29\u0155\3\2\2\2;\u015c\3\2\2\2=\u0163\3\2\2\2?\u016a")
        buf.write("\3\2\2\2A\u0171\3\2\2\2C\u0177\3\2\2\2E\u017d\3\2\2\2")
        buf.write("G\u0183\3\2\2\2I\u0189\3\2\2\2K\u018f\3\2\2\2M\u0195\3")
        buf.write("\2\2\2O\u019d\3\2\2\2Q\u01a5\3\2\2\2S\u01ad\3\2\2\2U\u01b3")
        buf.write("\3\2\2\2W\u01b9\3\2\2\2Y\u01bf\3\2\2\2[\u01c5\3\2\2\2")
        buf.write("]\u01cb\3\2\2\2_\u01d1\3\2\2\2a\u01d7\3\2\2\2c\u01dd\3")
        buf.write("\2\2\2e\u01e3\3\2\2\2g\u01eb\3\2\2\2i\u01f3\3\2\2\2k\u01fa")
        buf.write("\3\2\2\2m\u0200\3\2\2\2o\u0205\3\2\2\2q\u020b\3\2\2\2")
        buf.write("s\u020d\3\2\2\2u\u0212\3\2\2\2w\u0228\3\2\2\2y\u022b\3")
        buf.write("\2\2\2{\u022d\3\2\2\2}\u0234\3\2\2\2\177\u0238\3\2\2\2")
        buf.write("\u0081\u023f\3\2\2\2\u0083\u0241\3\2\2\2\u0085\u0243\3")
        buf.write("\2\2\2\u0087\u0248\3\2\2\2\u0089\u024a\3\2\2\2\u008b\u024f")
        buf.write("\3\2\2\2\u008d\u025d\3\2\2\2\u008f\u0269\3\2\2\2\u0091")
        buf.write("\u0277\3\2\2\2\u0093\u0285\3\2\2\2\u0095\u0297\3\2\2\2")
        buf.write("\u0097\u02a3\3\2\2\2\u0099\u02ad\3\2\2\2\u009b\u02bb\3")
        buf.write("\2\2\2\u009d\u02c7\3\2\2\2\u009f\u02d5\3\2\2\2\u00a1\u02e5")
        buf.write("\3\2\2\2\u00a3\u02ed\3\2\2\2\u00a5\u02f5\3\2\2\2\u00a7")
        buf.write("\u02fd\3\2\2\2\u00a9\u030f\3\2\2\2\u00ab\u0317\3\2\2\2")
        buf.write("\u00ad\u0321\3\2\2\2\u00af\u032f\3\2\2\2\u00b1\u0339\3")
        buf.write("\2\2\2\u00b3\u034b\3\2\2\2\u00b5\u0355\3\2\2\2\u00b7\u035f")
        buf.write("\3\2\2\2\u00b9\u0369\3\2\2\2\u00bb\u0377\3\2\2\2\u00bd")
        buf.write("\u0391\3\2\2\2\u00bf\u0393\3\2\2\2\u00c1\u0396\3\2\2\2")
        buf.write("\u00c3\u039a\3\2\2\2\u00c5\u00c6\7-\2\2\u00c6\4\3\2\2")
        buf.write("\2\u00c7\u00c8\7/\2\2\u00c8\6\3\2\2\2\u00c9\u00ca\7,\2")
        buf.write("\2\u00ca\b\3\2\2\2\u00cb\u00cc\7\61\2\2\u00cc\n\3\2\2")
        buf.write("\2\u00cd\u00ce\7*\2\2\u00ce\f\3\2\2\2\u00cf\u00d0\7+\2")
        buf.write("\2\u00d0\16\3\2\2\2\u00d1\u00d2\7}\2\2\u00d2\20\3\2\2")
        buf.write("\2\u00d3\u00d4\7\177\2\2\u00d4\22\3\2\2\2\u00d5\u00d6")
        buf.write("\7]\2\2\u00d6\24\3\2\2\2\u00d7\u00d8\7_\2\2\u00d8\26\3")
        buf.write("\2\2\2\u00d9\u00da\7.\2\2\u00da\30\3\2\2\2\u00db\u00dc")
        buf.write("\7\60\2\2\u00dc\32\3\2\2\2\u00dd\u00de\7~\2\2\u00de\34")
        buf.write("\3\2\2\2\u00df\u00e0\7a\2\2\u00e0\36\3\2\2\2\u00e1\u00e2")
        buf.write("\7`\2\2\u00e2 \3\2\2\2\u00e3\u00e4\7<\2\2\u00e4\"\3\2")
        buf.write("\2\2\u00e5\u00e6\7^\2\2\u00e6$\3\2\2\2\u00e7\u00e8\7^")
        buf.write("\2\2\u00e8\u00e9\7n\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7o\2\2\u00eb&\3\2\2\2\u00ec\u00ed\7^\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\u0124\7q\2\2\u00ef\u00f0\7^\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7i\2\2\u00f3\u00f4")
        buf.write("\7j\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7q\2\2\u00f9\u0124")
        buf.write("\7y\2\2\u00fa\u00fb\7^\2\2\u00fb\u00fc\7T\2\2\u00fc\u00fd")
        buf.write("\7k\2\2\u00fd\u00fe\7i\2\2\u00fe\u00ff\7j\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100\u0101\7c\2\2\u0101\u0102\7t\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7q\2\2\u0104\u0124\7y\2\2\u0105\u0106")
        buf.write("\7^\2\2\u0106\u0107\7n\2\2\u0107\u0108\7q\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\u010a\7i\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7k\2\2\u010c\u010d\7i\2\2\u010d\u010e\7j\2\2\u010e\u010f")
        buf.write("\7v\2\2\u010f\u0110\7c\2\2\u0110\u0111\7t\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\u0113\7q\2\2\u0113\u0124\7y\2\2\u0114\u0115")
        buf.write("\7^\2\2\u0115\u0116\7N\2\2\u0116\u0117\7q\2\2\u0117\u0118")
        buf.write("\7p\2\2\u0118\u0119\7i\2\2\u0119\u011a\7t\2\2\u011a\u011b")
        buf.write("\7k\2\2\u011b\u011c\7i\2\2\u011c\u011d\7j\2\2\u011d\u011e")
        buf.write("\7v\2\2\u011e\u011f\7c\2\2\u011f\u0120\7t\2\2\u0120\u0121")
        buf.write("\7t\2\2\u0121\u0122\7q\2\2\u0122\u0124\7y\2\2\u0123\u00ec")
        buf.write("\3\2\2\2\u0123\u00ef\3\2\2\2\u0123\u00fa\3\2\2\2\u0123")
        buf.write("\u0105\3\2\2\2\u0123\u0114\3\2\2\2\u0124(\3\2\2\2\u0125")
        buf.write("\u0126\7^\2\2\u0126\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128")
        buf.write("\u0129\7v\2\2\u0129*\3\2\2\2\u012a\u012b\7^\2\2\u012b")
        buf.write("\u012c\7u\2\2\u012c\u012d\7w\2\2\u012d\u012e\7o\2\2\u012e")
        buf.write(",\3\2\2\2\u012f\u0130\7^\2\2\u0130\u0131\7r\2\2\u0131")
        buf.write("\u0132\7t\2\2\u0132\u0133\7q\2\2\u0133\u0134\7f\2\2\u0134")
        buf.write(".\3\2\2\2\u0135\u0136\7c\2\2\u0136\u0137\7t\2\2\u0137")
        buf.write("\u0138\7e\2\2\u0138\60\3\2\2\2\u0139\u013b\5#\22\2\u013a")
        buf.write("\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013c\u013d\7n\2\2\u013d\u013e\7q\2\2\u013e\u013f\7i")
        buf.write("\2\2\u013f\62\3\2\2\2\u0140\u0142\5#\22\2\u0141\u0140")
        buf.write("\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\3\2\2\2\u0143")
        buf.write("\u0144\7n\2\2\u0144\u0145\7p\2\2\u0145\64\3\2\2\2\u0146")
        buf.write("\u0148\5#\22\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149\u014a\7u\2\2\u014a\u014b\7")
        buf.write("k\2\2\u014b\u014c\7p\2\2\u014c\66\3\2\2\2\u014d\u014f")
        buf.write("\5#\22\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0151\7e\2\2\u0151\u0152\7q\2\2\u0152")
        buf.write("\u0153\7u\2\2\u01538\3\2\2\2\u0154\u0156\5#\22\2\u0155")
        buf.write("\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157\u0158\7v\2\2\u0158\u0159\7c\2\2\u0159\u015a\7p")
        buf.write("\2\2\u015a:\3\2\2\2\u015b\u015d\5#\22\2\u015c\u015b\3")
        buf.write("\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f")
        buf.write("\7e\2\2\u015f\u0160\7u\2\2\u0160\u0161\7e\2\2\u0161<\3")
        buf.write("\2\2\2\u0162\u0164\5#\22\2\u0163\u0162\3\2\2\2\u0163\u0164")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\7u\2\2\u0166")
        buf.write("\u0167\7g\2\2\u0167\u0168\7e\2\2\u0168>\3\2\2\2\u0169")
        buf.write("\u016b\5#\22\2\u016a\u0169\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016c\3\2\2\2\u016c\u016d\7e\2\2\u016d\u016e\7")
        buf.write("q\2\2\u016e\u016f\7v\2\2\u016f@\3\2\2\2\u0170\u0172\5")
        buf.write("#\22\2\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0174\5/\30\2\u0174\u0175\5\65\33\2\u0175")
        buf.write("B\3\2\2\2\u0176\u0178\5#\22\2\u0177\u0176\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\5/\30\2")
        buf.write("\u017a\u017b\5\67\34\2\u017bD\3\2\2\2\u017c\u017e\5#\22")
        buf.write("\2\u017d\u017c\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f")
        buf.write("\3\2\2\2\u017f\u0180\5/\30\2\u0180\u0181\59\35\2\u0181")
        buf.write("F\3\2\2\2\u0182\u0184\5#\22\2\u0183\u0182\3\2\2\2\u0183")
        buf.write("\u0184\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\5/\30\2")
        buf.write("\u0186\u0187\5;\36\2\u0187H\3\2\2\2\u0188\u018a\5#\22")
        buf.write("\2\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b")
        buf.write("\3\2\2\2\u018b\u018c\5/\30\2\u018c\u018d\5=\37\2\u018d")
        buf.write("J\3\2\2\2\u018e\u0190\5#\22\2\u018f\u018e\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0192\5/\30\2")
        buf.write("\u0192\u0193\5? \2\u0193L\3\2\2\2\u0194\u0196\5#\22\2")
        buf.write("\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197\u0198\7u\2\2\u0198\u0199\7k\2\2\u0199\u019a")
        buf.write("\7p\2\2\u019a\u019b\7j\2\2\u019bN\3\2\2\2\u019c\u019e")
        buf.write("\5#\22\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\7e\2\2\u01a0\u01a1\7q\2\2\u01a1")
        buf.write("\u01a2\7u\2\2\u01a2\u01a3\7j\2\2\u01a3P\3\2\2\2\u01a4")
        buf.write("\u01a6\5#\22\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7\u01a8\7v\2\2\u01a8\u01a9\7")
        buf.write("c\2\2\u01a9\u01aa\7p\2\2\u01aa\u01ab\7j\2\2\u01abR\3\2")
        buf.write("\2\2\u01ac\u01ae\5#\22\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\5/\30\2\u01b0")
        buf.write("\u01b1\5M\'\2\u01b1T\3\2\2\2\u01b2\u01b4\5#\22\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b6\5/\30\2\u01b6\u01b7\5O(\2\u01b7V\3\2\2\2")
        buf.write("\u01b8\u01ba\5#\22\2\u01b9\u01b8\3\2\2\2\u01b9\u01ba\3")
        buf.write("\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\5/\30\2\u01bc\u01bd")
        buf.write("\5Q)\2\u01bdX\3\2\2\2\u01be\u01c0\5#\22\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("\u01c2\7e\2\2\u01c2\u01c3\7p\2\2\u01c3Z\3\2\2\2\u01c4")
        buf.write("\u01c6\5#\22\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c7\3\2\2\2\u01c7\u01c8\7u\2\2\u01c8\u01c9\7")
        buf.write("p\2\2\u01c9\\\3\2\2\2\u01ca\u01cc\5#\22\2\u01cb\u01ca")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("\u01ce\7f\2\2\u01ce\u01cf\7p\2\2\u01cf^\3\2\2\2\u01d0")
        buf.write("\u01d2\5#\22\2\u01d1\u01d0\3\2\2\2\u01d1\u01d2\3\2\2\2")
        buf.write("\u01d2\u01d3\3\2\2\2\u01d3\u01d4\5/\30\2\u01d4\u01d5\5")
        buf.write("Y-\2\u01d5`\3\2\2\2\u01d6\u01d8\5#\22\2\u01d7\u01d6\3")
        buf.write("\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da")
        buf.write("\5/\30\2\u01da\u01db\5[.\2\u01dbb\3\2\2\2\u01dc\u01de")
        buf.write("\5#\22\2\u01dd\u01dc\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01e0\5/\30\2\u01e0\u01e1\5]/\2\u01e1")
        buf.write("d\3\2\2\2\u01e2\u01e4\5#\22\2\u01e3\u01e2\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\7u\2\2")
        buf.write("\u01e6\u01e7\7s\2\2\u01e7\u01e8\7t\2\2\u01e8\u01e9\7v")
        buf.write("\2\2\u01e9f\3\2\2\2\u01ea\u01ec\5#\22\2\u01eb\u01ea\3")
        buf.write("\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ee")
        buf.write("\7d\2\2\u01ee\u01ef\7k\2\2\u01ef\u01f0\7p\2\2\u01f0\u01f1")
        buf.write("\7q\2\2\u01f1\u01f2\7o\2\2\u01f2h\3\2\2\2\u01f3\u01f4")
        buf.write("\7^\2\2\u01f4\u01f5\7v\2\2\u01f5\u01f6\7k\2\2\u01f6\u01f7")
        buf.write("\7o\2\2\u01f7\u01f8\7g\2\2\u01f8\u01f9\7u\2\2\u01f9j\3")
        buf.write("\2\2\2\u01fa\u01fb\7^\2\2\u01fb\u01fc\7e\2\2\u01fc\u01fd")
        buf.write("\7f\2\2\u01fd\u01fe\7q\2\2\u01fe\u01ff\7v\2\2\u01ffl\3")
        buf.write("\2\2\2\u0200\u0201\7^\2\2\u0201\u0202\7f\2\2\u0202\u0203")
        buf.write("\7k\2\2\u0203\u0204\7x\2\2\u0204n\3\2\2\2\u0205\u0206")
        buf.write("\7^\2\2\u0206\u0207\7h\2\2\u0207\u0208\7t\2\2\u0208\u0209")
        buf.write("\7c\2\2\u0209\u020a\7e\2\2\u020ap\3\2\2\2\u020b\u020c")
        buf.write("\t\2\2\2\u020cr\3\2\2\2\u020d\u020e\t\3\2\2\u020et\3\2")
        buf.write("\2\2\u020f\u0211\5s:\2\u0210\u020f\3\2\2\2\u0211\u0214")
        buf.write("\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213")
        buf.write("\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0215\u0217\7\60\2")
        buf.write("\2\u0216\u0215\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0219")
        buf.write("\3\2\2\2\u0218\u021a\5s:\2\u0219\u0218\3\2\2\2\u021a\u021b")
        buf.write("\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c")
        buf.write("\u0226\3\2\2\2\u021d\u021f\t\4\2\2\u021e\u0220\t\5\2\2")
        buf.write("\u021f\u021e\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0222\3")
        buf.write("\2\2\2\u0221\u0223\5s:\2\u0222\u0221\3\2\2\2\u0223\u0224")
        buf.write("\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225")
        buf.write("\u0227\3\2\2\2\u0226\u021d\3\2\2\2\u0226\u0227\3\2\2\2")
        buf.write("\u0227v\3\2\2\2\u0228\u0229\7f\2\2\u0229\u022a\5q9\2\u022a")
        buf.write("x\3\2\2\2\u022b\u022c\5q9\2\u022cz\3\2\2\2\u022d\u022f")
        buf.write("\5u;\2\u022e\u0230\5y=\2\u022f\u022e\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232")
        buf.write("|\3\2\2\2\u0233\u0235\5y=\2\u0234\u0233\3\2\2\2\u0235")
        buf.write("\u0236\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2")
        buf.write("\u0237~\3\2\2\2\u0238\u0239\7^\2\2\u0239\u023a\7k\2\2")
        buf.write("\u023a\u023b\7p\2\2\u023b\u023c\7h\2\2\u023c\u023d\7v")
        buf.write("\2\2\u023d\u023e\7{\2\2\u023e\u0080\3\2\2\2\u023f\u0240")
        buf.write("\7?\2\2\u0240\u0082\3\2\2\2\u0241\u0242\7>\2\2\u0242\u0084")
        buf.write("\3\2\2\2\u0243\u0244\7^\2\2\u0244\u0245\7n\2\2\u0245\u0246")
        buf.write("\7g\2\2\u0246\u0247\7s\2\2\u0247\u0086\3\2\2\2\u0248\u0249")
        buf.write("\7@\2\2\u0249\u0088\3\2\2\2\u024a\u024b\7^\2\2\u024b\u024c")
        buf.write("\7i\2\2\u024c\u024d\7g\2\2\u024d\u024e\7s\2\2\u024e\u008a")
        buf.write("\3\2\2\2\u024f\u0250\7#\2\2\u0250\u008c\3\2\2\2\u0251")
        buf.write("\u0252\7^\2\2\u0252\u0253\7c\2\2\u0253\u0254\7n\2\2\u0254")
        buf.write("\u0255\7r\2\2\u0255\u0256\7j\2\2\u0256\u025e\7c\2\2\u0257")
        buf.write("\u0258\7^\2\2\u0258\u0259\7C\2\2\u0259\u025a\7n\2\2\u025a")
        buf.write("\u025b\7r\2\2\u025b\u025c\7j\2\2\u025c\u025e\7c\2\2\u025d")
        buf.write("\u0251\3\2\2\2\u025d\u0257\3\2\2\2\u025e\u008e\3\2\2\2")
        buf.write("\u025f\u0260\7^\2\2\u0260\u0261\7d\2\2\u0261\u0262\7g")
        buf.write("\2\2\u0262\u0263\7v\2\2\u0263\u026a\7c\2\2\u0264\u0265")
        buf.write("\7^\2\2\u0265\u0266\7D\2\2\u0266\u0267\7g\2\2\u0267\u0268")
        buf.write("\7v\2\2\u0268\u026a\7c\2\2\u0269\u025f\3\2\2\2\u0269\u0264")
        buf.write("\3\2\2\2\u026a\u0090\3\2\2\2\u026b\u026c\7^\2\2\u026c")
        buf.write("\u026d\7i\2\2\u026d\u026e\7c\2\2\u026e\u026f\7o\2\2\u026f")
        buf.write("\u0270\7o\2\2\u0270\u0278\7c\2\2\u0271\u0272\7^\2\2\u0272")
        buf.write("\u0273\7I\2\2\u0273\u0274\7c\2\2\u0274\u0275\7o\2\2\u0275")
        buf.write("\u0276\7o\2\2\u0276\u0278\7c\2\2\u0277\u026b\3\2\2\2\u0277")
        buf.write("\u0271\3\2\2\2\u0278\u0092\3\2\2\2\u0279\u027a\7^\2\2")
        buf.write("\u027a\u027b\7f\2\2\u027b\u027c\7g\2\2\u027c\u027d\7n")
        buf.write("\2\2\u027d\u027e\7v\2\2\u027e\u0286\7c\2\2\u027f\u0280")
        buf.write("\7^\2\2\u0280\u0281\7F\2\2\u0281\u0282\7g\2\2\u0282\u0283")
        buf.write("\7n\2\2\u0283\u0284\7v\2\2\u0284\u0286\7c\2\2\u0285\u0279")
        buf.write("\3\2\2\2\u0285\u027f\3\2\2\2\u0286\u0094\3\2\2\2\u0287")
        buf.write("\u0288\7^\2\2\u0288\u0289\7g\2\2\u0289\u028a\7r\2\2\u028a")
        buf.write("\u028b\7u\2\2\u028b\u028c\7k\2\2\u028c\u028d\7n\2\2\u028d")
        buf.write("\u028e\7q\2\2\u028e\u0298\7p\2\2\u028f\u0290\7^\2\2\u0290")
        buf.write("\u0291\7G\2\2\u0291\u0292\7r\2\2\u0292\u0293\7u\2\2\u0293")
        buf.write("\u0294\7k\2\2\u0294\u0295\7n\2\2\u0295\u0296\7q\2\2\u0296")
        buf.write("\u0298\7p\2\2\u0297\u0287\3\2\2\2\u0297\u028f\3\2\2\2")
        buf.write("\u0298\u0096\3\2\2\2\u0299\u029a\7^\2\2\u029a\u029b\7")
        buf.write("|\2\2\u029b\u029c\7g\2\2\u029c\u029d\7v\2\2\u029d\u02a4")
        buf.write("\7c\2\2\u029e\u029f\7^\2\2\u029f\u02a0\7\\\2\2\u02a0\u02a1")
        buf.write("\7g\2\2\u02a1\u02a2\7v\2\2\u02a2\u02a4\7c\2\2\u02a3\u0299")
        buf.write("\3\2\2\2\u02a3\u029e\3\2\2\2\u02a4\u0098\3\2\2\2\u02a5")
        buf.write("\u02a6\7^\2\2\u02a6\u02a7\7g\2\2\u02a7\u02a8\7v\2\2\u02a8")
        buf.write("\u02ae\7c\2\2\u02a9\u02aa\7^\2\2\u02aa\u02ab\7G\2\2\u02ab")
        buf.write("\u02ac\7v\2\2\u02ac\u02ae\7c\2\2\u02ad\u02a5\3\2\2\2\u02ad")
        buf.write("\u02a9\3\2\2\2\u02ae\u009a\3\2\2\2\u02af\u02b0\7^\2\2")
        buf.write("\u02b0\u02b1\7v\2\2\u02b1\u02b2\7j\2\2\u02b2\u02b3\7g")
        buf.write("\2\2\u02b3\u02b4\7v\2\2\u02b4\u02bc\7c\2\2\u02b5\u02b6")
        buf.write("\7^\2\2\u02b6\u02b7\7V\2\2\u02b7\u02b8\7j\2\2\u02b8\u02b9")
        buf.write("\7g\2\2\u02b9\u02ba\7v\2\2\u02ba\u02bc\7c\2\2\u02bb\u02af")
        buf.write("\3\2\2\2\u02bb\u02b5\3\2\2\2\u02bc\u009c\3\2\2\2\u02bd")
        buf.write("\u02be\7^\2\2\u02be\u02bf\7k\2\2\u02bf\u02c0\7q\2\2\u02c0")
        buf.write("\u02c1\7v\2\2\u02c1\u02c8\7c\2\2\u02c2\u02c3\7^\2\2\u02c3")
        buf.write("\u02c4\7K\2\2\u02c4\u02c5\7q\2\2\u02c5\u02c6\7v\2\2\u02c6")
        buf.write("\u02c8\7c\2\2\u02c7\u02bd\3\2\2\2\u02c7\u02c2\3\2\2\2")
        buf.write("\u02c8\u009e\3\2\2\2\u02c9\u02ca\7^\2\2\u02ca\u02cb\7")
        buf.write("m\2\2\u02cb\u02cc\7c\2\2\u02cc\u02cd\7r\2\2\u02cd\u02ce")
        buf.write("\7r\2\2\u02ce\u02d6\7c\2\2\u02cf\u02d0\7^\2\2\u02d0\u02d1")
        buf.write("\7M\2\2\u02d1\u02d2\7c\2\2\u02d2\u02d3\7r\2\2\u02d3\u02d4")
        buf.write("\7r\2\2\u02d4\u02d6\7c\2\2\u02d5\u02c9\3\2\2\2\u02d5\u02cf")
        buf.write("\3\2\2\2\u02d6\u00a0\3\2\2\2\u02d7\u02d8\7^\2\2\u02d8")
        buf.write("\u02d9\7n\2\2\u02d9\u02da\7c\2\2\u02da\u02db\7o\2\2\u02db")
        buf.write("\u02dc\7d\2\2\u02dc\u02dd\7f\2\2\u02dd\u02e6\7c\2\2\u02de")
        buf.write("\u02df\7^\2\2\u02df\u02e0\7N\2\2\u02e0\u02e1\7c\2\2\u02e1")
        buf.write("\u02e2\7o\2\2\u02e2\u02e3\7d\2\2\u02e3\u02e4\7f\2\2\u02e4")
        buf.write("\u02e6\7c\2\2\u02e5\u02d7\3\2\2\2\u02e5\u02de\3\2\2\2")
        buf.write("\u02e6\u00a2\3\2\2\2\u02e7\u02e8\7^\2\2\u02e8\u02e9\7")
        buf.write("o\2\2\u02e9\u02ee\7w\2\2\u02ea\u02eb\7^\2\2\u02eb\u02ec")
        buf.write("\7O\2\2\u02ec\u02ee\7w\2\2\u02ed\u02e7\3\2\2\2\u02ed\u02ea")
        buf.write("\3\2\2\2\u02ee\u00a4\3\2\2\2\u02ef\u02f0\7^\2\2\u02f0")
        buf.write("\u02f1\7p\2\2\u02f1\u02f6\7w\2\2\u02f2\u02f3\7^\2\2\u02f3")
        buf.write("\u02f4\7P\2\2\u02f4\u02f6\7w\2\2\u02f5\u02ef\3\2\2\2\u02f5")
        buf.write("\u02f2\3\2\2\2\u02f6\u00a6\3\2\2\2\u02f7\u02f8\7^\2\2")
        buf.write("\u02f8\u02f9\7z\2\2\u02f9\u02fe\7k\2\2\u02fa\u02fb\7^")
        buf.write("\2\2\u02fb\u02fc\7Z\2\2\u02fc\u02fe\7k\2\2\u02fd\u02f7")
        buf.write("\3\2\2\2\u02fd\u02fa\3\2\2\2\u02fe\u00a8\3\2\2\2\u02ff")
        buf.write("\u0300\7^\2\2\u0300\u0301\7q\2\2\u0301\u0302\7o\2\2\u0302")
        buf.write("\u0303\7k\2\2\u0303\u0304\7e\2\2\u0304\u0305\7t\2\2\u0305")
        buf.write("\u0306\7q\2\2\u0306\u0310\7p\2\2\u0307\u0308\7^\2\2\u0308")
        buf.write("\u0309\7Q\2\2\u0309\u030a\7o\2\2\u030a\u030b\7k\2\2\u030b")
        buf.write("\u030c\7e\2\2\u030c\u030d\7t\2\2\u030d\u030e\7q\2\2\u030e")
        buf.write("\u0310\7p\2\2\u030f\u02ff\3\2\2\2\u030f\u0307\3\2\2\2")
        buf.write("\u0310\u00aa\3\2\2\2\u0311\u0312\7^\2\2\u0312\u0313\7")
        buf.write("r\2\2\u0313\u0318\7k\2\2\u0314\u0315\7^\2\2\u0315\u0316")
        buf.write("\7R\2\2\u0316\u0318\7k\2\2\u0317\u0311\3\2\2\2\u0317\u0314")
        buf.write("\3\2\2\2\u0318\u00ac\3\2\2\2\u0319\u031a\7^\2\2\u031a")
        buf.write("\u031b\7t\2\2\u031b\u031c\7j\2\2\u031c\u0322\7q\2\2\u031d")
        buf.write("\u031e\7^\2\2\u031e\u031f\7T\2\2\u031f\u0320\7j\2\2\u0320")
        buf.write("\u0322\7q\2\2\u0321\u0319\3\2\2\2\u0321\u031d\3\2\2\2")
        buf.write("\u0322\u00ae\3\2\2\2\u0323\u0324\7^\2\2\u0324\u0325\7")
        buf.write("u\2\2\u0325\u0326\7k\2\2\u0326\u0327\7i\2\2\u0327\u0328")
        buf.write("\7o\2\2\u0328\u0330\7c\2\2\u0329\u032a\7^\2\2\u032a\u032b")
        buf.write("\7U\2\2\u032b\u032c\7k\2\2\u032c\u032d\7i\2\2\u032d\u032e")
        buf.write("\7o\2\2\u032e\u0330\7c\2\2\u032f\u0323\3\2\2\2\u032f\u0329")
        buf.write("\3\2\2\2\u0330\u00b0\3\2\2\2\u0331\u0332\7^\2\2\u0332")
        buf.write("\u0333\7v\2\2\u0333\u0334\7c\2\2\u0334\u033a\7w\2\2\u0335")
        buf.write("\u0336\7^\2\2\u0336\u0337\7V\2\2\u0337\u0338\7c\2\2\u0338")
        buf.write("\u033a\7w\2\2\u0339\u0331\3\2\2\2\u0339\u0335\3\2\2\2")
        buf.write("\u033a\u00b2\3\2\2\2\u033b\u033c\7^\2\2\u033c\u033d\7")
        buf.write("w\2\2\u033d\u033e\7r\2\2\u033e\u033f\7u\2\2\u033f\u0340")
        buf.write("\7k\2\2\u0340\u0341\7n\2\2\u0341\u0342\7q\2\2\u0342\u034c")
        buf.write("\7p\2\2\u0343\u0344\7^\2\2\u0344\u0345\7W\2\2\u0345\u0346")
        buf.write("\7r\2\2\u0346\u0347\7u\2\2\u0347\u0348\7k\2\2\u0348\u0349")
        buf.write("\7n\2\2\u0349\u034a\7q\2\2\u034a\u034c\7p\2\2\u034b\u033b")
        buf.write("\3\2\2\2\u034b\u0343\3\2\2\2\u034c\u00b4\3\2\2\2\u034d")
        buf.write("\u034e\7^\2\2\u034e\u034f\7r\2\2\u034f\u0350\7j\2\2\u0350")
        buf.write("\u0356\7k\2\2\u0351\u0352\7^\2\2\u0352\u0353\7R\2\2\u0353")
        buf.write("\u0354\7j\2\2\u0354\u0356\7k\2\2\u0355\u034d\3\2\2\2\u0355")
        buf.write("\u0351\3\2\2\2\u0356\u00b6\3\2\2\2\u0357\u0358\7^\2\2")
        buf.write("\u0358\u0359\7e\2\2\u0359\u035a\7j\2\2\u035a\u0360\7k")
        buf.write("\2\2\u035b\u035c\7^\2\2\u035c\u035d\7E\2\2\u035d\u035e")
        buf.write("\7j\2\2\u035e\u0360\7k\2\2\u035f\u0357\3\2\2\2\u035f\u035b")
        buf.write("\3\2\2\2\u0360\u00b8\3\2\2\2\u0361\u0362\7^\2\2\u0362")
        buf.write("\u0363\7r\2\2\u0363\u0364\7u\2\2\u0364\u036a\7k\2\2\u0365")
        buf.write("\u0366\7^\2\2\u0366\u0367\7R\2\2\u0367\u0368\7u\2\2\u0368")
        buf.write("\u036a\7k\2\2\u0369\u0361\3\2\2\2\u0369\u0365\3\2\2\2")
        buf.write("\u036a\u00ba\3\2\2\2\u036b\u036c\7^\2\2\u036c\u036d\7")
        buf.write("q\2\2\u036d\u036e\7o\2\2\u036e\u036f\7g\2\2\u036f\u0370")
        buf.write("\7i\2\2\u0370\u0378\7c\2\2\u0371\u0372\7^\2\2\u0372\u0373")
        buf.write("\7Q\2\2\u0373\u0374\7o\2\2\u0374\u0375\7g\2\2\u0375\u0376")
        buf.write("\7i\2\2\u0376\u0378\7c\2\2\u0377\u036b\3\2\2\2\u0377\u0371")
        buf.write("\3\2\2\2\u0378\u00bc\3\2\2\2\u0379\u0392\5\u008dG\2\u037a")
        buf.write("\u0392\5\u008fH\2\u037b\u0392\5\u0091I\2\u037c\u0392\5")
        buf.write("\u0093J\2\u037d\u0392\5\u0095K\2\u037e\u0392\5\u0097L")
        buf.write("\2\u037f\u0392\5\u0099M\2\u0380\u0392\5\u009bN\2\u0381")
        buf.write("\u0392\5\u009dO\2\u0382\u0392\5\u009fP\2\u0383\u0392\5")
        buf.write("\u00a1Q\2\u0384\u0392\5\u00a3R\2\u0385\u0392\5\u00a5S")
        buf.write("\2\u0386\u0392\5\u00a7T\2\u0387\u0392\5\u00a9U\2\u0388")
        buf.write("\u0392\5\u00abV\2\u0389\u0392\5\u00adW\2\u038a\u0392\5")
        buf.write("\u00afX\2\u038b\u0392\5\u00b1Y\2\u038c\u0392\5\u00b3Z")
        buf.write("\2\u038d\u0392\5\u00b5[\2\u038e\u0392\5\u00b7\\\2\u038f")
        buf.write("\u0392\5\u00b9]\2\u0390\u0392\5\u00bb^\2\u0391\u0379\3")
        buf.write("\2\2\2\u0391\u037a\3\2\2\2\u0391\u037b\3\2\2\2\u0391\u037c")
        buf.write("\3\2\2\2\u0391\u037d\3\2\2\2\u0391\u037e\3\2\2\2\u0391")
        buf.write("\u037f\3\2\2\2\u0391\u0380\3\2\2\2\u0391\u0381\3\2\2\2")
        buf.write("\u0391\u0382\3\2\2\2\u0391\u0383\3\2\2\2\u0391\u0384\3")
        buf.write("\2\2\2\u0391\u0385\3\2\2\2\u0391\u0386\3\2\2\2\u0391\u0387")
        buf.write("\3\2\2\2\u0391\u0388\3\2\2\2\u0391\u0389\3\2\2\2\u0391")
        buf.write("\u038a\3\2\2\2\u0391\u038b\3\2\2\2\u0391\u038c\3\2\2\2")
        buf.write("\u0391\u038d\3\2\2\2\u0391\u038e\3\2\2\2\u0391\u038f\3")
        buf.write("\2\2\2\u0391\u0390\3\2\2\2\u0392\u00be\3\2\2\2\u0393\u0394")
        buf.write("\5\u00bd_\2\u0394\u0395\5\17\b\2\u0395\u00c0\3\2\2\2\u0396")
        buf.write("\u0397\5\u00bd_\2\u0397\u0398\5\13\6\2\u0398\u00c2\3\2")
        buf.write("\2\2\u0399\u039b\t\6\2\2\u039a\u0399\3\2\2\2\u039b\u039c")
        buf.write("\3\2\2\2\u039c\u039a\3\2\2\2\u039c\u039d\3\2\2\2\u039d")
        buf.write("\u039e\3\2\2\2\u039e\u039f\bb\2\2\u039f\u00c4\3\2\2\2")
        buf.write("B\2\u0123\u013a\u0141\u0147\u014e\u0155\u015c\u0163\u016a")
        buf.write("\u0171\u0177\u017d\u0183\u0189\u018f\u0195\u019d\u01a5")
        buf.write("\u01ad\u01b3\u01b9\u01bf\u01c5\u01cb\u01d1\u01d7\u01dd")
        buf.write("\u01e3\u01eb\u0212\u0216\u021b\u021f\u0224\u0226\u0231")
        buf.write("\u0236\u025d\u0269\u0277\u0285\u0297\u02a3\u02ad\u02bb")
        buf.write("\u02c7\u02d5\u02e5\u02ed\u02f5\u02fd\u030f\u0317\u0321")
        buf.write("\u032f\u0339\u034b\u0355\u035f\u0369\u0377\u0391\u039c")
        buf.write("\3\b\2\2")
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
    GREEKFUNCTIONBRACE = 67
    GREEKFUNCTIONPAREN = 68
    WS = 69

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
            "BANG", "GREEKLETTER", "GREEKFUNCTIONBRACE", "GREEKFUNCTIONPAREN", 
            "WS" ]

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
                  "PHI", "CHI", "PSI", "OMEGA", "GREEKLETTER", "GREEKFUNCTIONBRACE", 
                  "GREEKFUNCTIONPAREN", "WS" ]

    grammarFileName = "MatexLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


