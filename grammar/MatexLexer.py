# Generated from .\grammar\MatexLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u0374\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r")
        buf.write("\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0106\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\5\24\u0119\n\24\3")
        buf.write("\24\3\24\3\24\3\24\3\25\5\25\u0120\n\25\3\25\3\25\3\25")
        buf.write("\3\26\5\26\u0126\n\26\3\26\3\26\3\26\3\26\3\27\5\27\u012d")
        buf.write("\n\27\3\27\3\27\3\27\3\27\3\30\5\30\u0134\n\30\3\30\3")
        buf.write("\30\3\30\3\30\3\31\5\31\u013b\n\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\5\32\u0142\n\32\3\32\3\32\3\32\3\32\3\33\5\33\u0149")
        buf.write("\n\33\3\33\3\33\3\33\3\33\3\34\5\34\u0150\n\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\35\5\35\u015a\n\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\5\36\u0164\n\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\5\37\u016e\n\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \5 \u0178\n \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\5!\u0182\n!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3\"\5\"\u018c\n\"\3\"\3\"\3\"\3\"\3\"\3#\5#\u0194\n")
        buf.write("#\3#\3#\3#\3#\3#\3$\5$\u019c\n$\3$\3$\3$\3$\3$\3%\5%\u01a4")
        buf.write("\n%\3%\3%\3%\3%\3%\3%\3%\3&\5&\u01ae\n&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\5\'\u01b8\n\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3(\5(\u01c2\n(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\7\63")
        buf.write("\u01ee\n\63\f\63\16\63\u01f1\13\63\3\63\5\63\u01f4\n\63")
        buf.write("\3\63\6\63\u01f7\n\63\r\63\16\63\u01f8\3\63\3\63\5\63")
        buf.write("\u01fd\n\63\3\63\6\63\u0200\n\63\r\63\16\63\u0201\5\63")
        buf.write("\u0204\n\63\3\64\3\64\3\64\3\65\3\65\3\66\5\66\u020c\n")
        buf.write("\66\3\66\6\66\u020f\n\66\r\66\16\66\u0210\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\38\38\39\39\3:\3:\3:\3:\3:\3;")
        buf.write("\3;\3<\3<\3<\3<\3<\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\5>\u0238\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u0244")
        buf.write("\n?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u0252\n@\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u0260\nA\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\5B\u0272\nB\3")
        buf.write("C\3C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u027e\nC\3D\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\5D\u0288\nD\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\5E\u0296\nE\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u02a2")
        buf.write("\nF\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u02b0\nG\3")
        buf.write("H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\5H\u02c0\nH\3")
        buf.write("I\3I\3I\3I\3I\3I\5I\u02c8\nI\3J\3J\3J\3J\3J\3J\5J\u02d0")
        buf.write("\nJ\3K\3K\3K\3K\3K\3K\5K\u02d8\nK\3L\3L\3L\3L\3L\3L\3")
        buf.write("L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u02ea\nL\3M\3M\3M\3M\3")
        buf.write("M\3M\5M\u02f2\nM\3N\3N\3N\3N\3N\3N\3N\3N\5N\u02fc\nN\3")
        buf.write("O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u030a\nO\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\5P\u0314\nP\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3")
        buf.write("Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u0326\nQ\3R\3R\3R\3R\3R\3R\3")
        buf.write("R\3R\5R\u0330\nR\3S\3S\3S\3S\3S\3S\3S\3S\5S\u033a\nS\3")
        buf.write("T\3T\3T\3T\3T\3T\3T\3T\5T\u0344\nT\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\5U\u0352\nU\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u036c")
        buf.write("\nV\3W\6W\u036f\nW\rW\16W\u0370\3W\3W\2\2X\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\2c\2e\62g\63i\64k\65m\66o\67q8s9u:w;y<{\2}")
        buf.write("\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b")
        buf.write("\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099")
        buf.write("\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9\2\u00ab=\u00ad>\3\2\7\4\2C\\c|\3\2\62;\4\2GG")
        buf.write("gg\4\2--//\5\2\13\f\17\17\"\"\2\u03aa\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\3\u00af")
        buf.write("\3\2\2\2\5\u00b1\3\2\2\2\7\u00b3\3\2\2\2\t\u00b5\3\2\2")
        buf.write("\2\13\u00b7\3\2\2\2\r\u00b9\3\2\2\2\17\u00bb\3\2\2\2\21")
        buf.write("\u00bd\3\2\2\2\23\u00bf\3\2\2\2\25\u00c1\3\2\2\2\27\u00c3")
        buf.write("\3\2\2\2\31\u00c5\3\2\2\2\33\u00c7\3\2\2\2\35\u00c9\3")
        buf.write("\2\2\2\37\u0105\3\2\2\2!\u0107\3\2\2\2#\u010c\3\2\2\2")
        buf.write("%\u0111\3\2\2\2\'\u0118\3\2\2\2)\u011f\3\2\2\2+\u0125")
        buf.write("\3\2\2\2-\u012c\3\2\2\2/\u0133\3\2\2\2\61\u013a\3\2\2")
        buf.write("\2\63\u0141\3\2\2\2\65\u0148\3\2\2\2\67\u014f\3\2\2\2")
        buf.write("9\u0159\3\2\2\2;\u0163\3\2\2\2=\u016d\3\2\2\2?\u0177\3")
        buf.write("\2\2\2A\u0181\3\2\2\2C\u018b\3\2\2\2E\u0193\3\2\2\2G\u019b")
        buf.write("\3\2\2\2I\u01a3\3\2\2\2K\u01ad\3\2\2\2M\u01b7\3\2\2\2")
        buf.write("O\u01c1\3\2\2\2Q\u01c8\3\2\2\2S\u01cf\3\2\2\2U\u01d5\3")
        buf.write("\2\2\2W\u01da\3\2\2\2Y\u01e0\3\2\2\2[\u01e2\3\2\2\2]\u01e4")
        buf.write("\3\2\2\2_\u01e6\3\2\2\2a\u01e8\3\2\2\2c\u01ea\3\2\2\2")
        buf.write("e\u01ef\3\2\2\2g\u0205\3\2\2\2i\u0208\3\2\2\2k\u020b\3")
        buf.write("\2\2\2m\u0212\3\2\2\2o\u0219\3\2\2\2q\u021b\3\2\2\2s\u021d")
        buf.write("\3\2\2\2u\u0222\3\2\2\2w\u0224\3\2\2\2y\u0229\3\2\2\2")
        buf.write("{\u0237\3\2\2\2}\u0243\3\2\2\2\177\u0251\3\2\2\2\u0081")
        buf.write("\u025f\3\2\2\2\u0083\u0271\3\2\2\2\u0085\u027d\3\2\2\2")
        buf.write("\u0087\u0287\3\2\2\2\u0089\u0295\3\2\2\2\u008b\u02a1\3")
        buf.write("\2\2\2\u008d\u02af\3\2\2\2\u008f\u02bf\3\2\2\2\u0091\u02c7")
        buf.write("\3\2\2\2\u0093\u02cf\3\2\2\2\u0095\u02d7\3\2\2\2\u0097")
        buf.write("\u02e9\3\2\2\2\u0099\u02f1\3\2\2\2\u009b\u02fb\3\2\2\2")
        buf.write("\u009d\u0309\3\2\2\2\u009f\u0313\3\2\2\2\u00a1\u0325\3")
        buf.write("\2\2\2\u00a3\u032f\3\2\2\2\u00a5\u0339\3\2\2\2\u00a7\u0343")
        buf.write("\3\2\2\2\u00a9\u0351\3\2\2\2\u00ab\u036b\3\2\2\2\u00ad")
        buf.write("\u036e\3\2\2\2\u00af\u00b0\7-\2\2\u00b0\4\3\2\2\2\u00b1")
        buf.write("\u00b2\7/\2\2\u00b2\6\3\2\2\2\u00b3\u00b4\7,\2\2\u00b4")
        buf.write("\b\3\2\2\2\u00b5\u00b6\7\61\2\2\u00b6\n\3\2\2\2\u00b7")
        buf.write("\u00b8\7*\2\2\u00b8\f\3\2\2\2\u00b9\u00ba\7+\2\2\u00ba")
        buf.write("\16\3\2\2\2\u00bb\u00bc\7}\2\2\u00bc\20\3\2\2\2\u00bd")
        buf.write("\u00be\7\177\2\2\u00be\22\3\2\2\2\u00bf\u00c0\7]\2\2\u00c0")
        buf.write("\24\3\2\2\2\u00c1\u00c2\7_\2\2\u00c2\26\3\2\2\2\u00c3")
        buf.write("\u00c4\7.\2\2\u00c4\30\3\2\2\2\u00c5\u00c6\7\60\2\2\u00c6")
        buf.write("\32\3\2\2\2\u00c7\u00c8\7~\2\2\u00c8\34\3\2\2\2\u00c9")
        buf.write("\u00ca\7^\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7k\2\2\u00cc")
        buf.write("\u00cd\7o\2\2\u00cd\36\3\2\2\2\u00ce\u00cf\7^\2\2\u00cf")
        buf.write("\u00d0\7v\2\2\u00d0\u0106\7q\2\2\u00d1\u00d2\7^\2\2\u00d2")
        buf.write("\u00d3\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7i\2\2\u00d5")
        buf.write("\u00d6\7j\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7c\2\2\u00d8")
        buf.write("\u00d9\7t\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7q\2\2\u00db")
        buf.write("\u0106\7y\2\2\u00dc\u00dd\7^\2\2\u00dd\u00de\7T\2\2\u00de")
        buf.write("\u00df\7k\2\2\u00df\u00e0\7i\2\2\u00e0\u00e1\7j\2\2\u00e1")
        buf.write("\u00e2\7v\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7t\2\2\u00e4")
        buf.write("\u00e5\7t\2\2\u00e5\u00e6\7q\2\2\u00e6\u0106\7y\2\2\u00e7")
        buf.write("\u00e8\7^\2\2\u00e8\u00e9\7n\2\2\u00e9\u00ea\7q\2\2\u00ea")
        buf.write("\u00eb\7p\2\2\u00eb\u00ec\7i\2\2\u00ec\u00ed\7t\2\2\u00ed")
        buf.write("\u00ee\7k\2\2\u00ee\u00ef\7i\2\2\u00ef\u00f0\7j\2\2\u00f0")
        buf.write("\u00f1\7v\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7t\2\2\u00f3")
        buf.write("\u00f4\7t\2\2\u00f4\u00f5\7q\2\2\u00f5\u0106\7y\2\2\u00f6")
        buf.write("\u00f7\7^\2\2\u00f7\u00f8\7N\2\2\u00f8\u00f9\7q\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\u00fb\7i\2\2\u00fb\u00fc\7t\2\2\u00fc")
        buf.write("\u00fd\7k\2\2\u00fd\u00fe\7i\2\2\u00fe\u00ff\7j\2\2\u00ff")
        buf.write("\u0100\7v\2\2\u0100\u0101\7c\2\2\u0101\u0102\7t\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103\u0104\7q\2\2\u0104\u0106\7y\2\2\u0105")
        buf.write("\u00ce\3\2\2\2\u0105\u00d1\3\2\2\2\u0105\u00dc\3\2\2\2")
        buf.write("\u0105\u00e7\3\2\2\2\u0105\u00f6\3\2\2\2\u0106 \3\2\2")
        buf.write("\2\u0107\u0108\7^\2\2\u0108\u0109\7k\2\2\u0109\u010a\7")
        buf.write("p\2\2\u010a\u010b\7v\2\2\u010b\"\3\2\2\2\u010c\u010d\7")
        buf.write("^\2\2\u010d\u010e\7u\2\2\u010e\u010f\7w\2\2\u010f\u0110")
        buf.write("\7o\2\2\u0110$\3\2\2\2\u0111\u0112\7^\2\2\u0112\u0113")
        buf.write("\7r\2\2\u0113\u0114\7t\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7f\2\2\u0116&\3\2\2\2\u0117\u0119\5_\60\2\u0118\u0117")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u011b\7n\2\2\u011b\u011c\7q\2\2\u011c\u011d\7i\2\2\u011d")
        buf.write("(\3\2\2\2\u011e\u0120\5_\60\2\u011f\u011e\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\7n\2\2")
        buf.write("\u0122\u0123\7p\2\2\u0123*\3\2\2\2\u0124\u0126\5_\60\2")
        buf.write("\u0125\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3")
        buf.write("\2\2\2\u0127\u0128\7u\2\2\u0128\u0129\7k\2\2\u0129\u012a")
        buf.write("\7p\2\2\u012a,\3\2\2\2\u012b\u012d\5_\60\2\u012c\u012b")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u012f\7e\2\2\u012f\u0130\7q\2\2\u0130\u0131\7u\2\2\u0131")
        buf.write(".\3\2\2\2\u0132\u0134\5_\60\2\u0133\u0132\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\7v\2\2")
        buf.write("\u0136\u0137\7c\2\2\u0137\u0138\7p\2\2\u0138\60\3\2\2")
        buf.write("\2\u0139\u013b\5_\60\2\u013a\u0139\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\7e\2\2\u013d")
        buf.write("\u013e\7u\2\2\u013e\u013f\7e\2\2\u013f\62\3\2\2\2\u0140")
        buf.write("\u0142\5_\60\2\u0141\u0140\3\2\2\2\u0141\u0142\3\2\2\2")
        buf.write("\u0142\u0143\3\2\2\2\u0143\u0144\7u\2\2\u0144\u0145\7")
        buf.write("g\2\2\u0145\u0146\7e\2\2\u0146\64\3\2\2\2\u0147\u0149")
        buf.write("\5_\60\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014a\u014b\7e\2\2\u014b\u014c\7q\2\2\u014c")
        buf.write("\u014d\7v\2\2\u014d\66\3\2\2\2\u014e\u0150\5_\60\2\u014f")
        buf.write("\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\u0152\7c\2\2\u0152\u0153\7t\2\2\u0153\u0154\7e")
        buf.write("\2\2\u0154\u0155\7u\2\2\u0155\u0156\7k\2\2\u0156\u0157")
        buf.write("\7p\2\2\u01578\3\2\2\2\u0158\u015a\5_\60\2\u0159\u0158")
        buf.write("\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write("\u015c\7c\2\2\u015c\u015d\7t\2\2\u015d\u015e\7e\2\2\u015e")
        buf.write("\u015f\7e\2\2\u015f\u0160\7q\2\2\u0160\u0161\7u\2\2\u0161")
        buf.write(":\3\2\2\2\u0162\u0164\5_\60\2\u0163\u0162\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\7c\2\2")
        buf.write("\u0166\u0167\7t\2\2\u0167\u0168\7e\2\2\u0168\u0169\7v")
        buf.write("\2\2\u0169\u016a\7c\2\2\u016a\u016b\7p\2\2\u016b<\3\2")
        buf.write("\2\2\u016c\u016e\5_\60\2\u016d\u016c\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\7c\2\2\u0170")
        buf.write("\u0171\7t\2\2\u0171\u0172\7e\2\2\u0172\u0173\7e\2\2\u0173")
        buf.write("\u0174\7u\2\2\u0174\u0175\7e\2\2\u0175>\3\2\2\2\u0176")
        buf.write("\u0178\5_\60\2\u0177\u0176\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017a\7c\2\2\u017a\u017b\7")
        buf.write("t\2\2\u017b\u017c\7e\2\2\u017c\u017d\7u\2\2\u017d\u017e")
        buf.write("\7g\2\2\u017e\u017f\7e\2\2\u017f@\3\2\2\2\u0180\u0182")
        buf.write("\5_\60\2\u0181\u0180\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0184\7c\2\2\u0184\u0185\7t\2\2\u0185")
        buf.write("\u0186\7e\2\2\u0186\u0187\7e\2\2\u0187\u0188\7q\2\2\u0188")
        buf.write("\u0189\7v\2\2\u0189B\3\2\2\2\u018a\u018c\5_\60\2\u018b")
        buf.write("\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\3\2\2\2")
        buf.write("\u018d\u018e\7u\2\2\u018e\u018f\7k\2\2\u018f\u0190\7p")
        buf.write("\2\2\u0190\u0191\7j\2\2\u0191D\3\2\2\2\u0192\u0194\5_")
        buf.write("\60\2\u0193\u0192\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0196\7e\2\2\u0196\u0197\7q\2\2\u0197\u0198")
        buf.write("\7u\2\2\u0198\u0199\7j\2\2\u0199F\3\2\2\2\u019a\u019c")
        buf.write("\5_\60\2\u019b\u019a\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d\u019e\7v\2\2\u019e\u019f\7c\2\2\u019f")
        buf.write("\u01a0\7p\2\2\u01a0\u01a1\7j\2\2\u01a1H\3\2\2\2\u01a2")
        buf.write("\u01a4\5_\60\2\u01a3\u01a2\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a6\7c\2\2\u01a6\u01a7\7")
        buf.write("t\2\2\u01a7\u01a8\7u\2\2\u01a8\u01a9\7k\2\2\u01a9\u01aa")
        buf.write("\7p\2\2\u01aa\u01ab\7j\2\2\u01abJ\3\2\2\2\u01ac\u01ae")
        buf.write("\5_\60\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b0\7c\2\2\u01b0\u01b1\7t\2\2\u01b1")
        buf.write("\u01b2\7e\2\2\u01b2\u01b3\7q\2\2\u01b3\u01b4\7u\2\2\u01b4")
        buf.write("\u01b5\7j\2\2\u01b5L\3\2\2\2\u01b6\u01b8\5_\60\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\3\2\2\2")
        buf.write("\u01b9\u01ba\7c\2\2\u01ba\u01bb\7t\2\2\u01bb\u01bc\7v")
        buf.write("\2\2\u01bc\u01bd\7c\2\2\u01bd\u01be\7p\2\2\u01be\u01bf")
        buf.write("\7j\2\2\u01bfN\3\2\2\2\u01c0\u01c2\5_\60\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("\u01c4\7u\2\2\u01c4\u01c5\7s\2\2\u01c5\u01c6\7t\2\2\u01c6")
        buf.write("\u01c7\7v\2\2\u01c7P\3\2\2\2\u01c8\u01c9\7^\2\2\u01c9")
        buf.write("\u01ca\7v\2\2\u01ca\u01cb\7k\2\2\u01cb\u01cc\7o\2\2\u01cc")
        buf.write("\u01cd\7g\2\2\u01cd\u01ce\7u\2\2\u01ceR\3\2\2\2\u01cf")
        buf.write("\u01d0\7^\2\2\u01d0\u01d1\7e\2\2\u01d1\u01d2\7f\2\2\u01d2")
        buf.write("\u01d3\7q\2\2\u01d3\u01d4\7v\2\2\u01d4T\3\2\2\2\u01d5")
        buf.write("\u01d6\7^\2\2\u01d6\u01d7\7f\2\2\u01d7\u01d8\7k\2\2\u01d8")
        buf.write("\u01d9\7x\2\2\u01d9V\3\2\2\2\u01da\u01db\7^\2\2\u01db")
        buf.write("\u01dc\7h\2\2\u01dc\u01dd\7t\2\2\u01dd\u01de\7c\2\2\u01de")
        buf.write("\u01df\7e\2\2\u01dfX\3\2\2\2\u01e0\u01e1\7a\2\2\u01e1")
        buf.write("Z\3\2\2\2\u01e2\u01e3\7`\2\2\u01e3\\\3\2\2\2\u01e4\u01e5")
        buf.write("\7<\2\2\u01e5^\3\2\2\2\u01e6\u01e7\7^\2\2\u01e7`\3\2\2")
        buf.write("\2\u01e8\u01e9\t\2\2\2\u01e9b\3\2\2\2\u01ea\u01eb\t\3")
        buf.write("\2\2\u01ebd\3\2\2\2\u01ec\u01ee\5c\62\2\u01ed\u01ec\3")
        buf.write("\2\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0")
        buf.write("\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2")
        buf.write("\u01f4\7\60\2\2\u01f3\u01f2\3\2\2\2\u01f3\u01f4\3\2\2")
        buf.write("\2\u01f4\u01f6\3\2\2\2\u01f5\u01f7\5c\62\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f9\u0203\3\2\2\2\u01fa\u01fc\t\4\2\2")
        buf.write("\u01fb\u01fd\t\5\2\2\u01fc\u01fb\3\2\2\2\u01fc\u01fd\3")
        buf.write("\2\2\2\u01fd\u01ff\3\2\2\2\u01fe\u0200\5c\62\2\u01ff\u01fe")
        buf.write("\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u01ff\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0204\3\2\2\2\u0203\u01fa\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204f\3\2\2\2\u0205\u0206\7f\2\2")
        buf.write("\u0206\u0207\5a\61\2\u0207h\3\2\2\2\u0208\u0209\5a\61")
        buf.write("\2\u0209j\3\2\2\2\u020a\u020c\5e\63\2\u020b\u020a\3\2")
        buf.write("\2\2\u020b\u020c\3\2\2\2\u020c\u020e\3\2\2\2\u020d\u020f")
        buf.write("\5i\65\2\u020e\u020d\3\2\2\2\u020f\u0210\3\2\2\2\u0210")
        buf.write("\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211l\3\2\2\2\u0212")
        buf.write("\u0213\7^\2\2\u0213\u0214\7k\2\2\u0214\u0215\7p\2\2\u0215")
        buf.write("\u0216\7h\2\2\u0216\u0217\7v\2\2\u0217\u0218\7{\2\2\u0218")
        buf.write("n\3\2\2\2\u0219\u021a\7?\2\2\u021ap\3\2\2\2\u021b\u021c")
        buf.write("\7>\2\2\u021cr\3\2\2\2\u021d\u021e\7^\2\2\u021e\u021f")
        buf.write("\7n\2\2\u021f\u0220\7g\2\2\u0220\u0221\7s\2\2\u0221t\3")
        buf.write("\2\2\2\u0222\u0223\7@\2\2\u0223v\3\2\2\2\u0224\u0225\7")
        buf.write("^\2\2\u0225\u0226\7i\2\2\u0226\u0227\7g\2\2\u0227\u0228")
        buf.write("\7s\2\2\u0228x\3\2\2\2\u0229\u022a\7#\2\2\u022az\3\2\2")
        buf.write("\2\u022b\u022c\7^\2\2\u022c\u022d\7c\2\2\u022d\u022e\7")
        buf.write("n\2\2\u022e\u022f\7r\2\2\u022f\u0230\7j\2\2\u0230\u0238")
        buf.write("\7c\2\2\u0231\u0232\7^\2\2\u0232\u0233\7C\2\2\u0233\u0234")
        buf.write("\7n\2\2\u0234\u0235\7r\2\2\u0235\u0236\7j\2\2\u0236\u0238")
        buf.write("\7c\2\2\u0237\u022b\3\2\2\2\u0237\u0231\3\2\2\2\u0238")
        buf.write("|\3\2\2\2\u0239\u023a\7^\2\2\u023a\u023b\7d\2\2\u023b")
        buf.write("\u023c\7g\2\2\u023c\u023d\7v\2\2\u023d\u0244\7c\2\2\u023e")
        buf.write("\u023f\7^\2\2\u023f\u0240\7D\2\2\u0240\u0241\7g\2\2\u0241")
        buf.write("\u0242\7v\2\2\u0242\u0244\7c\2\2\u0243\u0239\3\2\2\2\u0243")
        buf.write("\u023e\3\2\2\2\u0244~\3\2\2\2\u0245\u0246\7^\2\2\u0246")
        buf.write("\u0247\7i\2\2\u0247\u0248\7c\2\2\u0248\u0249\7o\2\2\u0249")
        buf.write("\u024a\7o\2\2\u024a\u0252\7c\2\2\u024b\u024c\7^\2\2\u024c")
        buf.write("\u024d\7I\2\2\u024d\u024e\7c\2\2\u024e\u024f\7o\2\2\u024f")
        buf.write("\u0250\7o\2\2\u0250\u0252\7c\2\2\u0251\u0245\3\2\2\2\u0251")
        buf.write("\u024b\3\2\2\2\u0252\u0080\3\2\2\2\u0253\u0254\7^\2\2")
        buf.write("\u0254\u0255\7f\2\2\u0255\u0256\7g\2\2\u0256\u0257\7n")
        buf.write("\2\2\u0257\u0258\7v\2\2\u0258\u0260\7c\2\2\u0259\u025a")
        buf.write("\7^\2\2\u025a\u025b\7F\2\2\u025b\u025c\7g\2\2\u025c\u025d")
        buf.write("\7n\2\2\u025d\u025e\7v\2\2\u025e\u0260\7c\2\2\u025f\u0253")
        buf.write("\3\2\2\2\u025f\u0259\3\2\2\2\u0260\u0082\3\2\2\2\u0261")
        buf.write("\u0262\7^\2\2\u0262\u0263\7g\2\2\u0263\u0264\7r\2\2\u0264")
        buf.write("\u0265\7u\2\2\u0265\u0266\7k\2\2\u0266\u0267\7n\2\2\u0267")
        buf.write("\u0268\7q\2\2\u0268\u0272\7p\2\2\u0269\u026a\7^\2\2\u026a")
        buf.write("\u026b\7G\2\2\u026b\u026c\7r\2\2\u026c\u026d\7u\2\2\u026d")
        buf.write("\u026e\7k\2\2\u026e\u026f\7n\2\2\u026f\u0270\7q\2\2\u0270")
        buf.write("\u0272\7p\2\2\u0271\u0261\3\2\2\2\u0271\u0269\3\2\2\2")
        buf.write("\u0272\u0084\3\2\2\2\u0273\u0274\7^\2\2\u0274\u0275\7")
        buf.write("|\2\2\u0275\u0276\7g\2\2\u0276\u0277\7v\2\2\u0277\u027e")
        buf.write("\7c\2\2\u0278\u0279\7^\2\2\u0279\u027a\7\\\2\2\u027a\u027b")
        buf.write("\7g\2\2\u027b\u027c\7v\2\2\u027c\u027e\7c\2\2\u027d\u0273")
        buf.write("\3\2\2\2\u027d\u0278\3\2\2\2\u027e\u0086\3\2\2\2\u027f")
        buf.write("\u0280\7^\2\2\u0280\u0281\7g\2\2\u0281\u0282\7v\2\2\u0282")
        buf.write("\u0288\7c\2\2\u0283\u0284\7^\2\2\u0284\u0285\7G\2\2\u0285")
        buf.write("\u0286\7v\2\2\u0286\u0288\7c\2\2\u0287\u027f\3\2\2\2\u0287")
        buf.write("\u0283\3\2\2\2\u0288\u0088\3\2\2\2\u0289\u028a\7^\2\2")
        buf.write("\u028a\u028b\7v\2\2\u028b\u028c\7j\2\2\u028c\u028d\7g")
        buf.write("\2\2\u028d\u028e\7v\2\2\u028e\u0296\7c\2\2\u028f\u0290")
        buf.write("\7^\2\2\u0290\u0291\7V\2\2\u0291\u0292\7j\2\2\u0292\u0293")
        buf.write("\7g\2\2\u0293\u0294\7v\2\2\u0294\u0296\7c\2\2\u0295\u0289")
        buf.write("\3\2\2\2\u0295\u028f\3\2\2\2\u0296\u008a\3\2\2\2\u0297")
        buf.write("\u0298\7^\2\2\u0298\u0299\7k\2\2\u0299\u029a\7q\2\2\u029a")
        buf.write("\u029b\7v\2\2\u029b\u02a2\7c\2\2\u029c\u029d\7^\2\2\u029d")
        buf.write("\u029e\7K\2\2\u029e\u029f\7q\2\2\u029f\u02a0\7v\2\2\u02a0")
        buf.write("\u02a2\7c\2\2\u02a1\u0297\3\2\2\2\u02a1\u029c\3\2\2\2")
        buf.write("\u02a2\u008c\3\2\2\2\u02a3\u02a4\7^\2\2\u02a4\u02a5\7")
        buf.write("m\2\2\u02a5\u02a6\7c\2\2\u02a6\u02a7\7r\2\2\u02a7\u02a8")
        buf.write("\7r\2\2\u02a8\u02b0\7c\2\2\u02a9\u02aa\7^\2\2\u02aa\u02ab")
        buf.write("\7M\2\2\u02ab\u02ac\7c\2\2\u02ac\u02ad\7r\2\2\u02ad\u02ae")
        buf.write("\7r\2\2\u02ae\u02b0\7c\2\2\u02af\u02a3\3\2\2\2\u02af\u02a9")
        buf.write("\3\2\2\2\u02b0\u008e\3\2\2\2\u02b1\u02b2\7^\2\2\u02b2")
        buf.write("\u02b3\7n\2\2\u02b3\u02b4\7c\2\2\u02b4\u02b5\7o\2\2\u02b5")
        buf.write("\u02b6\7d\2\2\u02b6\u02b7\7f\2\2\u02b7\u02c0\7c\2\2\u02b8")
        buf.write("\u02b9\7^\2\2\u02b9\u02ba\7N\2\2\u02ba\u02bb\7c\2\2\u02bb")
        buf.write("\u02bc\7o\2\2\u02bc\u02bd\7d\2\2\u02bd\u02be\7f\2\2\u02be")
        buf.write("\u02c0\7c\2\2\u02bf\u02b1\3\2\2\2\u02bf\u02b8\3\2\2\2")
        buf.write("\u02c0\u0090\3\2\2\2\u02c1\u02c2\7^\2\2\u02c2\u02c3\7")
        buf.write("o\2\2\u02c3\u02c8\7w\2\2\u02c4\u02c5\7^\2\2\u02c5\u02c6")
        buf.write("\7O\2\2\u02c6\u02c8\7w\2\2\u02c7\u02c1\3\2\2\2\u02c7\u02c4")
        buf.write("\3\2\2\2\u02c8\u0092\3\2\2\2\u02c9\u02ca\7^\2\2\u02ca")
        buf.write("\u02cb\7p\2\2\u02cb\u02d0\7w\2\2\u02cc\u02cd\7^\2\2\u02cd")
        buf.write("\u02ce\7P\2\2\u02ce\u02d0\7w\2\2\u02cf\u02c9\3\2\2\2\u02cf")
        buf.write("\u02cc\3\2\2\2\u02d0\u0094\3\2\2\2\u02d1\u02d2\7^\2\2")
        buf.write("\u02d2\u02d3\7z\2\2\u02d3\u02d8\7k\2\2\u02d4\u02d5\7^")
        buf.write("\2\2\u02d5\u02d6\7Z\2\2\u02d6\u02d8\7k\2\2\u02d7\u02d1")
        buf.write("\3\2\2\2\u02d7\u02d4\3\2\2\2\u02d8\u0096\3\2\2\2\u02d9")
        buf.write("\u02da\7^\2\2\u02da\u02db\7q\2\2\u02db\u02dc\7o\2\2\u02dc")
        buf.write("\u02dd\7k\2\2\u02dd\u02de\7e\2\2\u02de\u02df\7t\2\2\u02df")
        buf.write("\u02e0\7q\2\2\u02e0\u02ea\7p\2\2\u02e1\u02e2\7^\2\2\u02e2")
        buf.write("\u02e3\7Q\2\2\u02e3\u02e4\7o\2\2\u02e4\u02e5\7k\2\2\u02e5")
        buf.write("\u02e6\7e\2\2\u02e6\u02e7\7t\2\2\u02e7\u02e8\7q\2\2\u02e8")
        buf.write("\u02ea\7p\2\2\u02e9\u02d9\3\2\2\2\u02e9\u02e1\3\2\2\2")
        buf.write("\u02ea\u0098\3\2\2\2\u02eb\u02ec\7^\2\2\u02ec\u02ed\7")
        buf.write("r\2\2\u02ed\u02f2\7k\2\2\u02ee\u02ef\7^\2\2\u02ef\u02f0")
        buf.write("\7R\2\2\u02f0\u02f2\7k\2\2\u02f1\u02eb\3\2\2\2\u02f1\u02ee")
        buf.write("\3\2\2\2\u02f2\u009a\3\2\2\2\u02f3\u02f4\7^\2\2\u02f4")
        buf.write("\u02f5\7t\2\2\u02f5\u02f6\7j\2\2\u02f6\u02fc\7q\2\2\u02f7")
        buf.write("\u02f8\7^\2\2\u02f8\u02f9\7T\2\2\u02f9\u02fa\7j\2\2\u02fa")
        buf.write("\u02fc\7q\2\2\u02fb\u02f3\3\2\2\2\u02fb\u02f7\3\2\2\2")
        buf.write("\u02fc\u009c\3\2\2\2\u02fd\u02fe\7^\2\2\u02fe\u02ff\7")
        buf.write("u\2\2\u02ff\u0300\7k\2\2\u0300\u0301\7i\2\2\u0301\u0302")
        buf.write("\7o\2\2\u0302\u030a\7c\2\2\u0303\u0304\7^\2\2\u0304\u0305")
        buf.write("\7U\2\2\u0305\u0306\7k\2\2\u0306\u0307\7i\2\2\u0307\u0308")
        buf.write("\7o\2\2\u0308\u030a\7c\2\2\u0309\u02fd\3\2\2\2\u0309\u0303")
        buf.write("\3\2\2\2\u030a\u009e\3\2\2\2\u030b\u030c\7^\2\2\u030c")
        buf.write("\u030d\7v\2\2\u030d\u030e\7c\2\2\u030e\u0314\7w\2\2\u030f")
        buf.write("\u0310\7^\2\2\u0310\u0311\7V\2\2\u0311\u0312\7c\2\2\u0312")
        buf.write("\u0314\7w\2\2\u0313\u030b\3\2\2\2\u0313\u030f\3\2\2\2")
        buf.write("\u0314\u00a0\3\2\2\2\u0315\u0316\7^\2\2\u0316\u0317\7")
        buf.write("w\2\2\u0317\u0318\7r\2\2\u0318\u0319\7u\2\2\u0319\u031a")
        buf.write("\7k\2\2\u031a\u031b\7n\2\2\u031b\u031c\7q\2\2\u031c\u0326")
        buf.write("\7p\2\2\u031d\u031e\7^\2\2\u031e\u031f\7W\2\2\u031f\u0320")
        buf.write("\7r\2\2\u0320\u0321\7u\2\2\u0321\u0322\7k\2\2\u0322\u0323")
        buf.write("\7n\2\2\u0323\u0324\7q\2\2\u0324\u0326\7p\2\2\u0325\u0315")
        buf.write("\3\2\2\2\u0325\u031d\3\2\2\2\u0326\u00a2\3\2\2\2\u0327")
        buf.write("\u0328\7^\2\2\u0328\u0329\7r\2\2\u0329\u032a\7j\2\2\u032a")
        buf.write("\u0330\7k\2\2\u032b\u032c\7^\2\2\u032c\u032d\7R\2\2\u032d")
        buf.write("\u032e\7j\2\2\u032e\u0330\7k\2\2\u032f\u0327\3\2\2\2\u032f")
        buf.write("\u032b\3\2\2\2\u0330\u00a4\3\2\2\2\u0331\u0332\7^\2\2")
        buf.write("\u0332\u0333\7e\2\2\u0333\u0334\7j\2\2\u0334\u033a\7k")
        buf.write("\2\2\u0335\u0336\7^\2\2\u0336\u0337\7E\2\2\u0337\u0338")
        buf.write("\7j\2\2\u0338\u033a\7k\2\2\u0339\u0331\3\2\2\2\u0339\u0335")
        buf.write("\3\2\2\2\u033a\u00a6\3\2\2\2\u033b\u033c\7^\2\2\u033c")
        buf.write("\u033d\7r\2\2\u033d\u033e\7u\2\2\u033e\u0344\7k\2\2\u033f")
        buf.write("\u0340\7^\2\2\u0340\u0341\7R\2\2\u0341\u0342\7u\2\2\u0342")
        buf.write("\u0344\7k\2\2\u0343\u033b\3\2\2\2\u0343\u033f\3\2\2\2")
        buf.write("\u0344\u00a8\3\2\2\2\u0345\u0346\7^\2\2\u0346\u0347\7")
        buf.write("q\2\2\u0347\u0348\7o\2\2\u0348\u0349\7g\2\2\u0349\u034a")
        buf.write("\7i\2\2\u034a\u0352\7c\2\2\u034b\u034c\7^\2\2\u034c\u034d")
        buf.write("\7Q\2\2\u034d\u034e\7o\2\2\u034e\u034f\7g\2\2\u034f\u0350")
        buf.write("\7i\2\2\u0350\u0352\7c\2\2\u0351\u0345\3\2\2\2\u0351\u034b")
        buf.write("\3\2\2\2\u0352\u00aa\3\2\2\2\u0353\u036c\5{>\2\u0354\u036c")
        buf.write("\5}?\2\u0355\u036c\5\177@\2\u0356\u036c\5\u0081A\2\u0357")
        buf.write("\u036c\5\u0083B\2\u0358\u036c\5\u0085C\2\u0359\u036c\5")
        buf.write("\u0087D\2\u035a\u036c\5\u0089E\2\u035b\u036c\5\u008bF")
        buf.write("\2\u035c\u036c\5\u008dG\2\u035d\u036c\5\u008fH\2\u035e")
        buf.write("\u036c\5\u0091I\2\u035f\u036c\5\u0093J\2\u0360\u036c\5")
        buf.write("\u0095K\2\u0361\u036c\5\u0097L\2\u0362\u036c\5\u0099M")
        buf.write("\2\u0363\u036c\5\u009bN\2\u0364\u036c\5\u009dO\2\u0365")
        buf.write("\u036c\5\u009fP\2\u0366\u036c\5\u00a1Q\2\u0367\u036c\5")
        buf.write("\u00a3R\2\u0368\u036c\5\u00a5S\2\u0369\u036c\5\u00a7T")
        buf.write("\2\u036a\u036c\5\u00a9U\2\u036b\u0353\3\2\2\2\u036b\u0354")
        buf.write("\3\2\2\2\u036b\u0355\3\2\2\2\u036b\u0356\3\2\2\2\u036b")
        buf.write("\u0357\3\2\2\2\u036b\u0358\3\2\2\2\u036b\u0359\3\2\2\2")
        buf.write("\u036b\u035a\3\2\2\2\u036b\u035b\3\2\2\2\u036b\u035c\3")
        buf.write("\2\2\2\u036b\u035d\3\2\2\2\u036b\u035e\3\2\2\2\u036b\u035f")
        buf.write("\3\2\2\2\u036b\u0360\3\2\2\2\u036b\u0361\3\2\2\2\u036b")
        buf.write("\u0362\3\2\2\2\u036b\u0363\3\2\2\2\u036b\u0364\3\2\2\2")
        buf.write("\u036b\u0365\3\2\2\2\u036b\u0366\3\2\2\2\u036b\u0367\3")
        buf.write("\2\2\2\u036b\u0368\3\2\2\2\u036b\u0369\3\2\2\2\u036b\u036a")
        buf.write("\3\2\2\2\u036c\u00ac\3\2\2\2\u036d\u036f\t\6\2\2\u036e")
        buf.write("\u036d\3\2\2\2\u036f\u0370\3\2\2\2\u0370\u036e\3\2\2\2")
        buf.write("\u0370\u0371\3\2\2\2\u0371\u0372\3\2\2\2\u0372\u0373\b")
        buf.write("W\2\2\u0373\u00ae\3\2\2\2;\2\u0105\u0118\u011f\u0125\u012c")
        buf.write("\u0133\u013a\u0141\u0148\u014f\u0159\u0163\u016d\u0177")
        buf.write("\u0181\u018b\u0193\u019b\u01a3\u01ad\u01b7\u01c1\u01ef")
        buf.write("\u01f3\u01f8\u01fc\u0201\u0203\u020b\u0210\u0237\u0243")
        buf.write("\u0251\u025f\u0271\u027d\u0287\u0295\u02a1\u02af\u02bf")
        buf.write("\u02c7\u02cf\u02d7\u02e9\u02f1\u02fb\u0309\u0313\u0325")
        buf.write("\u032f\u0339\u0343\u0351\u036b\u0370\3\b\2\2")
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
    FUNC_LIM = 14
    LIM_APPROACH_SYM = 15
    FUNC_INT = 16
    FUNC_SUM = 17
    FUNC_PROD = 18
    FUNC_LOG = 19
    FUNC_LN = 20
    FUNC_SIN = 21
    FUNC_COS = 22
    FUNC_TAN = 23
    FUNC_CSC = 24
    FUNC_SEC = 25
    FUNC_COT = 26
    FUNC_ARCSIN = 27
    FUNC_ARCCOS = 28
    FUNC_ARCTAN = 29
    FUNC_ARCCSC = 30
    FUNC_ARCSEC = 31
    FUNC_ARCCOT = 32
    FUNC_SINH = 33
    FUNC_COSH = 34
    FUNC_TANH = 35
    FUNC_ARCSINH = 36
    FUNC_ARCCOSH = 37
    FUNC_ARCTANH = 38
    FUNC_SQRT = 39
    CMD_TIMES = 40
    CMD_CDOT = 41
    CMD_DIV = 42
    CMD_FRAC = 43
    UNDERSCORE = 44
    CARET = 45
    COLON = 46
    BACKSLASH = 47
    NUMBER = 48
    DERIVATIVE = 49
    VARIABLE = 50
    MIXNUMBER = 51
    INFINITY = 52
    EQ = 53
    LT = 54
    LTE = 55
    GT = 56
    GTE = 57
    BANG = 58
    GREEKLETTER = 59
    WS = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "'.'", "'|'", "'\\lim'", "'\\int'", "'\\sum'", 
            "'\\prod'", "'\\times'", "'\\cdot'", "'\\div'", "'\\frac'", 
            "'_'", "'^'", "':'", "'\\'", "'\\infty'", "'='", "'<'", "'\\leq'", 
            "'>'", "'\\geq'", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MUL", "DIV", "L_PAREN", "R_PAREN", "L_BRACE", 
            "R_BRACE", "L_BRACKET", "R_BRACKET", "COMMA", "DOT", "BAR", 
            "FUNC_LIM", "LIM_APPROACH_SYM", "FUNC_INT", "FUNC_SUM", "FUNC_PROD", 
            "FUNC_LOG", "FUNC_LN", "FUNC_SIN", "FUNC_COS", "FUNC_TAN", "FUNC_CSC", 
            "FUNC_SEC", "FUNC_COT", "FUNC_ARCSIN", "FUNC_ARCCOS", "FUNC_ARCTAN", 
            "FUNC_ARCCSC", "FUNC_ARCSEC", "FUNC_ARCCOT", "FUNC_SINH", "FUNC_COSH", 
            "FUNC_TANH", "FUNC_ARCSINH", "FUNC_ARCCOSH", "FUNC_ARCTANH", 
            "FUNC_SQRT", "CMD_TIMES", "CMD_CDOT", "CMD_DIV", "CMD_FRAC", 
            "UNDERSCORE", "CARET", "COLON", "BACKSLASH", "NUMBER", "DERIVATIVE", 
            "VARIABLE", "MIXNUMBER", "INFINITY", "EQ", "LT", "LTE", "GT", 
            "GTE", "BANG", "GREEKLETTER", "WS" ]

    ruleNames = [ "PLUS", "MINUS", "MUL", "DIV", "L_PAREN", "R_PAREN", "L_BRACE", 
                  "R_BRACE", "L_BRACKET", "R_BRACKET", "COMMA", "DOT", "BAR", 
                  "FUNC_LIM", "LIM_APPROACH_SYM", "FUNC_INT", "FUNC_SUM", 
                  "FUNC_PROD", "FUNC_LOG", "FUNC_LN", "FUNC_SIN", "FUNC_COS", 
                  "FUNC_TAN", "FUNC_CSC", "FUNC_SEC", "FUNC_COT", "FUNC_ARCSIN", 
                  "FUNC_ARCCOS", "FUNC_ARCTAN", "FUNC_ARCCSC", "FUNC_ARCSEC", 
                  "FUNC_ARCCOT", "FUNC_SINH", "FUNC_COSH", "FUNC_TANH", 
                  "FUNC_ARCSINH", "FUNC_ARCCOSH", "FUNC_ARCTANH", "FUNC_SQRT", 
                  "CMD_TIMES", "CMD_CDOT", "CMD_DIV", "CMD_FRAC", "UNDERSCORE", 
                  "CARET", "COLON", "BACKSLASH", "LETTER", "DIGIT", "NUMBER", 
                  "DERIVATIVE", "VARIABLE", "MIXNUMBER", "INFINITY", "EQ", 
                  "LT", "LTE", "GT", "GTE", "BANG", "ALPHA", "BETA", "GAMMA", 
                  "DELTA", "EPSILON", "ZETA", "ETA", "THETA", "IOTA", "KAPPA", 
                  "LAMBDA", "MU", "NU", "XI", "OMICRON", "PI", "RHO", "SIGMA", 
                  "TAU", "UPSILON", "PHI", "CHI", "PSI", "OMEGA", "GREEKLETTER", 
                  "WS" ]

    grammarFileName = "MatexLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


