# Generated from .\pymatex\grammar\MatexLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u03c9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u012c\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\5\31\u0143\n\31\3\31\3\31\3")
        buf.write("\31\3\31\3\32\5\32\u014a\n\32\3\32\3\32\3\32\3\33\5\33")
        buf.write("\u0150\n\33\3\33\3\33\3\33\3\33\3\34\5\34\u0157\n\34\3")
        buf.write("\34\3\34\3\34\3\34\3\35\5\35\u015e\n\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\5\36\u0165\n\36\3\36\3\36\3\36\3\36\3\37\5")
        buf.write("\37\u016c\n\37\3\37\3\37\3\37\3\37\3 \5 \u0173\n \3 \3")
        buf.write(" \3 \3 \3!\5!\u017a\n!\3!\3!\3!\3\"\5\"\u0180\n\"\3\"")
        buf.write("\3\"\3\"\3#\5#\u0186\n#\3#\3#\3#\3$\5$\u018c\n$\3$\3$")
        buf.write("\3$\3%\5%\u0192\n%\3%\3%\3%\3&\5&\u0198\n&\3&\3&\3&\3")
        buf.write("\'\5\'\u019e\n\'\3\'\3\'\3\'\3\'\3\'\3(\5(\u01a6\n(\3")
        buf.write("(\3(\3(\3(\3(\3)\5)\u01ae\n)\3)\3)\3)\3)\3)\3*\5*\u01b6")
        buf.write("\n*\3*\3*\3*\3+\5+\u01bc\n+\3+\3+\3+\3,\5,\u01c2\n,\3")
        buf.write(",\3,\3,\3-\5-\u01c8\n-\3-\3-\3-\3.\5.\u01ce\n.\3.\3.\3")
        buf.write(".\3/\5/\u01d4\n/\3/\3/\3/\3\60\5\60\u01da\n\60\3\60\3")
        buf.write("\60\3\60\3\61\5\61\u01e0\n\61\3\61\3\61\3\61\3\62\5\62")
        buf.write("\u01e6\n\62\3\62\3\62\3\62\3\63\5\63\u01ec\n\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\64\5\64\u01f4\n\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\38\38\38\39\39\3:\3:\3;\7;\u0219\n;\f;\16;\u021c")
        buf.write("\13;\3;\5;\u021f\n;\3;\6;\u0222\n;\r;\16;\u0223\3;\3;")
        buf.write("\5;\u0228\n;\3;\6;\u022b\n;\r;\16;\u022c\5;\u022f\n;\3")
        buf.write("<\3<\3<\3=\3=\3>\3>\6>\u0238\n>\r>\16>\u0239\3?\6?\u023d")
        buf.write("\n?\r?\16?\u023e\3@\3@\3@\3@\3@\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\3D\3D\3E\3E\3E\3E\3E\3F\3F\3F\3F\5F\u025c\n")
        buf.write("F\3G\3G\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\5H\u026c\n")
        buf.write("H\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u0278\nI\3J\3J\3J\3")
        buf.write("J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u0286\nJ\3K\3K\3K\3K\3K\3")
        buf.write("K\3K\3K\3K\3K\3K\3K\5K\u0294\nK\3L\3L\3L\3L\3L\3L\3L\3")
        buf.write("L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u02a6\nL\3M\3M\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\3M\5M\u02b2\nM\3N\3N\3N\3N\3N\3N\3N\3N\5N\u02bc")
        buf.write("\nN\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u02ca\nO\3")
        buf.write("P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u02d6\nP\3Q\3Q\3Q\3Q\3")
        buf.write("Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u02e4\nQ\3R\3R\3R\3R\3R\3R\3")
        buf.write("R\3R\3R\3R\3R\3R\3R\3R\5R\u02f4\nR\3S\3S\3S\3S\3S\3S\5")
        buf.write("S\u02fc\nS\3T\3T\3T\3T\3T\3T\5T\u0304\nT\3U\3U\3U\3U\3")
        buf.write("U\3U\5U\u030c\nU\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\5V\u031e\nV\3W\3W\3W\3W\3W\3W\5W\u0326\nW\3")
        buf.write("X\3X\3X\3X\3X\3X\3X\3X\5X\u0330\nX\3Y\3Y\3Y\3Y\3Y\3Y\3")
        buf.write("Y\3Y\3Y\3Y\3Y\3Y\5Y\u033e\nY\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\5")
        buf.write("Z\u0348\nZ\3[\3[\3[\3[\3[\3[\3[\3[\3[\3[\3[\3[\3[\3[\3")
        buf.write("[\3[\5[\u035a\n[\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\5\\\u0364")
        buf.write("\n\\\3]\3]\3]\3]\3]\3]\3]\3]\5]\u036e\n]\3^\3^\3^\3^\3")
        buf.write("^\3^\3^\3^\5^\u0378\n^\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3")
        buf.write("_\3_\5_\u0386\n_\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3")
        buf.write("`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\5`\u03a0\n`\3a\3a\3")
        buf.write("a\3a\3a\5a\u03a7\na\3a\3a\3b\3b\5b\u03ad\nb\3b\3b\3c\3")
        buf.write("c\5c\u03b3\nc\3c\3c\3d\3d\5d\u03b9\nd\3d\3d\3e\3e\5e\u03bf")
        buf.write("\ne\3e\3e\3f\6f\u03c4\nf\rf\16f\u03c5\3f\3f\2\2g\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\2%\23\'\24)\25+\26-\27/\2\61\30\63")
        buf.write("\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)")
        buf.write("U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67q\2s\2u8w")
        buf.write("9y:{;}<\177=\u0081>\u0083\2\u0085\2\u0087\2\u0089\2\u008b")
        buf.write("?\u008d@\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099")
        buf.write("\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5")
        buf.write("\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bfA\u00c1\2\u00c3")
        buf.write("B\u00c5C\u00c7D\u00c9E\u00cbF\3\2\7\4\2C\\c|\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2\u0408\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2\61\3\2\2\2\2\63\3\2")
        buf.write("\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2")
        buf.write("=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2")
        buf.write("\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2")
        buf.write("\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2")
        buf.write("\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3")
        buf.write("\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u00bf\3\2\2\2\2\u00c3\3\2\2")
        buf.write("\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb")
        buf.write("\3\2\2\2\3\u00cd\3\2\2\2\5\u00cf\3\2\2\2\7\u00d1\3\2\2")
        buf.write("\2\t\u00d3\3\2\2\2\13\u00d5\3\2\2\2\r\u00d7\3\2\2\2\17")
        buf.write("\u00d9\3\2\2\2\21\u00db\3\2\2\2\23\u00dd\3\2\2\2\25\u00df")
        buf.write("\3\2\2\2\27\u00e1\3\2\2\2\31\u00e3\3\2\2\2\33\u00e5\3")
        buf.write("\2\2\2\35\u00e7\3\2\2\2\37\u00e9\3\2\2\2!\u00eb\3\2\2")
        buf.write("\2#\u00ed\3\2\2\2%\u00ef\3\2\2\2\'\u012b\3\2\2\2)\u012d")
        buf.write("\3\2\2\2+\u0132\3\2\2\2-\u0137\3\2\2\2/\u013d\3\2\2\2")
        buf.write("\61\u0142\3\2\2\2\63\u0149\3\2\2\2\65\u014f\3\2\2\2\67")
        buf.write("\u0156\3\2\2\29\u015d\3\2\2\2;\u0164\3\2\2\2=\u016b\3")
        buf.write("\2\2\2?\u0172\3\2\2\2A\u0179\3\2\2\2C\u017f\3\2\2\2E\u0185")
        buf.write("\3\2\2\2G\u018b\3\2\2\2I\u0191\3\2\2\2K\u0197\3\2\2\2")
        buf.write("M\u019d\3\2\2\2O\u01a5\3\2\2\2Q\u01ad\3\2\2\2S\u01b5\3")
        buf.write("\2\2\2U\u01bb\3\2\2\2W\u01c1\3\2\2\2Y\u01c7\3\2\2\2[\u01cd")
        buf.write("\3\2\2\2]\u01d3\3\2\2\2_\u01d9\3\2\2\2a\u01df\3\2\2\2")
        buf.write("c\u01e5\3\2\2\2e\u01eb\3\2\2\2g\u01f3\3\2\2\2i\u01fb\3")
        buf.write("\2\2\2k\u0202\3\2\2\2m\u0208\3\2\2\2o\u020d\3\2\2\2q\u0213")
        buf.write("\3\2\2\2s\u0215\3\2\2\2u\u021a\3\2\2\2w\u0230\3\2\2\2")
        buf.write("y\u0233\3\2\2\2{\u0235\3\2\2\2}\u023c\3\2\2\2\177\u0240")
        buf.write("\3\2\2\2\u0081\u0247\3\2\2\2\u0083\u0249\3\2\2\2\u0085")
        buf.write("\u024b\3\2\2\2\u0087\u0250\3\2\2\2\u0089\u0252\3\2\2\2")
        buf.write("\u008b\u025b\3\2\2\2\u008d\u025d\3\2\2\2\u008f\u026b\3")
        buf.write("\2\2\2\u0091\u0277\3\2\2\2\u0093\u0285\3\2\2\2\u0095\u0293")
        buf.write("\3\2\2\2\u0097\u02a5\3\2\2\2\u0099\u02b1\3\2\2\2\u009b")
        buf.write("\u02bb\3\2\2\2\u009d\u02c9\3\2\2\2\u009f\u02d5\3\2\2\2")
        buf.write("\u00a1\u02e3\3\2\2\2\u00a3\u02f3\3\2\2\2\u00a5\u02fb\3")
        buf.write("\2\2\2\u00a7\u0303\3\2\2\2\u00a9\u030b\3\2\2\2\u00ab\u031d")
        buf.write("\3\2\2\2\u00ad\u0325\3\2\2\2\u00af\u032f\3\2\2\2\u00b1")
        buf.write("\u033d\3\2\2\2\u00b3\u0347\3\2\2\2\u00b5\u0359\3\2\2\2")
        buf.write("\u00b7\u0363\3\2\2\2\u00b9\u036d\3\2\2\2\u00bb\u0377\3")
        buf.write("\2\2\2\u00bd\u0385\3\2\2\2\u00bf\u039f\3\2\2\2\u00c1\u03a1")
        buf.write("\3\2\2\2\u00c3\u03aa\3\2\2\2\u00c5\u03b0\3\2\2\2\u00c7")
        buf.write("\u03b6\3\2\2\2\u00c9\u03bc\3\2\2\2\u00cb\u03c3\3\2\2\2")
        buf.write("\u00cd\u00ce\7-\2\2\u00ce\4\3\2\2\2\u00cf\u00d0\7/\2\2")
        buf.write("\u00d0\6\3\2\2\2\u00d1\u00d2\7,\2\2\u00d2\b\3\2\2\2\u00d3")
        buf.write("\u00d4\7\61\2\2\u00d4\n\3\2\2\2\u00d5\u00d6\7*\2\2\u00d6")
        buf.write("\f\3\2\2\2\u00d7\u00d8\7+\2\2\u00d8\16\3\2\2\2\u00d9\u00da")
        buf.write("\7}\2\2\u00da\20\3\2\2\2\u00db\u00dc\7\177\2\2\u00dc\22")
        buf.write("\3\2\2\2\u00dd\u00de\7]\2\2\u00de\24\3\2\2\2\u00df\u00e0")
        buf.write("\7_\2\2\u00e0\26\3\2\2\2\u00e1\u00e2\7.\2\2\u00e2\30\3")
        buf.write("\2\2\2\u00e3\u00e4\7\60\2\2\u00e4\32\3\2\2\2\u00e5\u00e6")
        buf.write("\7~\2\2\u00e6\34\3\2\2\2\u00e7\u00e8\7a\2\2\u00e8\36\3")
        buf.write("\2\2\2\u00e9\u00ea\7`\2\2\u00ea \3\2\2\2\u00eb\u00ec\7")
        buf.write("<\2\2\u00ec\"\3\2\2\2\u00ed\u00ee\7^\2\2\u00ee$\3\2\2")
        buf.write("\2\u00ef\u00f0\7^\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7")
        buf.write("k\2\2\u00f2\u00f3\7o\2\2\u00f3&\3\2\2\2\u00f4\u00f5\7")
        buf.write("^\2\2\u00f5\u00f6\7v\2\2\u00f6\u012c\7q\2\2\u00f7\u00f8")
        buf.write("\7^\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb")
        buf.write("\7i\2\2\u00fb\u00fc\7j\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe")
        buf.write("\7c\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7q\2\2\u0101\u012c\7y\2\2\u0102\u0103\7^\2\2\u0103\u0104")
        buf.write("\7T\2\2\u0104\u0105\7k\2\2\u0105\u0106\7i\2\2\u0106\u0107")
        buf.write("\7j\2\2\u0107\u0108\7v\2\2\u0108\u0109\7c\2\2\u0109\u010a")
        buf.write("\7t\2\2\u010a\u010b\7t\2\2\u010b\u010c\7q\2\2\u010c\u012c")
        buf.write("\7y\2\2\u010d\u010e\7^\2\2\u010e\u010f\7n\2\2\u010f\u0110")
        buf.write("\7q\2\2\u0110\u0111\7p\2\2\u0111\u0112\7i\2\2\u0112\u0113")
        buf.write("\7t\2\2\u0113\u0114\7k\2\2\u0114\u0115\7i\2\2\u0115\u0116")
        buf.write("\7j\2\2\u0116\u0117\7v\2\2\u0117\u0118\7c\2\2\u0118\u0119")
        buf.write("\7t\2\2\u0119\u011a\7t\2\2\u011a\u011b\7q\2\2\u011b\u012c")
        buf.write("\7y\2\2\u011c\u011d\7^\2\2\u011d\u011e\7N\2\2\u011e\u011f")
        buf.write("\7q\2\2\u011f\u0120\7p\2\2\u0120\u0121\7i\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122\u0123\7k\2\2\u0123\u0124\7i\2\2\u0124\u0125")
        buf.write("\7j\2\2\u0125\u0126\7v\2\2\u0126\u0127\7c\2\2\u0127\u0128")
        buf.write("\7t\2\2\u0128\u0129\7t\2\2\u0129\u012a\7q\2\2\u012a\u012c")
        buf.write("\7y\2\2\u012b\u00f4\3\2\2\2\u012b\u00f7\3\2\2\2\u012b")
        buf.write("\u0102\3\2\2\2\u012b\u010d\3\2\2\2\u012b\u011c\3\2\2\2")
        buf.write("\u012c(\3\2\2\2\u012d\u012e\7^\2\2\u012e\u012f\7k\2\2")
        buf.write("\u012f\u0130\7p\2\2\u0130\u0131\7v\2\2\u0131*\3\2\2\2")
        buf.write("\u0132\u0133\7^\2\2\u0133\u0134\7u\2\2\u0134\u0135\7w")
        buf.write("\2\2\u0135\u0136\7o\2\2\u0136,\3\2\2\2\u0137\u0138\7^")
        buf.write("\2\2\u0138\u0139\7r\2\2\u0139\u013a\7t\2\2\u013a\u013b")
        buf.write("\7q\2\2\u013b\u013c\7f\2\2\u013c.\3\2\2\2\u013d\u013e")
        buf.write("\7c\2\2\u013e\u013f\7t\2\2\u013f\u0140\7e\2\2\u0140\60")
        buf.write("\3\2\2\2\u0141\u0143\5#\22\2\u0142\u0141\3\2\2\2\u0142")
        buf.write("\u0143\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145\7n\2\2")
        buf.write("\u0145\u0146\7q\2\2\u0146\u0147\7i\2\2\u0147\62\3\2\2")
        buf.write("\2\u0148\u014a\5#\22\2\u0149\u0148\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\7n\2\2\u014c")
        buf.write("\u014d\7p\2\2\u014d\64\3\2\2\2\u014e\u0150\5#\22\2\u014f")
        buf.write("\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\u0152\7u\2\2\u0152\u0153\7k\2\2\u0153\u0154\7p")
        buf.write("\2\2\u0154\66\3\2\2\2\u0155\u0157\5#\22\2\u0156\u0155")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2\u0158")
        buf.write("\u0159\7e\2\2\u0159\u015a\7q\2\2\u015a\u015b\7u\2\2\u015b")
        buf.write("8\3\2\2\2\u015c\u015e\5#\22\2\u015d\u015c\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\7v\2\2")
        buf.write("\u0160\u0161\7c\2\2\u0161\u0162\7p\2\2\u0162:\3\2\2\2")
        buf.write("\u0163\u0165\5#\22\2\u0164\u0163\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\7e\2\2\u0167\u0168")
        buf.write("\7u\2\2\u0168\u0169\7e\2\2\u0169<\3\2\2\2\u016a\u016c")
        buf.write("\5#\22\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\u016e\7u\2\2\u016e\u016f\7g\2\2\u016f")
        buf.write("\u0170\7e\2\2\u0170>\3\2\2\2\u0171\u0173\5#\22\2\u0172")
        buf.write("\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174\u0175\7e\2\2\u0175\u0176\7q\2\2\u0176\u0177\7v")
        buf.write("\2\2\u0177@\3\2\2\2\u0178\u017a\5#\22\2\u0179\u0178\3")
        buf.write("\2\2\2\u0179\u017a\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c")
        buf.write("\5/\30\2\u017c\u017d\5\65\33\2\u017dB\3\2\2\2\u017e\u0180")
        buf.write("\5#\22\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u0182\5/\30\2\u0182\u0183\5\67\34")
        buf.write("\2\u0183D\3\2\2\2\u0184\u0186\5#\22\2\u0185\u0184\3\2")
        buf.write("\2\2\u0185\u0186\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188")
        buf.write("\5/\30\2\u0188\u0189\59\35\2\u0189F\3\2\2\2\u018a\u018c")
        buf.write("\5#\22\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d\u018e\5/\30\2\u018e\u018f\5;\36\2")
        buf.write("\u018fH\3\2\2\2\u0190\u0192\5#\22\2\u0191\u0190\3\2\2")
        buf.write("\2\u0191\u0192\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194")
        buf.write("\5/\30\2\u0194\u0195\5=\37\2\u0195J\3\2\2\2\u0196\u0198")
        buf.write("\5#\22\2\u0197\u0196\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199\u019a\5/\30\2\u019a\u019b\5? \2\u019b")
        buf.write("L\3\2\2\2\u019c\u019e\5#\22\2\u019d\u019c\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\7u\2\2")
        buf.write("\u01a0\u01a1\7k\2\2\u01a1\u01a2\7p\2\2\u01a2\u01a3\7j")
        buf.write("\2\2\u01a3N\3\2\2\2\u01a4\u01a6\5#\22\2\u01a5\u01a4\3")
        buf.write("\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8")
        buf.write("\7e\2\2\u01a8\u01a9\7q\2\2\u01a9\u01aa\7u\2\2\u01aa\u01ab")
        buf.write("\7j\2\2\u01abP\3\2\2\2\u01ac\u01ae\5#\22\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("\u01b0\7v\2\2\u01b0\u01b1\7c\2\2\u01b1\u01b2\7p\2\2\u01b2")
        buf.write("\u01b3\7j\2\2\u01b3R\3\2\2\2\u01b4\u01b6\5#\22\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b8\5/\30\2\u01b8\u01b9\5M\'\2\u01b9T\3\2\2\2")
        buf.write("\u01ba\u01bc\5#\22\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3")
        buf.write("\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\5/\30\2\u01be\u01bf")
        buf.write("\5O(\2\u01bfV\3\2\2\2\u01c0\u01c2\5#\22\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("\u01c4\5/\30\2\u01c4\u01c5\5Q)\2\u01c5X\3\2\2\2\u01c6")
        buf.write("\u01c8\5#\22\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3\2\2\2")
        buf.write("\u01c8\u01c9\3\2\2\2\u01c9\u01ca\7e\2\2\u01ca\u01cb\7")
        buf.write("p\2\2\u01cbZ\3\2\2\2\u01cc\u01ce\5#\22\2\u01cd\u01cc\3")
        buf.write("\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0")
        buf.write("\7u\2\2\u01d0\u01d1\7p\2\2\u01d1\\\3\2\2\2\u01d2\u01d4")
        buf.write("\5#\22\2\u01d3\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d6\7f\2\2\u01d6\u01d7\7p\2\2\u01d7")
        buf.write("^\3\2\2\2\u01d8\u01da\5#\22\2\u01d9\u01d8\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dc\5/\30\2")
        buf.write("\u01dc\u01dd\5Y-\2\u01dd`\3\2\2\2\u01de\u01e0\5#\22\2")
        buf.write("\u01df\u01de\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\3")
        buf.write("\2\2\2\u01e1\u01e2\5/\30\2\u01e2\u01e3\5[.\2\u01e3b\3")
        buf.write("\2\2\2\u01e4\u01e6\5#\22\2\u01e5\u01e4\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\5/\30\2\u01e8")
        buf.write("\u01e9\5]/\2\u01e9d\3\2\2\2\u01ea\u01ec\5#\22\2\u01eb")
        buf.write("\u01ea\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ed\3\2\2\2")
        buf.write("\u01ed\u01ee\7u\2\2\u01ee\u01ef\7s\2\2\u01ef\u01f0\7t")
        buf.write("\2\2\u01f0\u01f1\7v\2\2\u01f1f\3\2\2\2\u01f2\u01f4\5#")
        buf.write("\22\2\u01f3\u01f2\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u01f6\7d\2\2\u01f6\u01f7\7k\2\2\u01f7\u01f8")
        buf.write("\7p\2\2\u01f8\u01f9\7q\2\2\u01f9\u01fa\7o\2\2\u01fah\3")
        buf.write("\2\2\2\u01fb\u01fc\7^\2\2\u01fc\u01fd\7v\2\2\u01fd\u01fe")
        buf.write("\7k\2\2\u01fe\u01ff\7o\2\2\u01ff\u0200\7g\2\2\u0200\u0201")
        buf.write("\7u\2\2\u0201j\3\2\2\2\u0202\u0203\7^\2\2\u0203\u0204")
        buf.write("\7e\2\2\u0204\u0205\7f\2\2\u0205\u0206\7q\2\2\u0206\u0207")
        buf.write("\7v\2\2\u0207l\3\2\2\2\u0208\u0209\7^\2\2\u0209\u020a")
        buf.write("\7f\2\2\u020a\u020b\7k\2\2\u020b\u020c\7x\2\2\u020cn\3")
        buf.write("\2\2\2\u020d\u020e\7^\2\2\u020e\u020f\7h\2\2\u020f\u0210")
        buf.write("\7t\2\2\u0210\u0211\7c\2\2\u0211\u0212\7e\2\2\u0212p\3")
        buf.write("\2\2\2\u0213\u0214\t\2\2\2\u0214r\3\2\2\2\u0215\u0216")
        buf.write("\t\3\2\2\u0216t\3\2\2\2\u0217\u0219\5s:\2\u0218\u0217")
        buf.write("\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021d\u021f\7\60\2\2\u021e\u021d\3\2\2\2\u021e\u021f")
        buf.write("\3\2\2\2\u021f\u0221\3\2\2\2\u0220\u0222\5s:\2\u0221\u0220")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0221\3\2\2\2\u0223")
        buf.write("\u0224\3\2\2\2\u0224\u022e\3\2\2\2\u0225\u0227\t\4\2\2")
        buf.write("\u0226\u0228\t\5\2\2\u0227\u0226\3\2\2\2\u0227\u0228\3")
        buf.write("\2\2\2\u0228\u022a\3\2\2\2\u0229\u022b\5s:\2\u022a\u0229")
        buf.write("\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022a\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u0225\3\2\2\2")
        buf.write("\u022e\u022f\3\2\2\2\u022fv\3\2\2\2\u0230\u0231\7f\2\2")
        buf.write("\u0231\u0232\5q9\2\u0232x\3\2\2\2\u0233\u0234\5q9\2\u0234")
        buf.write("z\3\2\2\2\u0235\u0237\5u;\2\u0236\u0238\5y=\2\u0237\u0236")
        buf.write("\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u0237\3\2\2\2\u0239")
        buf.write("\u023a\3\2\2\2\u023a|\3\2\2\2\u023b\u023d\5y=\2\u023c")
        buf.write("\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023c\3\2\2\2")
        buf.write("\u023e\u023f\3\2\2\2\u023f~\3\2\2\2\u0240\u0241\7^\2\2")
        buf.write("\u0241\u0242\7k\2\2\u0242\u0243\7p\2\2\u0243\u0244\7h")
        buf.write("\2\2\u0244\u0245\7v\2\2\u0245\u0246\7{\2\2\u0246\u0080")
        buf.write("\3\2\2\2\u0247\u0248\7?\2\2\u0248\u0082\3\2\2\2\u0249")
        buf.write("\u024a\7>\2\2\u024a\u0084\3\2\2\2\u024b\u024c\7^\2\2\u024c")
        buf.write("\u024d\7n\2\2\u024d\u024e\7g\2\2\u024e\u024f\7s\2\2\u024f")
        buf.write("\u0086\3\2\2\2\u0250\u0251\7@\2\2\u0251\u0088\3\2\2\2")
        buf.write("\u0252\u0253\7^\2\2\u0253\u0254\7i\2\2\u0254\u0255\7g")
        buf.write("\2\2\u0255\u0256\7s\2\2\u0256\u008a\3\2\2\2\u0257\u025c")
        buf.write("\5\u0083B\2\u0258\u025c\5\u0085C\2\u0259\u025c\5\u0087")
        buf.write("D\2\u025a\u025c\5\u0089E\2\u025b\u0257\3\2\2\2\u025b\u0258")
        buf.write("\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025a\3\2\2\2\u025c")
        buf.write("\u008c\3\2\2\2\u025d\u025e\7#\2\2\u025e\u008e\3\2\2\2")
        buf.write("\u025f\u0260\7^\2\2\u0260\u0261\7c\2\2\u0261\u0262\7n")
        buf.write("\2\2\u0262\u0263\7r\2\2\u0263\u0264\7j\2\2\u0264\u026c")
        buf.write("\7c\2\2\u0265\u0266\7^\2\2\u0266\u0267\7C\2\2\u0267\u0268")
        buf.write("\7n\2\2\u0268\u0269\7r\2\2\u0269\u026a\7j\2\2\u026a\u026c")
        buf.write("\7c\2\2\u026b\u025f\3\2\2\2\u026b\u0265\3\2\2\2\u026c")
        buf.write("\u0090\3\2\2\2\u026d\u026e\7^\2\2\u026e\u026f\7d\2\2\u026f")
        buf.write("\u0270\7g\2\2\u0270\u0271\7v\2\2\u0271\u0278\7c\2\2\u0272")
        buf.write("\u0273\7^\2\2\u0273\u0274\7D\2\2\u0274\u0275\7g\2\2\u0275")
        buf.write("\u0276\7v\2\2\u0276\u0278\7c\2\2\u0277\u026d\3\2\2\2\u0277")
        buf.write("\u0272\3\2\2\2\u0278\u0092\3\2\2\2\u0279\u027a\7^\2\2")
        buf.write("\u027a\u027b\7i\2\2\u027b\u027c\7c\2\2\u027c\u027d\7o")
        buf.write("\2\2\u027d\u027e\7o\2\2\u027e\u0286\7c\2\2\u027f\u0280")
        buf.write("\7^\2\2\u0280\u0281\7I\2\2\u0281\u0282\7c\2\2\u0282\u0283")
        buf.write("\7o\2\2\u0283\u0284\7o\2\2\u0284\u0286\7c\2\2\u0285\u0279")
        buf.write("\3\2\2\2\u0285\u027f\3\2\2\2\u0286\u0094\3\2\2\2\u0287")
        buf.write("\u0288\7^\2\2\u0288\u0289\7f\2\2\u0289\u028a\7g\2\2\u028a")
        buf.write("\u028b\7n\2\2\u028b\u028c\7v\2\2\u028c\u0294\7c\2\2\u028d")
        buf.write("\u028e\7^\2\2\u028e\u028f\7F\2\2\u028f\u0290\7g\2\2\u0290")
        buf.write("\u0291\7n\2\2\u0291\u0292\7v\2\2\u0292\u0294\7c\2\2\u0293")
        buf.write("\u0287\3\2\2\2\u0293\u028d\3\2\2\2\u0294\u0096\3\2\2\2")
        buf.write("\u0295\u0296\7^\2\2\u0296\u0297\7g\2\2\u0297\u0298\7r")
        buf.write("\2\2\u0298\u0299\7u\2\2\u0299\u029a\7k\2\2\u029a\u029b")
        buf.write("\7n\2\2\u029b\u029c\7q\2\2\u029c\u02a6\7p\2\2\u029d\u029e")
        buf.write("\7^\2\2\u029e\u029f\7G\2\2\u029f\u02a0\7r\2\2\u02a0\u02a1")
        buf.write("\7u\2\2\u02a1\u02a2\7k\2\2\u02a2\u02a3\7n\2\2\u02a3\u02a4")
        buf.write("\7q\2\2\u02a4\u02a6\7p\2\2\u02a5\u0295\3\2\2\2\u02a5\u029d")
        buf.write("\3\2\2\2\u02a6\u0098\3\2\2\2\u02a7\u02a8\7^\2\2\u02a8")
        buf.write("\u02a9\7|\2\2\u02a9\u02aa\7g\2\2\u02aa\u02ab\7v\2\2\u02ab")
        buf.write("\u02b2\7c\2\2\u02ac\u02ad\7^\2\2\u02ad\u02ae\7\\\2\2\u02ae")
        buf.write("\u02af\7g\2\2\u02af\u02b0\7v\2\2\u02b0\u02b2\7c\2\2\u02b1")
        buf.write("\u02a7\3\2\2\2\u02b1\u02ac\3\2\2\2\u02b2\u009a\3\2\2\2")
        buf.write("\u02b3\u02b4\7^\2\2\u02b4\u02b5\7g\2\2\u02b5\u02b6\7v")
        buf.write("\2\2\u02b6\u02bc\7c\2\2\u02b7\u02b8\7^\2\2\u02b8\u02b9")
        buf.write("\7G\2\2\u02b9\u02ba\7v\2\2\u02ba\u02bc\7c\2\2\u02bb\u02b3")
        buf.write("\3\2\2\2\u02bb\u02b7\3\2\2\2\u02bc\u009c\3\2\2\2\u02bd")
        buf.write("\u02be\7^\2\2\u02be\u02bf\7v\2\2\u02bf\u02c0\7j\2\2\u02c0")
        buf.write("\u02c1\7g\2\2\u02c1\u02c2\7v\2\2\u02c2\u02ca\7c\2\2\u02c3")
        buf.write("\u02c4\7^\2\2\u02c4\u02c5\7V\2\2\u02c5\u02c6\7j\2\2\u02c6")
        buf.write("\u02c7\7g\2\2\u02c7\u02c8\7v\2\2\u02c8\u02ca\7c\2\2\u02c9")
        buf.write("\u02bd\3\2\2\2\u02c9\u02c3\3\2\2\2\u02ca\u009e\3\2\2\2")
        buf.write("\u02cb\u02cc\7^\2\2\u02cc\u02cd\7k\2\2\u02cd\u02ce\7q")
        buf.write("\2\2\u02ce\u02cf\7v\2\2\u02cf\u02d6\7c\2\2\u02d0\u02d1")
        buf.write("\7^\2\2\u02d1\u02d2\7K\2\2\u02d2\u02d3\7q\2\2\u02d3\u02d4")
        buf.write("\7v\2\2\u02d4\u02d6\7c\2\2\u02d5\u02cb\3\2\2\2\u02d5\u02d0")
        buf.write("\3\2\2\2\u02d6\u00a0\3\2\2\2\u02d7\u02d8\7^\2\2\u02d8")
        buf.write("\u02d9\7m\2\2\u02d9\u02da\7c\2\2\u02da\u02db\7r\2\2\u02db")
        buf.write("\u02dc\7r\2\2\u02dc\u02e4\7c\2\2\u02dd\u02de\7^\2\2\u02de")
        buf.write("\u02df\7M\2\2\u02df\u02e0\7c\2\2\u02e0\u02e1\7r\2\2\u02e1")
        buf.write("\u02e2\7r\2\2\u02e2\u02e4\7c\2\2\u02e3\u02d7\3\2\2\2\u02e3")
        buf.write("\u02dd\3\2\2\2\u02e4\u00a2\3\2\2\2\u02e5\u02e6\7^\2\2")
        buf.write("\u02e6\u02e7\7n\2\2\u02e7\u02e8\7c\2\2\u02e8\u02e9\7o")
        buf.write("\2\2\u02e9\u02ea\7d\2\2\u02ea\u02eb\7f\2\2\u02eb\u02f4")
        buf.write("\7c\2\2\u02ec\u02ed\7^\2\2\u02ed\u02ee\7N\2\2\u02ee\u02ef")
        buf.write("\7c\2\2\u02ef\u02f0\7o\2\2\u02f0\u02f1\7d\2\2\u02f1\u02f2")
        buf.write("\7f\2\2\u02f2\u02f4\7c\2\2\u02f3\u02e5\3\2\2\2\u02f3\u02ec")
        buf.write("\3\2\2\2\u02f4\u00a4\3\2\2\2\u02f5\u02f6\7^\2\2\u02f6")
        buf.write("\u02f7\7o\2\2\u02f7\u02fc\7w\2\2\u02f8\u02f9\7^\2\2\u02f9")
        buf.write("\u02fa\7O\2\2\u02fa\u02fc\7w\2\2\u02fb\u02f5\3\2\2\2\u02fb")
        buf.write("\u02f8\3\2\2\2\u02fc\u00a6\3\2\2\2\u02fd\u02fe\7^\2\2")
        buf.write("\u02fe\u02ff\7p\2\2\u02ff\u0304\7w\2\2\u0300\u0301\7^")
        buf.write("\2\2\u0301\u0302\7P\2\2\u0302\u0304\7w\2\2\u0303\u02fd")
        buf.write("\3\2\2\2\u0303\u0300\3\2\2\2\u0304\u00a8\3\2\2\2\u0305")
        buf.write("\u0306\7^\2\2\u0306\u0307\7z\2\2\u0307\u030c\7k\2\2\u0308")
        buf.write("\u0309\7^\2\2\u0309\u030a\7Z\2\2\u030a\u030c\7k\2\2\u030b")
        buf.write("\u0305\3\2\2\2\u030b\u0308\3\2\2\2\u030c\u00aa\3\2\2\2")
        buf.write("\u030d\u030e\7^\2\2\u030e\u030f\7q\2\2\u030f\u0310\7o")
        buf.write("\2\2\u0310\u0311\7k\2\2\u0311\u0312\7e\2\2\u0312\u0313")
        buf.write("\7t\2\2\u0313\u0314\7q\2\2\u0314\u031e\7p\2\2\u0315\u0316")
        buf.write("\7^\2\2\u0316\u0317\7Q\2\2\u0317\u0318\7o\2\2\u0318\u0319")
        buf.write("\7k\2\2\u0319\u031a\7e\2\2\u031a\u031b\7t\2\2\u031b\u031c")
        buf.write("\7q\2\2\u031c\u031e\7p\2\2\u031d\u030d\3\2\2\2\u031d\u0315")
        buf.write("\3\2\2\2\u031e\u00ac\3\2\2\2\u031f\u0320\7^\2\2\u0320")
        buf.write("\u0321\7r\2\2\u0321\u0326\7k\2\2\u0322\u0323\7^\2\2\u0323")
        buf.write("\u0324\7R\2\2\u0324\u0326\7k\2\2\u0325\u031f\3\2\2\2\u0325")
        buf.write("\u0322\3\2\2\2\u0326\u00ae\3\2\2\2\u0327\u0328\7^\2\2")
        buf.write("\u0328\u0329\7t\2\2\u0329\u032a\7j\2\2\u032a\u0330\7q")
        buf.write("\2\2\u032b\u032c\7^\2\2\u032c\u032d\7T\2\2\u032d\u032e")
        buf.write("\7j\2\2\u032e\u0330\7q\2\2\u032f\u0327\3\2\2\2\u032f\u032b")
        buf.write("\3\2\2\2\u0330\u00b0\3\2\2\2\u0331\u0332\7^\2\2\u0332")
        buf.write("\u0333\7u\2\2\u0333\u0334\7k\2\2\u0334\u0335\7i\2\2\u0335")
        buf.write("\u0336\7o\2\2\u0336\u033e\7c\2\2\u0337\u0338\7^\2\2\u0338")
        buf.write("\u0339\7U\2\2\u0339\u033a\7k\2\2\u033a\u033b\7i\2\2\u033b")
        buf.write("\u033c\7o\2\2\u033c\u033e\7c\2\2\u033d\u0331\3\2\2\2\u033d")
        buf.write("\u0337\3\2\2\2\u033e\u00b2\3\2\2\2\u033f\u0340\7^\2\2")
        buf.write("\u0340\u0341\7v\2\2\u0341\u0342\7c\2\2\u0342\u0348\7w")
        buf.write("\2\2\u0343\u0344\7^\2\2\u0344\u0345\7V\2\2\u0345\u0346")
        buf.write("\7c\2\2\u0346\u0348\7w\2\2\u0347\u033f\3\2\2\2\u0347\u0343")
        buf.write("\3\2\2\2\u0348\u00b4\3\2\2\2\u0349\u034a\7^\2\2\u034a")
        buf.write("\u034b\7w\2\2\u034b\u034c\7r\2\2\u034c\u034d\7u\2\2\u034d")
        buf.write("\u034e\7k\2\2\u034e\u034f\7n\2\2\u034f\u0350\7q\2\2\u0350")
        buf.write("\u035a\7p\2\2\u0351\u0352\7^\2\2\u0352\u0353\7W\2\2\u0353")
        buf.write("\u0354\7r\2\2\u0354\u0355\7u\2\2\u0355\u0356\7k\2\2\u0356")
        buf.write("\u0357\7n\2\2\u0357\u0358\7q\2\2\u0358\u035a\7p\2\2\u0359")
        buf.write("\u0349\3\2\2\2\u0359\u0351\3\2\2\2\u035a\u00b6\3\2\2\2")
        buf.write("\u035b\u035c\7^\2\2\u035c\u035d\7r\2\2\u035d\u035e\7j")
        buf.write("\2\2\u035e\u0364\7k\2\2\u035f\u0360\7^\2\2\u0360\u0361")
        buf.write("\7R\2\2\u0361\u0362\7j\2\2\u0362\u0364\7k\2\2\u0363\u035b")
        buf.write("\3\2\2\2\u0363\u035f\3\2\2\2\u0364\u00b8\3\2\2\2\u0365")
        buf.write("\u0366\7^\2\2\u0366\u0367\7e\2\2\u0367\u0368\7j\2\2\u0368")
        buf.write("\u036e\7k\2\2\u0369\u036a\7^\2\2\u036a\u036b\7E\2\2\u036b")
        buf.write("\u036c\7j\2\2\u036c\u036e\7k\2\2\u036d\u0365\3\2\2\2\u036d")
        buf.write("\u0369\3\2\2\2\u036e\u00ba\3\2\2\2\u036f\u0370\7^\2\2")
        buf.write("\u0370\u0371\7r\2\2\u0371\u0372\7u\2\2\u0372\u0378\7k")
        buf.write("\2\2\u0373\u0374\7^\2\2\u0374\u0375\7R\2\2\u0375\u0376")
        buf.write("\7u\2\2\u0376\u0378\7k\2\2\u0377\u036f\3\2\2\2\u0377\u0373")
        buf.write("\3\2\2\2\u0378\u00bc\3\2\2\2\u0379\u037a\7^\2\2\u037a")
        buf.write("\u037b\7q\2\2\u037b\u037c\7o\2\2\u037c\u037d\7g\2\2\u037d")
        buf.write("\u037e\7i\2\2\u037e\u0386\7c\2\2\u037f\u0380\7^\2\2\u0380")
        buf.write("\u0381\7Q\2\2\u0381\u0382\7o\2\2\u0382\u0383\7g\2\2\u0383")
        buf.write("\u0384\7i\2\2\u0384\u0386\7c\2\2\u0385\u0379\3\2\2\2\u0385")
        buf.write("\u037f\3\2\2\2\u0386\u00be\3\2\2\2\u0387\u03a0\5\u008f")
        buf.write("H\2\u0388\u03a0\5\u0091I\2\u0389\u03a0\5\u0093J\2\u038a")
        buf.write("\u03a0\5\u0095K\2\u038b\u03a0\5\u0097L\2\u038c\u03a0\5")
        buf.write("\u0099M\2\u038d\u03a0\5\u009bN\2\u038e\u03a0\5\u009dO")
        buf.write("\2\u038f\u03a0\5\u009fP\2\u0390\u03a0\5\u00a1Q\2\u0391")
        buf.write("\u03a0\5\u00a3R\2\u0392\u03a0\5\u00a5S\2\u0393\u03a0\5")
        buf.write("\u00a7T\2\u0394\u03a0\5\u00a9U\2\u0395\u03a0\5\u00abV")
        buf.write("\2\u0396\u03a0\5\u00adW\2\u0397\u03a0\5\u00afX\2\u0398")
        buf.write("\u03a0\5\u00b1Y\2\u0399\u03a0\5\u00b3Z\2\u039a\u03a0\5")
        buf.write("\u00b5[\2\u039b\u03a0\5\u00b7\\\2\u039c\u03a0\5\u00b9")
        buf.write("]\2\u039d\u03a0\5\u00bb^\2\u039e\u03a0\5\u00bd_\2\u039f")
        buf.write("\u0387\3\2\2\2\u039f\u0388\3\2\2\2\u039f\u0389\3\2\2\2")
        buf.write("\u039f\u038a\3\2\2\2\u039f\u038b\3\2\2\2\u039f\u038c\3")
        buf.write("\2\2\2\u039f\u038d\3\2\2\2\u039f\u038e\3\2\2\2\u039f\u038f")
        buf.write("\3\2\2\2\u039f\u0390\3\2\2\2\u039f\u0391\3\2\2\2\u039f")
        buf.write("\u0392\3\2\2\2\u039f\u0393\3\2\2\2\u039f\u0394\3\2\2\2")
        buf.write("\u039f\u0395\3\2\2\2\u039f\u0396\3\2\2\2\u039f\u0397\3")
        buf.write("\2\2\2\u039f\u0398\3\2\2\2\u039f\u0399\3\2\2\2\u039f\u039a")
        buf.write("\3\2\2\2\u039f\u039b\3\2\2\2\u039f\u039c\3\2\2\2\u039f")
        buf.write("\u039d\3\2\2\2\u039f\u039e\3\2\2\2\u03a0\u00c0\3\2\2\2")
        buf.write("\u03a1\u03a2\5\35\17\2\u03a2\u03a6\5\17\b\2\u03a3\u03a7")
        buf.write("\5y=\2\u03a4\u03a7\5u;\2\u03a5\u03a7\5\u00bf`\2\u03a6")
        buf.write("\u03a3\3\2\2\2\u03a6\u03a4\3\2\2\2\u03a6\u03a5\3\2\2\2")
        buf.write("\u03a7\u03a8\3\2\2\2\u03a8\u03a9\5\21\t\2\u03a9\u00c2")
        buf.write("\3\2\2\2\u03aa\u03ac\5q9\2\u03ab\u03ad\5\u00c1a\2\u03ac")
        buf.write("\u03ab\3\2\2\2\u03ac\u03ad\3\2\2\2\u03ad\u03ae\3\2\2\2")
        buf.write("\u03ae\u03af\5\17\b\2\u03af\u00c4\3\2\2\2\u03b0\u03b2")
        buf.write("\5q9\2\u03b1\u03b3\5\u00c1a\2\u03b2\u03b1\3\2\2\2\u03b2")
        buf.write("\u03b3\3\2\2\2\u03b3\u03b4\3\2\2\2\u03b4\u03b5\5\13\6")
        buf.write("\2\u03b5\u00c6\3\2\2\2\u03b6\u03b8\5\u00bf`\2\u03b7\u03b9")
        buf.write("\5\u00c1a\2\u03b8\u03b7\3\2\2\2\u03b8\u03b9\3\2\2\2\u03b9")
        buf.write("\u03ba\3\2\2\2\u03ba\u03bb\5\17\b\2\u03bb\u00c8\3\2\2")
        buf.write("\2\u03bc\u03be\5\u00bf`\2\u03bd\u03bf\5\u00c1a\2\u03be")
        buf.write("\u03bd\3\2\2\2\u03be\u03bf\3\2\2\2\u03bf\u03c0\3\2\2\2")
        buf.write("\u03c0\u03c1\5\13\6\2\u03c1\u00ca\3\2\2\2\u03c2\u03c4")
        buf.write("\t\6\2\2\u03c3\u03c2\3\2\2\2\u03c4\u03c5\3\2\2\2\u03c5")
        buf.write("\u03c3\3\2\2\2\u03c5\u03c6\3\2\2\2\u03c6\u03c7\3\2\2\2")
        buf.write("\u03c7\u03c8\bf\2\2\u03c8\u00cc\3\2\2\2H\2\u012b\u0142")
        buf.write("\u0149\u014f\u0156\u015d\u0164\u016b\u0172\u0179\u017f")
        buf.write("\u0185\u018b\u0191\u0197\u019d\u01a5\u01ad\u01b5\u01bb")
        buf.write("\u01c1\u01c7\u01cd\u01d3\u01d9\u01df\u01e5\u01eb\u01f3")
        buf.write("\u021a\u021e\u0223\u0227\u022c\u022e\u0239\u023e\u025b")
        buf.write("\u026b\u0277\u0285\u0293\u02a5\u02b1\u02bb\u02c9\u02d5")
        buf.write("\u02e3\u02f3\u02fb\u0303\u030b\u031d\u0325\u032f\u033d")
        buf.write("\u0347\u0359\u0363\u036d\u0377\u0385\u039f\u03a6\u03ac")
        buf.write("\u03b2\u03b8\u03be\u03c5\3\b\2\2")
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
    INEQUALITIES = 61
    BANG = 62
    GREEKLETTER = 63
    LETTERFUNCTIONBRACE = 64
    LETTERFUNCTIONPAREN = 65
    GREEKFUNCTIONBRACE = 66
    GREEKFUNCTIONPAREN = 67
    WS = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "'.'", "'|'", "'_'", "'^'", "':'", "'\\lim'", 
            "'\\int'", "'\\sum'", "'\\prod'", "'\\times'", "'\\cdot'", "'\\div'", 
            "'\\frac'", "'\\infty'", "'='", "'!'" ]

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
            "MIXNUMBER", "WORD", "INFINITY", "EQ", "INEQUALITIES", "BANG", 
            "GREEKLETTER", "LETTERFUNCTIONBRACE", "LETTERFUNCTIONPAREN", 
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
                  "WORD", "INFINITY", "EQ", "LT", "LTE", "GT", "GTE", "INEQUALITIES", 
                  "BANG", "ALPHA", "BETA", "GAMMA", "DELTA", "EPSILON", 
                  "ZETA", "ETA", "THETA", "IOTA", "KAPPA", "LAMBDA", "MU", 
                  "NU", "XI", "OMICRON", "PI", "RHO", "SIGMA", "TAU", "UPSILON", 
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


