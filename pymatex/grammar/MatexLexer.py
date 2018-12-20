# Generated from .\pymatex\grammar\MatexLexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u03cd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u012e\n\24\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\5\32\u0147\n")
        buf.write("\32\3\32\3\32\3\32\3\32\3\33\5\33\u014e\n\33\3\33\3\33")
        buf.write("\3\33\3\34\5\34\u0154\n\34\3\34\3\34\3\34\3\34\3\35\5")
        buf.write("\35\u015b\n\35\3\35\3\35\3\35\3\35\3\36\5\36\u0162\n\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\5\37\u0169\n\37\3\37\3\37\3")
        buf.write("\37\3\37\3 \5 \u0170\n \3 \3 \3 \3 \3!\5!\u0177\n!\3!")
        buf.write("\3!\3!\3!\3\"\5\"\u017e\n\"\3\"\3\"\3\"\3#\5#\u0184\n")
        buf.write("#\3#\3#\3#\3$\5$\u018a\n$\3$\3$\3$\3%\5%\u0190\n%\3%\3")
        buf.write("%\3%\3&\5&\u0196\n&\3&\3&\3&\3\'\5\'\u019c\n\'\3\'\3\'")
        buf.write("\3\'\3(\5(\u01a2\n(\3(\3(\3(\3(\3(\3)\5)\u01aa\n)\3)\3")
        buf.write(")\3)\3)\3)\3*\5*\u01b2\n*\3*\3*\3*\3*\3*\3+\5+\u01ba\n")
        buf.write("+\3+\3+\3+\3,\5,\u01c0\n,\3,\3,\3,\3-\5-\u01c6\n-\3-\3")
        buf.write("-\3-\3.\5.\u01cc\n.\3.\3.\3.\3/\5/\u01d2\n/\3/\3/\3/\3")
        buf.write("\60\5\60\u01d8\n\60\3\60\3\60\3\60\3\61\5\61\u01de\n\61")
        buf.write("\3\61\3\61\3\61\3\62\5\62\u01e4\n\62\3\62\3\62\3\62\3")
        buf.write("\63\5\63\u01ea\n\63\3\63\3\63\3\63\3\64\5\64\u01f0\n\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\5\65\u01f8\n\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\39")
        buf.write("\39\39\39\39\39\3:\3:\3;\3;\3<\7<\u021d\n<\f<\16<\u0220")
        buf.write("\13<\3<\5<\u0223\n<\3<\6<\u0226\n<\r<\16<\u0227\3<\3<")
        buf.write("\5<\u022c\n<\3<\6<\u022f\n<\r<\16<\u0230\5<\u0233\n<\3")
        buf.write("=\3=\3=\3>\3>\3?\3?\6?\u023c\n?\r?\16?\u023d\3@\6@\u0241")
        buf.write("\n@\r@\16@\u0242\3A\3A\3A\3A\3A\3A\3A\3B\3B\3C\3C\3D\3")
        buf.write("D\3D\3D\3D\3E\3E\3F\3F\3F\3F\3F\3G\3G\3G\3G\5G\u0260\n")
        buf.write("G\3H\3H\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u0270\n")
        buf.write("I\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u027c\nJ\3K\3K\3K\3")
        buf.write("K\3K\3K\3K\3K\3K\3K\3K\3K\5K\u028a\nK\3L\3L\3L\3L\3L\3")
        buf.write("L\3L\3L\3L\3L\3L\3L\5L\u0298\nL\3M\3M\3M\3M\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\3M\3M\3M\3M\3M\5M\u02aa\nM\3N\3N\3N\3N\3N\3")
        buf.write("N\3N\3N\3N\3N\5N\u02b6\nN\3O\3O\3O\3O\3O\3O\3O\3O\5O\u02c0")
        buf.write("\nO\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u02ce\nP\3")
        buf.write("Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u02da\nQ\3R\3R\3R\3R\3")
        buf.write("R\3R\3R\3R\3R\3R\3R\3R\5R\u02e8\nR\3S\3S\3S\3S\3S\3S\3")
        buf.write("S\3S\3S\3S\3S\3S\3S\3S\5S\u02f8\nS\3T\3T\3T\3T\3T\3T\5")
        buf.write("T\u0300\nT\3U\3U\3U\3U\3U\3U\5U\u0308\nU\3V\3V\3V\3V\3")
        buf.write("V\3V\5V\u0310\nV\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3")
        buf.write("W\3W\3W\3W\5W\u0322\nW\3X\3X\3X\3X\3X\3X\5X\u032a\nX\3")
        buf.write("Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\5Y\u0334\nY\3Z\3Z\3Z\3Z\3Z\3Z\3")
        buf.write("Z\3Z\3Z\3Z\3Z\3Z\5Z\u0342\nZ\3[\3[\3[\3[\3[\3[\3[\3[\5")
        buf.write("[\u034c\n[\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\")
        buf.write("\3\\\3\\\3\\\3\\\3\\\5\\\u035e\n\\\3]\3]\3]\3]\3]\3]\3")
        buf.write("]\3]\5]\u0368\n]\3^\3^\3^\3^\3^\3^\3^\3^\5^\u0372\n^\3")
        buf.write("_\3_\3_\3_\3_\3_\3_\3_\5_\u037c\n_\3`\3`\3`\3`\3`\3`\3")
        buf.write("`\3`\3`\3`\3`\3`\5`\u038a\n`\3a\3a\3a\3a\3a\3a\3a\3a\3")
        buf.write("a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\5a\u03a4")
        buf.write("\na\3b\3b\3b\3b\3b\5b\u03ab\nb\3b\3b\3c\3c\5c\u03b1\n")
        buf.write("c\3c\3c\3d\3d\5d\u03b7\nd\3d\3d\3e\3e\5e\u03bd\ne\3e\3")
        buf.write("e\3f\3f\5f\u03c3\nf\3f\3f\3g\6g\u03c8\ng\rg\16g\u03c9")
        buf.write("\3g\3g\2\2h\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\2%\23\'\24)\25+\26")
        buf.write("-\27/\30\61\2\63\31\65\32\67\339\34;\35=\36?\37A C!E\"")
        buf.write("G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66")
        buf.write("o\67q8s\2u\2w9y:{;}<\177=\u0081>\u0083?\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d@\u008fA\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3")
        buf.write("\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1")
        buf.write("\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf")
        buf.write("\2\u00c1B\u00c3\2\u00c5C\u00c7D\u00c9E\u00cbF\u00cdG\3")
        buf.write("\2\7\4\2C\\c|\3\2\62;\4\2GGgg\4\2--//\5\2\13\f\17\17\"")
        buf.write("\"\2\u040c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2w")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u00c1\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2")
        buf.write("\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\3\u00cf")
        buf.write("\3\2\2\2\5\u00d1\3\2\2\2\7\u00d3\3\2\2\2\t\u00d5\3\2\2")
        buf.write("\2\13\u00d7\3\2\2\2\r\u00d9\3\2\2\2\17\u00db\3\2\2\2\21")
        buf.write("\u00dd\3\2\2\2\23\u00df\3\2\2\2\25\u00e1\3\2\2\2\27\u00e3")
        buf.write("\3\2\2\2\31\u00e5\3\2\2\2\33\u00e7\3\2\2\2\35\u00e9\3")
        buf.write("\2\2\2\37\u00eb\3\2\2\2!\u00ed\3\2\2\2#\u00ef\3\2\2\2")
        buf.write("%\u00f1\3\2\2\2\'\u012d\3\2\2\2)\u012f\3\2\2\2+\u0131")
        buf.write("\3\2\2\2-\u0136\3\2\2\2/\u013b\3\2\2\2\61\u0141\3\2\2")
        buf.write("\2\63\u0146\3\2\2\2\65\u014d\3\2\2\2\67\u0153\3\2\2\2")
        buf.write("9\u015a\3\2\2\2;\u0161\3\2\2\2=\u0168\3\2\2\2?\u016f\3")
        buf.write("\2\2\2A\u0176\3\2\2\2C\u017d\3\2\2\2E\u0183\3\2\2\2G\u0189")
        buf.write("\3\2\2\2I\u018f\3\2\2\2K\u0195\3\2\2\2M\u019b\3\2\2\2")
        buf.write("O\u01a1\3\2\2\2Q\u01a9\3\2\2\2S\u01b1\3\2\2\2U\u01b9\3")
        buf.write("\2\2\2W\u01bf\3\2\2\2Y\u01c5\3\2\2\2[\u01cb\3\2\2\2]\u01d1")
        buf.write("\3\2\2\2_\u01d7\3\2\2\2a\u01dd\3\2\2\2c\u01e3\3\2\2\2")
        buf.write("e\u01e9\3\2\2\2g\u01ef\3\2\2\2i\u01f7\3\2\2\2k\u01ff\3")
        buf.write("\2\2\2m\u0206\3\2\2\2o\u020c\3\2\2\2q\u0211\3\2\2\2s\u0217")
        buf.write("\3\2\2\2u\u0219\3\2\2\2w\u021e\3\2\2\2y\u0234\3\2\2\2")
        buf.write("{\u0237\3\2\2\2}\u0239\3\2\2\2\177\u0240\3\2\2\2\u0081")
        buf.write("\u0244\3\2\2\2\u0083\u024b\3\2\2\2\u0085\u024d\3\2\2\2")
        buf.write("\u0087\u024f\3\2\2\2\u0089\u0254\3\2\2\2\u008b\u0256\3")
        buf.write("\2\2\2\u008d\u025f\3\2\2\2\u008f\u0261\3\2\2\2\u0091\u026f")
        buf.write("\3\2\2\2\u0093\u027b\3\2\2\2\u0095\u0289\3\2\2\2\u0097")
        buf.write("\u0297\3\2\2\2\u0099\u02a9\3\2\2\2\u009b\u02b5\3\2\2\2")
        buf.write("\u009d\u02bf\3\2\2\2\u009f\u02cd\3\2\2\2\u00a1\u02d9\3")
        buf.write("\2\2\2\u00a3\u02e7\3\2\2\2\u00a5\u02f7\3\2\2\2\u00a7\u02ff")
        buf.write("\3\2\2\2\u00a9\u0307\3\2\2\2\u00ab\u030f\3\2\2\2\u00ad")
        buf.write("\u0321\3\2\2\2\u00af\u0329\3\2\2\2\u00b1\u0333\3\2\2\2")
        buf.write("\u00b3\u0341\3\2\2\2\u00b5\u034b\3\2\2\2\u00b7\u035d\3")
        buf.write("\2\2\2\u00b9\u0367\3\2\2\2\u00bb\u0371\3\2\2\2\u00bd\u037b")
        buf.write("\3\2\2\2\u00bf\u0389\3\2\2\2\u00c1\u03a3\3\2\2\2\u00c3")
        buf.write("\u03a5\3\2\2\2\u00c5\u03ae\3\2\2\2\u00c7\u03b4\3\2\2\2")
        buf.write("\u00c9\u03ba\3\2\2\2\u00cb\u03c0\3\2\2\2\u00cd\u03c7\3")
        buf.write("\2\2\2\u00cf\u00d0\7-\2\2\u00d0\4\3\2\2\2\u00d1\u00d2")
        buf.write("\7/\2\2\u00d2\6\3\2\2\2\u00d3\u00d4\7,\2\2\u00d4\b\3\2")
        buf.write("\2\2\u00d5\u00d6\7\61\2\2\u00d6\n\3\2\2\2\u00d7\u00d8")
        buf.write("\7*\2\2\u00d8\f\3\2\2\2\u00d9\u00da\7+\2\2\u00da\16\3")
        buf.write("\2\2\2\u00db\u00dc\7}\2\2\u00dc\20\3\2\2\2\u00dd\u00de")
        buf.write("\7\177\2\2\u00de\22\3\2\2\2\u00df\u00e0\7]\2\2\u00e0\24")
        buf.write("\3\2\2\2\u00e1\u00e2\7_\2\2\u00e2\26\3\2\2\2\u00e3\u00e4")
        buf.write("\7.\2\2\u00e4\30\3\2\2\2\u00e5\u00e6\7\60\2\2\u00e6\32")
        buf.write("\3\2\2\2\u00e7\u00e8\7~\2\2\u00e8\34\3\2\2\2\u00e9\u00ea")
        buf.write("\7a\2\2\u00ea\36\3\2\2\2\u00eb\u00ec\7`\2\2\u00ec \3\2")
        buf.write("\2\2\u00ed\u00ee\7<\2\2\u00ee\"\3\2\2\2\u00ef\u00f0\7")
        buf.write("^\2\2\u00f0$\3\2\2\2\u00f1\u00f2\7^\2\2\u00f2\u00f3\7")
        buf.write("n\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7o\2\2\u00f5&\3\2")
        buf.write("\2\2\u00f6\u00f7\7^\2\2\u00f7\u00f8\7v\2\2\u00f8\u012e")
        buf.write("\7q\2\2\u00f9\u00fa\7^\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7i\2\2\u00fd\u00fe\7j\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7t\2\2\u0102\u0103\7q\2\2\u0103\u012e\7y\2\2\u0104\u0105")
        buf.write("\7^\2\2\u0105\u0106\7T\2\2\u0106\u0107\7k\2\2\u0107\u0108")
        buf.write("\7i\2\2\u0108\u0109\7j\2\2\u0109\u010a\7v\2\2\u010a\u010b")
        buf.write("\7c\2\2\u010b\u010c\7t\2\2\u010c\u010d\7t\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e\u012e\7y\2\2\u010f\u0110\7^\2\2\u0110\u0111")
        buf.write("\7n\2\2\u0111\u0112\7q\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7i\2\2\u0114\u0115\7t\2\2\u0115\u0116\7k\2\2\u0116\u0117")
        buf.write("\7i\2\2\u0117\u0118\7j\2\2\u0118\u0119\7v\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7t\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7q\2\2\u011d\u012e\7y\2\2\u011e\u011f\7^\2\2\u011f\u0120")
        buf.write("\7N\2\2\u0120\u0121\7q\2\2\u0121\u0122\7p\2\2\u0122\u0123")
        buf.write("\7i\2\2\u0123\u0124\7t\2\2\u0124\u0125\7k\2\2\u0125\u0126")
        buf.write("\7i\2\2\u0126\u0127\7j\2\2\u0127\u0128\7v\2\2\u0128\u0129")
        buf.write("\7c\2\2\u0129\u012a\7t\2\2\u012a\u012b\7t\2\2\u012b\u012c")
        buf.write("\7q\2\2\u012c\u012e\7y\2\2\u012d\u00f6\3\2\2\2\u012d\u00f9")
        buf.write("\3\2\2\2\u012d\u0104\3\2\2\2\u012d\u010f\3\2\2\2\u012d")
        buf.write("\u011e\3\2\2\2\u012e(\3\2\2\2\u012f\u0130\7M\2\2\u0130")
        buf.write("*\3\2\2\2\u0131\u0132\7^\2\2\u0132\u0133\7k\2\2\u0133")
        buf.write("\u0134\7p\2\2\u0134\u0135\7v\2\2\u0135,\3\2\2\2\u0136")
        buf.write("\u0137\7^\2\2\u0137\u0138\7u\2\2\u0138\u0139\7w\2\2\u0139")
        buf.write("\u013a\7o\2\2\u013a.\3\2\2\2\u013b\u013c\7^\2\2\u013c")
        buf.write("\u013d\7r\2\2\u013d\u013e\7t\2\2\u013e\u013f\7q\2\2\u013f")
        buf.write("\u0140\7f\2\2\u0140\60\3\2\2\2\u0141\u0142\7c\2\2\u0142")
        buf.write("\u0143\7t\2\2\u0143\u0144\7e\2\2\u0144\62\3\2\2\2\u0145")
        buf.write("\u0147\5#\22\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148\u0149\7n\2\2\u0149\u014a\7")
        buf.write("q\2\2\u014a\u014b\7i\2\2\u014b\64\3\2\2\2\u014c\u014e")
        buf.write("\5#\22\2\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0150\7n\2\2\u0150\u0151\7p\2\2\u0151")
        buf.write("\66\3\2\2\2\u0152\u0154\5#\22\2\u0153\u0152\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\7u\2\2")
        buf.write("\u0156\u0157\7k\2\2\u0157\u0158\7p\2\2\u01588\3\2\2\2")
        buf.write("\u0159\u015b\5#\22\2\u015a\u0159\3\2\2\2\u015a\u015b\3")
        buf.write("\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\7e\2\2\u015d\u015e")
        buf.write("\7q\2\2\u015e\u015f\7u\2\2\u015f:\3\2\2\2\u0160\u0162")
        buf.write("\5#\22\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0164\7v\2\2\u0164\u0165\7c\2\2\u0165")
        buf.write("\u0166\7p\2\2\u0166<\3\2\2\2\u0167\u0169\5#\22\2\u0168")
        buf.write("\u0167\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016a\u016b\7e\2\2\u016b\u016c\7u\2\2\u016c\u016d\7e")
        buf.write("\2\2\u016d>\3\2\2\2\u016e\u0170\5#\22\2\u016f\u016e\3")
        buf.write("\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172")
        buf.write("\7u\2\2\u0172\u0173\7g\2\2\u0173\u0174\7e\2\2\u0174@\3")
        buf.write("\2\2\2\u0175\u0177\5#\22\2\u0176\u0175\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\7e\2\2\u0179")
        buf.write("\u017a\7q\2\2\u017a\u017b\7v\2\2\u017bB\3\2\2\2\u017c")
        buf.write("\u017e\5#\22\2\u017d\u017c\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u0180\5\61\31\2\u0180\u0181")
        buf.write("\5\67\34\2\u0181D\3\2\2\2\u0182\u0184\5#\22\2\u0183\u0182")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("\u0186\5\61\31\2\u0186\u0187\59\35\2\u0187F\3\2\2\2\u0188")
        buf.write("\u018a\5#\22\2\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2")
        buf.write("\u018a\u018b\3\2\2\2\u018b\u018c\5\61\31\2\u018c\u018d")
        buf.write("\5;\36\2\u018dH\3\2\2\2\u018e\u0190\5#\22\2\u018f\u018e")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("\u0192\5\61\31\2\u0192\u0193\5=\37\2\u0193J\3\2\2\2\u0194")
        buf.write("\u0196\5#\22\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0198\5\61\31\2\u0198\u0199")
        buf.write("\5? \2\u0199L\3\2\2\2\u019a\u019c\5#\22\2\u019b\u019a")
        buf.write("\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u019e\5\61\31\2\u019e\u019f\5A!\2\u019fN\3\2\2\2\u01a0")
        buf.write("\u01a2\5#\22\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3\u01a4\7u\2\2\u01a4\u01a5\7")
        buf.write("k\2\2\u01a5\u01a6\7p\2\2\u01a6\u01a7\7j\2\2\u01a7P\3\2")
        buf.write("\2\2\u01a8\u01aa\5#\22\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\7e\2\2\u01ac")
        buf.write("\u01ad\7q\2\2\u01ad\u01ae\7u\2\2\u01ae\u01af\7j\2\2\u01af")
        buf.write("R\3\2\2\2\u01b0\u01b2\5#\22\2\u01b1\u01b0\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\7v\2\2")
        buf.write("\u01b4\u01b5\7c\2\2\u01b5\u01b6\7p\2\2\u01b6\u01b7\7j")
        buf.write("\2\2\u01b7T\3\2\2\2\u01b8\u01ba\5#\22\2\u01b9\u01b8\3")
        buf.write("\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc")
        buf.write("\5\61\31\2\u01bc\u01bd\5O(\2\u01bdV\3\2\2\2\u01be\u01c0")
        buf.write("\5#\22\2\u01bf\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01c1\3\2\2\2\u01c1\u01c2\5\61\31\2\u01c2\u01c3\5Q)\2")
        buf.write("\u01c3X\3\2\2\2\u01c4\u01c6\5#\22\2\u01c5\u01c4\3\2\2")
        buf.write("\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8")
        buf.write("\5\61\31\2\u01c8\u01c9\5S*\2\u01c9Z\3\2\2\2\u01ca\u01cc")
        buf.write("\5#\22\2\u01cb\u01ca\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01ce\7e\2\2\u01ce\u01cf\7p\2\2\u01cf")
        buf.write("\\\3\2\2\2\u01d0\u01d2\5#\22\2\u01d1\u01d0\3\2\2\2\u01d1")
        buf.write("\u01d2\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\7u\2\2")
        buf.write("\u01d4\u01d5\7p\2\2\u01d5^\3\2\2\2\u01d6\u01d8\5#\22\2")
        buf.write("\u01d7\u01d6\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3")
        buf.write("\2\2\2\u01d9\u01da\7f\2\2\u01da\u01db\7p\2\2\u01db`\3")
        buf.write("\2\2\2\u01dc\u01de\5#\22\2\u01dd\u01dc\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\5\61\31\2\u01e0")
        buf.write("\u01e1\5[.\2\u01e1b\3\2\2\2\u01e2\u01e4\5#\22\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5\3\2\2\2")
        buf.write("\u01e5\u01e6\5\61\31\2\u01e6\u01e7\5]/\2\u01e7d\3\2\2")
        buf.write("\2\u01e8\u01ea\5#\22\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea")
        buf.write("\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\5\61\31\2\u01ec")
        buf.write("\u01ed\5_\60\2\u01edf\3\2\2\2\u01ee\u01f0\5#\22\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01f2\7u\2\2\u01f2\u01f3\7s\2\2\u01f3\u01f4\7t")
        buf.write("\2\2\u01f4\u01f5\7v\2\2\u01f5h\3\2\2\2\u01f6\u01f8\5#")
        buf.write("\22\2\u01f7\u01f6\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9")
        buf.write("\3\2\2\2\u01f9\u01fa\7d\2\2\u01fa\u01fb\7k\2\2\u01fb\u01fc")
        buf.write("\7p\2\2\u01fc\u01fd\7q\2\2\u01fd\u01fe\7o\2\2\u01fej\3")
        buf.write("\2\2\2\u01ff\u0200\7^\2\2\u0200\u0201\7v\2\2\u0201\u0202")
        buf.write("\7k\2\2\u0202\u0203\7o\2\2\u0203\u0204\7g\2\2\u0204\u0205")
        buf.write("\7u\2\2\u0205l\3\2\2\2\u0206\u0207\7^\2\2\u0207\u0208")
        buf.write("\7e\2\2\u0208\u0209\7f\2\2\u0209\u020a\7q\2\2\u020a\u020b")
        buf.write("\7v\2\2\u020bn\3\2\2\2\u020c\u020d\7^\2\2\u020d\u020e")
        buf.write("\7f\2\2\u020e\u020f\7k\2\2\u020f\u0210\7x\2\2\u0210p\3")
        buf.write("\2\2\2\u0211\u0212\7^\2\2\u0212\u0213\7h\2\2\u0213\u0214")
        buf.write("\7t\2\2\u0214\u0215\7c\2\2\u0215\u0216\7e\2\2\u0216r\3")
        buf.write("\2\2\2\u0217\u0218\t\2\2\2\u0218t\3\2\2\2\u0219\u021a")
        buf.write("\t\3\2\2\u021av\3\2\2\2\u021b\u021d\5u;\2\u021c\u021b")
        buf.write("\3\2\2\2\u021d\u0220\3\2\2\2\u021e\u021c\3\2\2\2\u021e")
        buf.write("\u021f\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0221\u0223\7\60\2\2\u0222\u0221\3\2\2\2\u0222\u0223")
        buf.write("\3\2\2\2\u0223\u0225\3\2\2\2\u0224\u0226\5u;\2\u0225\u0224")
        buf.write("\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0225\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228\u0232\3\2\2\2\u0229\u022b\t\4\2\2")
        buf.write("\u022a\u022c\t\5\2\2\u022b\u022a\3\2\2\2\u022b\u022c\3")
        buf.write("\2\2\2\u022c\u022e\3\2\2\2\u022d\u022f\5u;\2\u022e\u022d")
        buf.write("\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u022e\3\2\2\2\u0230")
        buf.write("\u0231\3\2\2\2\u0231\u0233\3\2\2\2\u0232\u0229\3\2\2\2")
        buf.write("\u0232\u0233\3\2\2\2\u0233x\3\2\2\2\u0234\u0235\7f\2\2")
        buf.write("\u0235\u0236\5s:\2\u0236z\3\2\2\2\u0237\u0238\5s:\2\u0238")
        buf.write("|\3\2\2\2\u0239\u023b\5w<\2\u023a\u023c\5{>\2\u023b\u023a")
        buf.write("\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023b\3\2\2\2\u023d")
        buf.write("\u023e\3\2\2\2\u023e~\3\2\2\2\u023f\u0241\5{>\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0240\3\2\2\2")
        buf.write("\u0242\u0243\3\2\2\2\u0243\u0080\3\2\2\2\u0244\u0245\7")
        buf.write("^\2\2\u0245\u0246\7k\2\2\u0246\u0247\7p\2\2\u0247\u0248")
        buf.write("\7h\2\2\u0248\u0249\7v\2\2\u0249\u024a\7{\2\2\u024a\u0082")
        buf.write("\3\2\2\2\u024b\u024c\7?\2\2\u024c\u0084\3\2\2\2\u024d")
        buf.write("\u024e\7>\2\2\u024e\u0086\3\2\2\2\u024f\u0250\7^\2\2\u0250")
        buf.write("\u0251\7n\2\2\u0251\u0252\7g\2\2\u0252\u0253\7s\2\2\u0253")
        buf.write("\u0088\3\2\2\2\u0254\u0255\7@\2\2\u0255\u008a\3\2\2\2")
        buf.write("\u0256\u0257\7^\2\2\u0257\u0258\7i\2\2\u0258\u0259\7g")
        buf.write("\2\2\u0259\u025a\7s\2\2\u025a\u008c\3\2\2\2\u025b\u0260")
        buf.write("\5\u0085C\2\u025c\u0260\5\u0087D\2\u025d\u0260\5\u0089")
        buf.write("E\2\u025e\u0260\5\u008bF\2\u025f\u025b\3\2\2\2\u025f\u025c")
        buf.write("\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u025e\3\2\2\2\u0260")
        buf.write("\u008e\3\2\2\2\u0261\u0262\7#\2\2\u0262\u0090\3\2\2\2")
        buf.write("\u0263\u0264\7^\2\2\u0264\u0265\7c\2\2\u0265\u0266\7n")
        buf.write("\2\2\u0266\u0267\7r\2\2\u0267\u0268\7j\2\2\u0268\u0270")
        buf.write("\7c\2\2\u0269\u026a\7^\2\2\u026a\u026b\7C\2\2\u026b\u026c")
        buf.write("\7n\2\2\u026c\u026d\7r\2\2\u026d\u026e\7j\2\2\u026e\u0270")
        buf.write("\7c\2\2\u026f\u0263\3\2\2\2\u026f\u0269\3\2\2\2\u0270")
        buf.write("\u0092\3\2\2\2\u0271\u0272\7^\2\2\u0272\u0273\7d\2\2\u0273")
        buf.write("\u0274\7g\2\2\u0274\u0275\7v\2\2\u0275\u027c\7c\2\2\u0276")
        buf.write("\u0277\7^\2\2\u0277\u0278\7D\2\2\u0278\u0279\7g\2\2\u0279")
        buf.write("\u027a\7v\2\2\u027a\u027c\7c\2\2\u027b\u0271\3\2\2\2\u027b")
        buf.write("\u0276\3\2\2\2\u027c\u0094\3\2\2\2\u027d\u027e\7^\2\2")
        buf.write("\u027e\u027f\7i\2\2\u027f\u0280\7c\2\2\u0280\u0281\7o")
        buf.write("\2\2\u0281\u0282\7o\2\2\u0282\u028a\7c\2\2\u0283\u0284")
        buf.write("\7^\2\2\u0284\u0285\7I\2\2\u0285\u0286\7c\2\2\u0286\u0287")
        buf.write("\7o\2\2\u0287\u0288\7o\2\2\u0288\u028a\7c\2\2\u0289\u027d")
        buf.write("\3\2\2\2\u0289\u0283\3\2\2\2\u028a\u0096\3\2\2\2\u028b")
        buf.write("\u028c\7^\2\2\u028c\u028d\7f\2\2\u028d\u028e\7g\2\2\u028e")
        buf.write("\u028f\7n\2\2\u028f\u0290\7v\2\2\u0290\u0298\7c\2\2\u0291")
        buf.write("\u0292\7^\2\2\u0292\u0293\7F\2\2\u0293\u0294\7g\2\2\u0294")
        buf.write("\u0295\7n\2\2\u0295\u0296\7v\2\2\u0296\u0298\7c\2\2\u0297")
        buf.write("\u028b\3\2\2\2\u0297\u0291\3\2\2\2\u0298\u0098\3\2\2\2")
        buf.write("\u0299\u029a\7^\2\2\u029a\u029b\7g\2\2\u029b\u029c\7r")
        buf.write("\2\2\u029c\u029d\7u\2\2\u029d\u029e\7k\2\2\u029e\u029f")
        buf.write("\7n\2\2\u029f\u02a0\7q\2\2\u02a0\u02aa\7p\2\2\u02a1\u02a2")
        buf.write("\7^\2\2\u02a2\u02a3\7G\2\2\u02a3\u02a4\7r\2\2\u02a4\u02a5")
        buf.write("\7u\2\2\u02a5\u02a6\7k\2\2\u02a6\u02a7\7n\2\2\u02a7\u02a8")
        buf.write("\7q\2\2\u02a8\u02aa\7p\2\2\u02a9\u0299\3\2\2\2\u02a9\u02a1")
        buf.write("\3\2\2\2\u02aa\u009a\3\2\2\2\u02ab\u02ac\7^\2\2\u02ac")
        buf.write("\u02ad\7|\2\2\u02ad\u02ae\7g\2\2\u02ae\u02af\7v\2\2\u02af")
        buf.write("\u02b6\7c\2\2\u02b0\u02b1\7^\2\2\u02b1\u02b2\7\\\2\2\u02b2")
        buf.write("\u02b3\7g\2\2\u02b3\u02b4\7v\2\2\u02b4\u02b6\7c\2\2\u02b5")
        buf.write("\u02ab\3\2\2\2\u02b5\u02b0\3\2\2\2\u02b6\u009c\3\2\2\2")
        buf.write("\u02b7\u02b8\7^\2\2\u02b8\u02b9\7g\2\2\u02b9\u02ba\7v")
        buf.write("\2\2\u02ba\u02c0\7c\2\2\u02bb\u02bc\7^\2\2\u02bc\u02bd")
        buf.write("\7G\2\2\u02bd\u02be\7v\2\2\u02be\u02c0\7c\2\2\u02bf\u02b7")
        buf.write("\3\2\2\2\u02bf\u02bb\3\2\2\2\u02c0\u009e\3\2\2\2\u02c1")
        buf.write("\u02c2\7^\2\2\u02c2\u02c3\7v\2\2\u02c3\u02c4\7j\2\2\u02c4")
        buf.write("\u02c5\7g\2\2\u02c5\u02c6\7v\2\2\u02c6\u02ce\7c\2\2\u02c7")
        buf.write("\u02c8\7^\2\2\u02c8\u02c9\7V\2\2\u02c9\u02ca\7j\2\2\u02ca")
        buf.write("\u02cb\7g\2\2\u02cb\u02cc\7v\2\2\u02cc\u02ce\7c\2\2\u02cd")
        buf.write("\u02c1\3\2\2\2\u02cd\u02c7\3\2\2\2\u02ce\u00a0\3\2\2\2")
        buf.write("\u02cf\u02d0\7^\2\2\u02d0\u02d1\7k\2\2\u02d1\u02d2\7q")
        buf.write("\2\2\u02d2\u02d3\7v\2\2\u02d3\u02da\7c\2\2\u02d4\u02d5")
        buf.write("\7^\2\2\u02d5\u02d6\7K\2\2\u02d6\u02d7\7q\2\2\u02d7\u02d8")
        buf.write("\7v\2\2\u02d8\u02da\7c\2\2\u02d9\u02cf\3\2\2\2\u02d9\u02d4")
        buf.write("\3\2\2\2\u02da\u00a2\3\2\2\2\u02db\u02dc\7^\2\2\u02dc")
        buf.write("\u02dd\7m\2\2\u02dd\u02de\7c\2\2\u02de\u02df\7r\2\2\u02df")
        buf.write("\u02e0\7r\2\2\u02e0\u02e8\7c\2\2\u02e1\u02e2\7^\2\2\u02e2")
        buf.write("\u02e3\7M\2\2\u02e3\u02e4\7c\2\2\u02e4\u02e5\7r\2\2\u02e5")
        buf.write("\u02e6\7r\2\2\u02e6\u02e8\7c\2\2\u02e7\u02db\3\2\2\2\u02e7")
        buf.write("\u02e1\3\2\2\2\u02e8\u00a4\3\2\2\2\u02e9\u02ea\7^\2\2")
        buf.write("\u02ea\u02eb\7n\2\2\u02eb\u02ec\7c\2\2\u02ec\u02ed\7o")
        buf.write("\2\2\u02ed\u02ee\7d\2\2\u02ee\u02ef\7f\2\2\u02ef\u02f8")
        buf.write("\7c\2\2\u02f0\u02f1\7^\2\2\u02f1\u02f2\7N\2\2\u02f2\u02f3")
        buf.write("\7c\2\2\u02f3\u02f4\7o\2\2\u02f4\u02f5\7d\2\2\u02f5\u02f6")
        buf.write("\7f\2\2\u02f6\u02f8\7c\2\2\u02f7\u02e9\3\2\2\2\u02f7\u02f0")
        buf.write("\3\2\2\2\u02f8\u00a6\3\2\2\2\u02f9\u02fa\7^\2\2\u02fa")
        buf.write("\u02fb\7o\2\2\u02fb\u0300\7w\2\2\u02fc\u02fd\7^\2\2\u02fd")
        buf.write("\u02fe\7O\2\2\u02fe\u0300\7w\2\2\u02ff\u02f9\3\2\2\2\u02ff")
        buf.write("\u02fc\3\2\2\2\u0300\u00a8\3\2\2\2\u0301\u0302\7^\2\2")
        buf.write("\u0302\u0303\7p\2\2\u0303\u0308\7w\2\2\u0304\u0305\7^")
        buf.write("\2\2\u0305\u0306\7P\2\2\u0306\u0308\7w\2\2\u0307\u0301")
        buf.write("\3\2\2\2\u0307\u0304\3\2\2\2\u0308\u00aa\3\2\2\2\u0309")
        buf.write("\u030a\7^\2\2\u030a\u030b\7z\2\2\u030b\u0310\7k\2\2\u030c")
        buf.write("\u030d\7^\2\2\u030d\u030e\7Z\2\2\u030e\u0310\7k\2\2\u030f")
        buf.write("\u0309\3\2\2\2\u030f\u030c\3\2\2\2\u0310\u00ac\3\2\2\2")
        buf.write("\u0311\u0312\7^\2\2\u0312\u0313\7q\2\2\u0313\u0314\7o")
        buf.write("\2\2\u0314\u0315\7k\2\2\u0315\u0316\7e\2\2\u0316\u0317")
        buf.write("\7t\2\2\u0317\u0318\7q\2\2\u0318\u0322\7p\2\2\u0319\u031a")
        buf.write("\7^\2\2\u031a\u031b\7Q\2\2\u031b\u031c\7o\2\2\u031c\u031d")
        buf.write("\7k\2\2\u031d\u031e\7e\2\2\u031e\u031f\7t\2\2\u031f\u0320")
        buf.write("\7q\2\2\u0320\u0322\7p\2\2\u0321\u0311\3\2\2\2\u0321\u0319")
        buf.write("\3\2\2\2\u0322\u00ae\3\2\2\2\u0323\u0324\7^\2\2\u0324")
        buf.write("\u0325\7r\2\2\u0325\u032a\7k\2\2\u0326\u0327\7^\2\2\u0327")
        buf.write("\u0328\7R\2\2\u0328\u032a\7k\2\2\u0329\u0323\3\2\2\2\u0329")
        buf.write("\u0326\3\2\2\2\u032a\u00b0\3\2\2\2\u032b\u032c\7^\2\2")
        buf.write("\u032c\u032d\7t\2\2\u032d\u032e\7j\2\2\u032e\u0334\7q")
        buf.write("\2\2\u032f\u0330\7^\2\2\u0330\u0331\7T\2\2\u0331\u0332")
        buf.write("\7j\2\2\u0332\u0334\7q\2\2\u0333\u032b\3\2\2\2\u0333\u032f")
        buf.write("\3\2\2\2\u0334\u00b2\3\2\2\2\u0335\u0336\7^\2\2\u0336")
        buf.write("\u0337\7u\2\2\u0337\u0338\7k\2\2\u0338\u0339\7i\2\2\u0339")
        buf.write("\u033a\7o\2\2\u033a\u0342\7c\2\2\u033b\u033c\7^\2\2\u033c")
        buf.write("\u033d\7U\2\2\u033d\u033e\7k\2\2\u033e\u033f\7i\2\2\u033f")
        buf.write("\u0340\7o\2\2\u0340\u0342\7c\2\2\u0341\u0335\3\2\2\2\u0341")
        buf.write("\u033b\3\2\2\2\u0342\u00b4\3\2\2\2\u0343\u0344\7^\2\2")
        buf.write("\u0344\u0345\7v\2\2\u0345\u0346\7c\2\2\u0346\u034c\7w")
        buf.write("\2\2\u0347\u0348\7^\2\2\u0348\u0349\7V\2\2\u0349\u034a")
        buf.write("\7c\2\2\u034a\u034c\7w\2\2\u034b\u0343\3\2\2\2\u034b\u0347")
        buf.write("\3\2\2\2\u034c\u00b6\3\2\2\2\u034d\u034e\7^\2\2\u034e")
        buf.write("\u034f\7w\2\2\u034f\u0350\7r\2\2\u0350\u0351\7u\2\2\u0351")
        buf.write("\u0352\7k\2\2\u0352\u0353\7n\2\2\u0353\u0354\7q\2\2\u0354")
        buf.write("\u035e\7p\2\2\u0355\u0356\7^\2\2\u0356\u0357\7W\2\2\u0357")
        buf.write("\u0358\7r\2\2\u0358\u0359\7u\2\2\u0359\u035a\7k\2\2\u035a")
        buf.write("\u035b\7n\2\2\u035b\u035c\7q\2\2\u035c\u035e\7p\2\2\u035d")
        buf.write("\u034d\3\2\2\2\u035d\u0355\3\2\2\2\u035e\u00b8\3\2\2\2")
        buf.write("\u035f\u0360\7^\2\2\u0360\u0361\7r\2\2\u0361\u0362\7j")
        buf.write("\2\2\u0362\u0368\7k\2\2\u0363\u0364\7^\2\2\u0364\u0365")
        buf.write("\7R\2\2\u0365\u0366\7j\2\2\u0366\u0368\7k\2\2\u0367\u035f")
        buf.write("\3\2\2\2\u0367\u0363\3\2\2\2\u0368\u00ba\3\2\2\2\u0369")
        buf.write("\u036a\7^\2\2\u036a\u036b\7e\2\2\u036b\u036c\7j\2\2\u036c")
        buf.write("\u0372\7k\2\2\u036d\u036e\7^\2\2\u036e\u036f\7E\2\2\u036f")
        buf.write("\u0370\7j\2\2\u0370\u0372\7k\2\2\u0371\u0369\3\2\2\2\u0371")
        buf.write("\u036d\3\2\2\2\u0372\u00bc\3\2\2\2\u0373\u0374\7^\2\2")
        buf.write("\u0374\u0375\7r\2\2\u0375\u0376\7u\2\2\u0376\u037c\7k")
        buf.write("\2\2\u0377\u0378\7^\2\2\u0378\u0379\7R\2\2\u0379\u037a")
        buf.write("\7u\2\2\u037a\u037c\7k\2\2\u037b\u0373\3\2\2\2\u037b\u0377")
        buf.write("\3\2\2\2\u037c\u00be\3\2\2\2\u037d\u037e\7^\2\2\u037e")
        buf.write("\u037f\7q\2\2\u037f\u0380\7o\2\2\u0380\u0381\7g\2\2\u0381")
        buf.write("\u0382\7i\2\2\u0382\u038a\7c\2\2\u0383\u0384\7^\2\2\u0384")
        buf.write("\u0385\7Q\2\2\u0385\u0386\7o\2\2\u0386\u0387\7g\2\2\u0387")
        buf.write("\u0388\7i\2\2\u0388\u038a\7c\2\2\u0389\u037d\3\2\2\2\u0389")
        buf.write("\u0383\3\2\2\2\u038a\u00c0\3\2\2\2\u038b\u03a4\5\u0091")
        buf.write("I\2\u038c\u03a4\5\u0093J\2\u038d\u03a4\5\u0095K\2\u038e")
        buf.write("\u03a4\5\u0097L\2\u038f\u03a4\5\u0099M\2\u0390\u03a4\5")
        buf.write("\u009bN\2\u0391\u03a4\5\u009dO\2\u0392\u03a4\5\u009fP")
        buf.write("\2\u0393\u03a4\5\u00a1Q\2\u0394\u03a4\5\u00a3R\2\u0395")
        buf.write("\u03a4\5\u00a5S\2\u0396\u03a4\5\u00a7T\2\u0397\u03a4\5")
        buf.write("\u00a9U\2\u0398\u03a4\5\u00abV\2\u0399\u03a4\5\u00adW")
        buf.write("\2\u039a\u03a4\5\u00afX\2\u039b\u03a4\5\u00b1Y\2\u039c")
        buf.write("\u03a4\5\u00b3Z\2\u039d\u03a4\5\u00b5[\2\u039e\u03a4\5")
        buf.write("\u00b7\\\2\u039f\u03a4\5\u00b9]\2\u03a0\u03a4\5\u00bb")
        buf.write("^\2\u03a1\u03a4\5\u00bd_\2\u03a2\u03a4\5\u00bf`\2\u03a3")
        buf.write("\u038b\3\2\2\2\u03a3\u038c\3\2\2\2\u03a3\u038d\3\2\2\2")
        buf.write("\u03a3\u038e\3\2\2\2\u03a3\u038f\3\2\2\2\u03a3\u0390\3")
        buf.write("\2\2\2\u03a3\u0391\3\2\2\2\u03a3\u0392\3\2\2\2\u03a3\u0393")
        buf.write("\3\2\2\2\u03a3\u0394\3\2\2\2\u03a3\u0395\3\2\2\2\u03a3")
        buf.write("\u0396\3\2\2\2\u03a3\u0397\3\2\2\2\u03a3\u0398\3\2\2\2")
        buf.write("\u03a3\u0399\3\2\2\2\u03a3\u039a\3\2\2\2\u03a3\u039b\3")
        buf.write("\2\2\2\u03a3\u039c\3\2\2\2\u03a3\u039d\3\2\2\2\u03a3\u039e")
        buf.write("\3\2\2\2\u03a3\u039f\3\2\2\2\u03a3\u03a0\3\2\2\2\u03a3")
        buf.write("\u03a1\3\2\2\2\u03a3\u03a2\3\2\2\2\u03a4\u00c2\3\2\2\2")
        buf.write("\u03a5\u03a6\5\35\17\2\u03a6\u03aa\5\17\b\2\u03a7\u03ab")
        buf.write("\5{>\2\u03a8\u03ab\5w<\2\u03a9\u03ab\5\u00c1a\2\u03aa")
        buf.write("\u03a7\3\2\2\2\u03aa\u03a8\3\2\2\2\u03aa\u03a9\3\2\2\2")
        buf.write("\u03ab\u03ac\3\2\2\2\u03ac\u03ad\5\21\t\2\u03ad\u00c4")
        buf.write("\3\2\2\2\u03ae\u03b0\5s:\2\u03af\u03b1\5\u00c3b\2\u03b0")
        buf.write("\u03af\3\2\2\2\u03b0\u03b1\3\2\2\2\u03b1\u03b2\3\2\2\2")
        buf.write("\u03b2\u03b3\5\17\b\2\u03b3\u00c6\3\2\2\2\u03b4\u03b6")
        buf.write("\5s:\2\u03b5\u03b7\5\u00c3b\2\u03b6\u03b5\3\2\2\2\u03b6")
        buf.write("\u03b7\3\2\2\2\u03b7\u03b8\3\2\2\2\u03b8\u03b9\5\13\6")
        buf.write("\2\u03b9\u00c8\3\2\2\2\u03ba\u03bc\5\u00c1a\2\u03bb\u03bd")
        buf.write("\5\u00c3b\2\u03bc\u03bb\3\2\2\2\u03bc\u03bd\3\2\2\2\u03bd")
        buf.write("\u03be\3\2\2\2\u03be\u03bf\5\17\b\2\u03bf\u00ca\3\2\2")
        buf.write("\2\u03c0\u03c2\5\u00c1a\2\u03c1\u03c3\5\u00c3b\2\u03c2")
        buf.write("\u03c1\3\2\2\2\u03c2\u03c3\3\2\2\2\u03c3\u03c4\3\2\2\2")
        buf.write("\u03c4\u03c5\5\13\6\2\u03c5\u00cc\3\2\2\2\u03c6\u03c8")
        buf.write("\t\6\2\2\u03c7\u03c6\3\2\2\2\u03c8\u03c9\3\2\2\2\u03c9")
        buf.write("\u03c7\3\2\2\2\u03c9\u03ca\3\2\2\2\u03ca\u03cb\3\2\2\2")
        buf.write("\u03cb\u03cc\bg\2\2\u03cc\u00ce\3\2\2\2H\2\u012d\u0146")
        buf.write("\u014d\u0153\u015a\u0161\u0168\u016f\u0176\u017d\u0183")
        buf.write("\u0189\u018f\u0195\u019b\u01a1\u01a9\u01b1\u01b9\u01bf")
        buf.write("\u01c5\u01cb\u01d1\u01d7\u01dd\u01e3\u01e9\u01ef\u01f7")
        buf.write("\u021e\u0222\u0227\u022b\u0230\u0232\u023d\u0242\u025f")
        buf.write("\u026f\u027b\u0289\u0297\u02a9\u02b5\u02bf\u02cd\u02d9")
        buf.write("\u02e7\u02f7\u02ff\u0307\u030f\u0321\u0329\u0333\u0341")
        buf.write("\u034b\u035d\u0367\u0371\u037b\u0389\u03a3\u03aa\u03b0")
        buf.write("\u03b6\u03bc\u03c2\u03c9\3\b\2\2")
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
    FUNC_FRAC = 19
    FUNC_INT = 20
    FUNC_SUM = 21
    FUNC_PROD = 22
    FUNC_LOG = 23
    FUNC_LN = 24
    FUNC_SIN = 25
    FUNC_COS = 26
    FUNC_TAN = 27
    FUNC_CSC = 28
    FUNC_SEC = 29
    FUNC_COT = 30
    FUNC_ARCSIN = 31
    FUNC_ARCCOS = 32
    FUNC_ARCTAN = 33
    FUNC_ARCCSC = 34
    FUNC_ARCSEC = 35
    FUNC_ARCCOT = 36
    FUNC_SINH = 37
    FUNC_COSH = 38
    FUNC_TANH = 39
    FUNC_ARCSINH = 40
    FUNC_ARCCOSH = 41
    FUNC_ARCTANH = 42
    FUNC_ECOS = 43
    FUNC_ESIN = 44
    FUNC_EDELTAAMPLITUDE = 45
    FUNC_ARCECOS = 46
    FUNC_ARCESIN = 47
    FUNC_ARCEDELTAAMPLITUDE = 48
    FUNC_SQRT = 49
    FUNC_BINOMIAL = 50
    CMD_TIMES = 51
    CMD_CDOT = 52
    CMD_DIV = 53
    CMD_FRAC = 54
    NUMBER = 55
    DERIVATIVE = 56
    VARIABLE = 57
    MIXNUMBER = 58
    WORD = 59
    INFINITY = 60
    EQ = 61
    INEQUALITIES = 62
    BANG = 63
    GREEKLETTER = 64
    LETTERFUNCTIONBRACE = 65
    LETTERFUNCTIONPAREN = 66
    GREEKFUNCTIONBRACE = 67
    GREEKFUNCTIONPAREN = 68
    WS = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "'.'", "'|'", "'_'", "'^'", "':'", "'\\lim'", 
            "'K'", "'\\int'", "'\\sum'", "'\\prod'", "'\\times'", "'\\cdot'", 
            "'\\div'", "'\\frac'", "'\\infty'", "'='", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MUL", "DIV", "L_PAREN", "R_PAREN", "L_BRACE", 
            "R_BRACE", "L_BRACKET", "R_BRACKET", "COMMA", "DOT", "BAR", 
            "UNDERSCORE", "CARET", "COLON", "FUNC_LIM", "LIM_APPROACH_SYM", 
            "FUNC_FRAC", "FUNC_INT", "FUNC_SUM", "FUNC_PROD", "FUNC_LOG", 
            "FUNC_LN", "FUNC_SIN", "FUNC_COS", "FUNC_TAN", "FUNC_CSC", "FUNC_SEC", 
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
                  "LIM_APPROACH_SYM", "FUNC_FRAC", "FUNC_INT", "FUNC_SUM", 
                  "FUNC_PROD", "ARC", "FUNC_LOG", "FUNC_LN", "FUNC_SIN", 
                  "FUNC_COS", "FUNC_TAN", "FUNC_CSC", "FUNC_SEC", "FUNC_COT", 
                  "FUNC_ARCSIN", "FUNC_ARCCOS", "FUNC_ARCTAN", "FUNC_ARCCSC", 
                  "FUNC_ARCSEC", "FUNC_ARCCOT", "FUNC_SINH", "FUNC_COSH", 
                  "FUNC_TANH", "FUNC_ARCSINH", "FUNC_ARCCOSH", "FUNC_ARCTANH", 
                  "FUNC_ECOS", "FUNC_ESIN", "FUNC_EDELTAAMPLITUDE", "FUNC_ARCECOS", 
                  "FUNC_ARCESIN", "FUNC_ARCEDELTAAMPLITUDE", "FUNC_SQRT", 
                  "FUNC_BINOMIAL", "CMD_TIMES", "CMD_CDOT", "CMD_DIV", "CMD_FRAC", 
                  "LETTER", "DIGIT", "NUMBER", "DERIVATIVE", "VARIABLE", 
                  "MIXNUMBER", "WORD", "INFINITY", "EQ", "LT", "LTE", "GT", 
                  "GTE", "INEQUALITIES", "BANG", "ALPHA", "BETA", "GAMMA", 
                  "DELTA", "EPSILON", "ZETA", "ETA", "THETA", "IOTA", "KAPPA", 
                  "LAMBDA", "MU", "NU", "XI", "OMICRON", "PI", "RHO", "SIGMA", 
                  "TAU", "UPSILON", "PHI", "CHI", "PSI", "OMEGA", "GREEKLETTER", 
                  "INDICED", "LETTERFUNCTIONBRACE", "LETTERFUNCTIONPAREN", 
                  "GREEKFUNCTIONBRACE", "GREEKFUNCTIONPAREN", "WS" ]

    grammarFileName = "MatexLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


