# Generated from .\grammar\MatexLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u036d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0104\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\5\24\u0117\n\24\3\24\3")
        buf.write("\24\3\24\3\24\3\25\5\25\u011e\n\25\3\25\3\25\3\25\3\26")
        buf.write("\5\26\u0124\n\26\3\26\3\26\3\26\3\26\3\27\5\27\u012b\n")
        buf.write("\27\3\27\3\27\3\27\3\27\3\30\5\30\u0132\n\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\5\31\u0139\n\31\3\31\3\31\3\31\3\31\3")
        buf.write("\32\5\32\u0140\n\32\3\32\3\32\3\32\3\32\3\33\5\33\u0147")
        buf.write("\n\33\3\33\3\33\3\33\3\33\3\34\5\34\u014e\n\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\35\5\35\u0158\n\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\5\36\u0162\n\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\5\37\u016c\n\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \5 \u0176\n \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\5!\u0180\n!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3\"\5\"\u018a\n\"\3\"\3\"\3\"\3\"\3\"\3#\5#\u0192\n")
        buf.write("#\3#\3#\3#\3#\3#\3$\5$\u019a\n$\3$\3$\3$\3$\3$\3%\5%\u01a2")
        buf.write("\n%\3%\3%\3%\3%\3%\3%\3%\3&\5&\u01ac\n&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\5\'\u01b6\n\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3(\5(\u01c0\n(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\7\63")
        buf.write("\u01ec\n\63\f\63\16\63\u01ef\13\63\3\63\5\63\u01f2\n\63")
        buf.write("\3\63\6\63\u01f5\n\63\r\63\16\63\u01f6\3\63\3\63\5\63")
        buf.write("\u01fb\n\63\3\63\6\63\u01fe\n\63\r\63\16\63\u01ff\5\63")
        buf.write("\u0202\n\63\3\64\6\64\u0205\n\64\r\64\16\64\u0206\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\39\39\39\3:\3:\3;\3;\3;\3;\3;\3<\3<\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u0231\n=\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\5>\u023d\n>\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\5?\u024b\n?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\5@\u0259\n@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\5A\u026b\nA\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\5B\u0277\nB\3C\3C\3C\3C\3C\3C\3C\3C\5C\u0281\nC\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\5D\u028f\nD\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\5E\u029b\nE\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\3F\3F\3F\5F\u02a9\nF\3G\3G\3G\3G\3G\3G\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3G\5G\u02b9\nG\3H\3H\3H\3H\3H\3H\5H\u02c1\n")
        buf.write("H\3I\3I\3I\3I\3I\3I\5I\u02c9\nI\3J\3J\3J\3J\3J\3J\5J\u02d1")
        buf.write("\nJ\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\5")
        buf.write("K\u02e3\nK\3L\3L\3L\3L\3L\3L\5L\u02eb\nL\3M\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\5M\u02f5\nM\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3")
        buf.write("N\3N\5N\u0303\nN\3O\3O\3O\3O\3O\3O\3O\3O\5O\u030d\nO\3")
        buf.write("P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u031f")
        buf.write("\nP\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u0329\nQ\3R\3R\3R\3R\3")
        buf.write("R\3R\3R\3R\5R\u0333\nR\3S\3S\3S\3S\3S\3S\3S\3S\5S\u033d")
        buf.write("\nS\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\5T\u034b\nT\3")
        buf.write("U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\5U\u0365\nU\3V\6V\u0368\nV\rV\16V\u0369")
        buf.write("\3V\3V\2\2W\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\2c\2e\62g\63i\64k\65")
        buf.write("m\66o\67q8s9u:w;y\2{\2}\2\177\2\u0081\2\u0083\2\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093")
        buf.write("\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1")
        buf.write("\2\u00a3\2\u00a5\2\u00a7\2\u00a9<\u00ab=\3\2\7\4\2C\\")
        buf.write("c|\3\2\62;\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2\u03a2")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3")
        buf.write("\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\3")
        buf.write("\u00ad\3\2\2\2\5\u00af\3\2\2\2\7\u00b1\3\2\2\2\t\u00b3")
        buf.write("\3\2\2\2\13\u00b5\3\2\2\2\r\u00b7\3\2\2\2\17\u00b9\3\2")
        buf.write("\2\2\21\u00bb\3\2\2\2\23\u00bd\3\2\2\2\25\u00bf\3\2\2")
        buf.write("\2\27\u00c1\3\2\2\2\31\u00c3\3\2\2\2\33\u00c5\3\2\2\2")
        buf.write("\35\u00c7\3\2\2\2\37\u0103\3\2\2\2!\u0105\3\2\2\2#\u010a")
        buf.write("\3\2\2\2%\u010f\3\2\2\2\'\u0116\3\2\2\2)\u011d\3\2\2\2")
        buf.write("+\u0123\3\2\2\2-\u012a\3\2\2\2/\u0131\3\2\2\2\61\u0138")
        buf.write("\3\2\2\2\63\u013f\3\2\2\2\65\u0146\3\2\2\2\67\u014d\3")
        buf.write("\2\2\29\u0157\3\2\2\2;\u0161\3\2\2\2=\u016b\3\2\2\2?\u0175")
        buf.write("\3\2\2\2A\u017f\3\2\2\2C\u0189\3\2\2\2E\u0191\3\2\2\2")
        buf.write("G\u0199\3\2\2\2I\u01a1\3\2\2\2K\u01ab\3\2\2\2M\u01b5\3")
        buf.write("\2\2\2O\u01bf\3\2\2\2Q\u01c6\3\2\2\2S\u01cd\3\2\2\2U\u01d3")
        buf.write("\3\2\2\2W\u01d8\3\2\2\2Y\u01de\3\2\2\2[\u01e0\3\2\2\2")
        buf.write("]\u01e2\3\2\2\2_\u01e4\3\2\2\2a\u01e6\3\2\2\2c\u01e8\3")
        buf.write("\2\2\2e\u01ed\3\2\2\2g\u0204\3\2\2\2i\u0208\3\2\2\2k\u020b")
        buf.write("\3\2\2\2m\u0212\3\2\2\2o\u0214\3\2\2\2q\u0216\3\2\2\2")
        buf.write("s\u021b\3\2\2\2u\u021d\3\2\2\2w\u0222\3\2\2\2y\u0230\3")
        buf.write("\2\2\2{\u023c\3\2\2\2}\u024a\3\2\2\2\177\u0258\3\2\2\2")
        buf.write("\u0081\u026a\3\2\2\2\u0083\u0276\3\2\2\2\u0085\u0280\3")
        buf.write("\2\2\2\u0087\u028e\3\2\2\2\u0089\u029a\3\2\2\2\u008b\u02a8")
        buf.write("\3\2\2\2\u008d\u02b8\3\2\2\2\u008f\u02c0\3\2\2\2\u0091")
        buf.write("\u02c8\3\2\2\2\u0093\u02d0\3\2\2\2\u0095\u02e2\3\2\2\2")
        buf.write("\u0097\u02ea\3\2\2\2\u0099\u02f4\3\2\2\2\u009b\u0302\3")
        buf.write("\2\2\2\u009d\u030c\3\2\2\2\u009f\u031e\3\2\2\2\u00a1\u0328")
        buf.write("\3\2\2\2\u00a3\u0332\3\2\2\2\u00a5\u033c\3\2\2\2\u00a7")
        buf.write("\u034a\3\2\2\2\u00a9\u0364\3\2\2\2\u00ab\u0367\3\2\2\2")
        buf.write("\u00ad\u00ae\7-\2\2\u00ae\4\3\2\2\2\u00af\u00b0\7/\2\2")
        buf.write("\u00b0\6\3\2\2\2\u00b1\u00b2\7,\2\2\u00b2\b\3\2\2\2\u00b3")
        buf.write("\u00b4\7\61\2\2\u00b4\n\3\2\2\2\u00b5\u00b6\7*\2\2\u00b6")
        buf.write("\f\3\2\2\2\u00b7\u00b8\7+\2\2\u00b8\16\3\2\2\2\u00b9\u00ba")
        buf.write("\7}\2\2\u00ba\20\3\2\2\2\u00bb\u00bc\7\177\2\2\u00bc\22")
        buf.write("\3\2\2\2\u00bd\u00be\7]\2\2\u00be\24\3\2\2\2\u00bf\u00c0")
        buf.write("\7_\2\2\u00c0\26\3\2\2\2\u00c1\u00c2\7.\2\2\u00c2\30\3")
        buf.write("\2\2\2\u00c3\u00c4\7\60\2\2\u00c4\32\3\2\2\2\u00c5\u00c6")
        buf.write("\7~\2\2\u00c6\34\3\2\2\2\u00c7\u00c8\7^\2\2\u00c8\u00c9")
        buf.write("\7n\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7o\2\2\u00cb\36")
        buf.write("\3\2\2\2\u00cc\u00cd\7^\2\2\u00cd\u00ce\7v\2\2\u00ce\u0104")
        buf.write("\7q\2\2\u00cf\u00d0\7^\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7i\2\2\u00d3\u00d4\7j\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\u00d9\7q\2\2\u00d9\u0104\7y\2\2\u00da\u00db")
        buf.write("\7^\2\2\u00db\u00dc\7T\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de")
        buf.write("\7i\2\2\u00de\u00df\7j\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1")
        buf.write("\7c\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u0104\7y\2\2\u00e5\u00e6\7^\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7i\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed")
        buf.write("\7i\2\2\u00ed\u00ee\7j\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u0104\7y\2\2\u00f4\u00f5\7^\2\2\u00f5\u00f6")
        buf.write("\7N\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7i\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc")
        buf.write("\7i\2\2\u00fc\u00fd\7j\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7q\2\2\u0102\u0104\7y\2\2\u0103\u00cc\3\2\2\2\u0103\u00cf")
        buf.write("\3\2\2\2\u0103\u00da\3\2\2\2\u0103\u00e5\3\2\2\2\u0103")
        buf.write("\u00f4\3\2\2\2\u0104 \3\2\2\2\u0105\u0106\7^\2\2\u0106")
        buf.write("\u0107\7k\2\2\u0107\u0108\7p\2\2\u0108\u0109\7v\2\2\u0109")
        buf.write("\"\3\2\2\2\u010a\u010b\7^\2\2\u010b\u010c\7u\2\2\u010c")
        buf.write("\u010d\7w\2\2\u010d\u010e\7o\2\2\u010e$\3\2\2\2\u010f")
        buf.write("\u0110\7^\2\2\u0110\u0111\7r\2\2\u0111\u0112\7t\2\2\u0112")
        buf.write("\u0113\7q\2\2\u0113\u0114\7f\2\2\u0114&\3\2\2\2\u0115")
        buf.write("\u0117\5_\60\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\u0118\3\2\2\2\u0118\u0119\7n\2\2\u0119\u011a\7")
        buf.write("q\2\2\u011a\u011b\7i\2\2\u011b(\3\2\2\2\u011c\u011e\5")
        buf.write("_\60\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f")
        buf.write("\3\2\2\2\u011f\u0120\7n\2\2\u0120\u0121\7p\2\2\u0121*")
        buf.write("\3\2\2\2\u0122\u0124\5_\60\2\u0123\u0122\3\2\2\2\u0123")
        buf.write("\u0124\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\7u\2\2")
        buf.write("\u0126\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128,\3\2\2\2")
        buf.write("\u0129\u012b\5_\60\2\u012a\u0129\3\2\2\2\u012a\u012b\3")
        buf.write("\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\7e\2\2\u012d\u012e")
        buf.write("\7q\2\2\u012e\u012f\7u\2\2\u012f.\3\2\2\2\u0130\u0132")
        buf.write("\5_\60\2\u0131\u0130\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133\u0134\7v\2\2\u0134\u0135\7c\2\2\u0135")
        buf.write("\u0136\7p\2\2\u0136\60\3\2\2\2\u0137\u0139\5_\60\2\u0138")
        buf.write("\u0137\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013a\u013b\7e\2\2\u013b\u013c\7u\2\2\u013c\u013d\7e")
        buf.write("\2\2\u013d\62\3\2\2\2\u013e\u0140\5_\60\2\u013f\u013e")
        buf.write("\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0142\7u\2\2\u0142\u0143\7g\2\2\u0143\u0144\7e\2\2\u0144")
        buf.write("\64\3\2\2\2\u0145\u0147\5_\60\2\u0146\u0145\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\7e\2\2")
        buf.write("\u0149\u014a\7q\2\2\u014a\u014b\7v\2\2\u014b\66\3\2\2")
        buf.write("\2\u014c\u014e\5_\60\2\u014d\u014c\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\7c\2\2\u0150")
        buf.write("\u0151\7t\2\2\u0151\u0152\7e\2\2\u0152\u0153\7u\2\2\u0153")
        buf.write("\u0154\7k\2\2\u0154\u0155\7p\2\2\u01558\3\2\2\2\u0156")
        buf.write("\u0158\5_\60\2\u0157\u0156\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u0159\3\2\2\2\u0159\u015a\7c\2\2\u015a\u015b\7")
        buf.write("t\2\2\u015b\u015c\7e\2\2\u015c\u015d\7e\2\2\u015d\u015e")
        buf.write("\7q\2\2\u015e\u015f\7u\2\2\u015f:\3\2\2\2\u0160\u0162")
        buf.write("\5_\60\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0164\7c\2\2\u0164\u0165\7t\2\2\u0165")
        buf.write("\u0166\7e\2\2\u0166\u0167\7v\2\2\u0167\u0168\7c\2\2\u0168")
        buf.write("\u0169\7p\2\2\u0169<\3\2\2\2\u016a\u016c\5_\60\2\u016b")
        buf.write("\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u016e\7c\2\2\u016e\u016f\7t\2\2\u016f\u0170\7e")
        buf.write("\2\2\u0170\u0171\7e\2\2\u0171\u0172\7u\2\2\u0172\u0173")
        buf.write("\7e\2\2\u0173>\3\2\2\2\u0174\u0176\5_\60\2\u0175\u0174")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\3\2\2\2\u0177")
        buf.write("\u0178\7c\2\2\u0178\u0179\7t\2\2\u0179\u017a\7e\2\2\u017a")
        buf.write("\u017b\7u\2\2\u017b\u017c\7g\2\2\u017c\u017d\7e\2\2\u017d")
        buf.write("@\3\2\2\2\u017e\u0180\5_\60\2\u017f\u017e\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\7c\2\2")
        buf.write("\u0182\u0183\7t\2\2\u0183\u0184\7e\2\2\u0184\u0185\7e")
        buf.write("\2\2\u0185\u0186\7q\2\2\u0186\u0187\7v\2\2\u0187B\3\2")
        buf.write("\2\2\u0188\u018a\5_\60\2\u0189\u0188\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018c\7u\2\2\u018c")
        buf.write("\u018d\7k\2\2\u018d\u018e\7p\2\2\u018e\u018f\7j\2\2\u018f")
        buf.write("D\3\2\2\2\u0190\u0192\5_\60\2\u0191\u0190\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194\7e\2\2")
        buf.write("\u0194\u0195\7q\2\2\u0195\u0196\7u\2\2\u0196\u0197\7j")
        buf.write("\2\2\u0197F\3\2\2\2\u0198\u019a\5_\60\2\u0199\u0198\3")
        buf.write("\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c")
        buf.write("\7v\2\2\u019c\u019d\7c\2\2\u019d\u019e\7p\2\2\u019e\u019f")
        buf.write("\7j\2\2\u019fH\3\2\2\2\u01a0\u01a2\5_\60\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a4\7c\2\2\u01a4\u01a5\7t\2\2\u01a5\u01a6\7u\2\2\u01a6")
        buf.write("\u01a7\7k\2\2\u01a7\u01a8\7p\2\2\u01a8\u01a9\7j\2\2\u01a9")
        buf.write("J\3\2\2\2\u01aa\u01ac\5_\60\2\u01ab\u01aa\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\7c\2\2")
        buf.write("\u01ae\u01af\7t\2\2\u01af\u01b0\7e\2\2\u01b0\u01b1\7q")
        buf.write("\2\2\u01b1\u01b2\7u\2\2\u01b2\u01b3\7j\2\2\u01b3L\3\2")
        buf.write("\2\2\u01b4\u01b6\5_\60\2\u01b5\u01b4\3\2\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\7c\2\2\u01b8")
        buf.write("\u01b9\7t\2\2\u01b9\u01ba\7v\2\2\u01ba\u01bb\7c\2\2\u01bb")
        buf.write("\u01bc\7p\2\2\u01bc\u01bd\7j\2\2\u01bdN\3\2\2\2\u01be")
        buf.write("\u01c0\5_\60\2\u01bf\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2")
        buf.write("\u01c0\u01c1\3\2\2\2\u01c1\u01c2\7u\2\2\u01c2\u01c3\7")
        buf.write("s\2\2\u01c3\u01c4\7t\2\2\u01c4\u01c5\7v\2\2\u01c5P\3\2")
        buf.write("\2\2\u01c6\u01c7\7^\2\2\u01c7\u01c8\7v\2\2\u01c8\u01c9")
        buf.write("\7k\2\2\u01c9\u01ca\7o\2\2\u01ca\u01cb\7g\2\2\u01cb\u01cc")
        buf.write("\7u\2\2\u01ccR\3\2\2\2\u01cd\u01ce\7^\2\2\u01ce\u01cf")
        buf.write("\7e\2\2\u01cf\u01d0\7f\2\2\u01d0\u01d1\7q\2\2\u01d1\u01d2")
        buf.write("\7v\2\2\u01d2T\3\2\2\2\u01d3\u01d4\7^\2\2\u01d4\u01d5")
        buf.write("\7f\2\2\u01d5\u01d6\7k\2\2\u01d6\u01d7\7x\2\2\u01d7V\3")
        buf.write("\2\2\2\u01d8\u01d9\7^\2\2\u01d9\u01da\7h\2\2\u01da\u01db")
        buf.write("\7t\2\2\u01db\u01dc\7c\2\2\u01dc\u01dd\7e\2\2\u01ddX\3")
        buf.write("\2\2\2\u01de\u01df\7a\2\2\u01dfZ\3\2\2\2\u01e0\u01e1\7")
        buf.write("`\2\2\u01e1\\\3\2\2\2\u01e2\u01e3\7<\2\2\u01e3^\3\2\2")
        buf.write("\2\u01e4\u01e5\7^\2\2\u01e5`\3\2\2\2\u01e6\u01e7\t\2\2")
        buf.write("\2\u01e7b\3\2\2\2\u01e8\u01e9\t\3\2\2\u01e9d\3\2\2\2\u01ea")
        buf.write("\u01ec\5c\62\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2")
        buf.write("\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f1\3")
        buf.write("\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f2\7\60\2\2\u01f1")
        buf.write("\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f4\3\2\2\2")
        buf.write("\u01f3\u01f5\5c\62\2\u01f4\u01f3\3\2\2\2\u01f5\u01f6\3")
        buf.write("\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u0201")
        buf.write("\3\2\2\2\u01f8\u01fa\t\4\2\2\u01f9\u01fb\t\5\2\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fd\3\2\2\2")
        buf.write("\u01fc\u01fe\5c\62\2\u01fd\u01fc\3\2\2\2\u01fe\u01ff\3")
        buf.write("\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0202")
        buf.write("\3\2\2\2\u0201\u01f8\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("f\3\2\2\2\u0203\u0205\5a\61\2\u0204\u0203\3\2\2\2\u0205")
        buf.write("\u0206\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2")
        buf.write("\u0207h\3\2\2\2\u0208\u0209\5e\63\2\u0209\u020a\5g\64")
        buf.write("\2\u020aj\3\2\2\2\u020b\u020c\7^\2\2\u020c\u020d\7k\2")
        buf.write("\2\u020d\u020e\7p\2\2\u020e\u020f\7h\2\2\u020f\u0210\7")
        buf.write("v\2\2\u0210\u0211\7{\2\2\u0211l\3\2\2\2\u0212\u0213\7")
        buf.write("?\2\2\u0213n\3\2\2\2\u0214\u0215\7>\2\2\u0215p\3\2\2\2")
        buf.write("\u0216\u0217\7^\2\2\u0217\u0218\7n\2\2\u0218\u0219\7g")
        buf.write("\2\2\u0219\u021a\7s\2\2\u021ar\3\2\2\2\u021b\u021c\7@")
        buf.write("\2\2\u021ct\3\2\2\2\u021d\u021e\7^\2\2\u021e\u021f\7i")
        buf.write("\2\2\u021f\u0220\7g\2\2\u0220\u0221\7s\2\2\u0221v\3\2")
        buf.write("\2\2\u0222\u0223\7#\2\2\u0223x\3\2\2\2\u0224\u0225\7^")
        buf.write("\2\2\u0225\u0226\7c\2\2\u0226\u0227\7n\2\2\u0227\u0228")
        buf.write("\7r\2\2\u0228\u0229\7j\2\2\u0229\u0231\7c\2\2\u022a\u022b")
        buf.write("\7^\2\2\u022b\u022c\7C\2\2\u022c\u022d\7n\2\2\u022d\u022e")
        buf.write("\7r\2\2\u022e\u022f\7j\2\2\u022f\u0231\7c\2\2\u0230\u0224")
        buf.write("\3\2\2\2\u0230\u022a\3\2\2\2\u0231z\3\2\2\2\u0232\u0233")
        buf.write("\7^\2\2\u0233\u0234\7d\2\2\u0234\u0235\7g\2\2\u0235\u0236")
        buf.write("\7v\2\2\u0236\u023d\7c\2\2\u0237\u0238\7^\2\2\u0238\u0239")
        buf.write("\7D\2\2\u0239\u023a\7g\2\2\u023a\u023b\7v\2\2\u023b\u023d")
        buf.write("\7c\2\2\u023c\u0232\3\2\2\2\u023c\u0237\3\2\2\2\u023d")
        buf.write("|\3\2\2\2\u023e\u023f\7^\2\2\u023f\u0240\7i\2\2\u0240")
        buf.write("\u0241\7c\2\2\u0241\u0242\7o\2\2\u0242\u0243\7o\2\2\u0243")
        buf.write("\u024b\7c\2\2\u0244\u0245\7^\2\2\u0245\u0246\7I\2\2\u0246")
        buf.write("\u0247\7c\2\2\u0247\u0248\7o\2\2\u0248\u0249\7o\2\2\u0249")
        buf.write("\u024b\7c\2\2\u024a\u023e\3\2\2\2\u024a\u0244\3\2\2\2")
        buf.write("\u024b~\3\2\2\2\u024c\u024d\7^\2\2\u024d\u024e\7f\2\2")
        buf.write("\u024e\u024f\7g\2\2\u024f\u0250\7n\2\2\u0250\u0251\7v")
        buf.write("\2\2\u0251\u0259\7c\2\2\u0252\u0253\7^\2\2\u0253\u0254")
        buf.write("\7F\2\2\u0254\u0255\7g\2\2\u0255\u0256\7n\2\2\u0256\u0257")
        buf.write("\7v\2\2\u0257\u0259\7c\2\2\u0258\u024c\3\2\2\2\u0258\u0252")
        buf.write("\3\2\2\2\u0259\u0080\3\2\2\2\u025a\u025b\7^\2\2\u025b")
        buf.write("\u025c\7g\2\2\u025c\u025d\7r\2\2\u025d\u025e\7u\2\2\u025e")
        buf.write("\u025f\7k\2\2\u025f\u0260\7n\2\2\u0260\u0261\7q\2\2\u0261")
        buf.write("\u026b\7p\2\2\u0262\u0263\7^\2\2\u0263\u0264\7G\2\2\u0264")
        buf.write("\u0265\7r\2\2\u0265\u0266\7u\2\2\u0266\u0267\7k\2\2\u0267")
        buf.write("\u0268\7n\2\2\u0268\u0269\7q\2\2\u0269\u026b\7p\2\2\u026a")
        buf.write("\u025a\3\2\2\2\u026a\u0262\3\2\2\2\u026b\u0082\3\2\2\2")
        buf.write("\u026c\u026d\7^\2\2\u026d\u026e\7|\2\2\u026e\u026f\7g")
        buf.write("\2\2\u026f\u0270\7v\2\2\u0270\u0277\7c\2\2\u0271\u0272")
        buf.write("\7^\2\2\u0272\u0273\7\\\2\2\u0273\u0274\7g\2\2\u0274\u0275")
        buf.write("\7v\2\2\u0275\u0277\7c\2\2\u0276\u026c\3\2\2\2\u0276\u0271")
        buf.write("\3\2\2\2\u0277\u0084\3\2\2\2\u0278\u0279\7^\2\2\u0279")
        buf.write("\u027a\7g\2\2\u027a\u027b\7v\2\2\u027b\u0281\7c\2\2\u027c")
        buf.write("\u027d\7^\2\2\u027d\u027e\7G\2\2\u027e\u027f\7v\2\2\u027f")
        buf.write("\u0281\7c\2\2\u0280\u0278\3\2\2\2\u0280\u027c\3\2\2\2")
        buf.write("\u0281\u0086\3\2\2\2\u0282\u0283\7^\2\2\u0283\u0284\7")
        buf.write("v\2\2\u0284\u0285\7j\2\2\u0285\u0286\7g\2\2\u0286\u0287")
        buf.write("\7v\2\2\u0287\u028f\7c\2\2\u0288\u0289\7^\2\2\u0289\u028a")
        buf.write("\7V\2\2\u028a\u028b\7j\2\2\u028b\u028c\7g\2\2\u028c\u028d")
        buf.write("\7v\2\2\u028d\u028f\7c\2\2\u028e\u0282\3\2\2\2\u028e\u0288")
        buf.write("\3\2\2\2\u028f\u0088\3\2\2\2\u0290\u0291\7^\2\2\u0291")
        buf.write("\u0292\7k\2\2\u0292\u0293\7q\2\2\u0293\u0294\7v\2\2\u0294")
        buf.write("\u029b\7c\2\2\u0295\u0296\7^\2\2\u0296\u0297\7K\2\2\u0297")
        buf.write("\u0298\7q\2\2\u0298\u0299\7v\2\2\u0299\u029b\7c\2\2\u029a")
        buf.write("\u0290\3\2\2\2\u029a\u0295\3\2\2\2\u029b\u008a\3\2\2\2")
        buf.write("\u029c\u029d\7^\2\2\u029d\u029e\7m\2\2\u029e\u029f\7c")
        buf.write("\2\2\u029f\u02a0\7r\2\2\u02a0\u02a1\7r\2\2\u02a1\u02a9")
        buf.write("\7c\2\2\u02a2\u02a3\7^\2\2\u02a3\u02a4\7M\2\2\u02a4\u02a5")
        buf.write("\7c\2\2\u02a5\u02a6\7r\2\2\u02a6\u02a7\7r\2\2\u02a7\u02a9")
        buf.write("\7c\2\2\u02a8\u029c\3\2\2\2\u02a8\u02a2\3\2\2\2\u02a9")
        buf.write("\u008c\3\2\2\2\u02aa\u02ab\7^\2\2\u02ab\u02ac\7n\2\2\u02ac")
        buf.write("\u02ad\7c\2\2\u02ad\u02ae\7o\2\2\u02ae\u02af\7d\2\2\u02af")
        buf.write("\u02b0\7f\2\2\u02b0\u02b9\7c\2\2\u02b1\u02b2\7^\2\2\u02b2")
        buf.write("\u02b3\7N\2\2\u02b3\u02b4\7c\2\2\u02b4\u02b5\7o\2\2\u02b5")
        buf.write("\u02b6\7d\2\2\u02b6\u02b7\7f\2\2\u02b7\u02b9\7c\2\2\u02b8")
        buf.write("\u02aa\3\2\2\2\u02b8\u02b1\3\2\2\2\u02b9\u008e\3\2\2\2")
        buf.write("\u02ba\u02bb\7^\2\2\u02bb\u02bc\7o\2\2\u02bc\u02c1\7w")
        buf.write("\2\2\u02bd\u02be\7^\2\2\u02be\u02bf\7O\2\2\u02bf\u02c1")
        buf.write("\7w\2\2\u02c0\u02ba\3\2\2\2\u02c0\u02bd\3\2\2\2\u02c1")
        buf.write("\u0090\3\2\2\2\u02c2\u02c3\7^\2\2\u02c3\u02c4\7p\2\2\u02c4")
        buf.write("\u02c9\7w\2\2\u02c5\u02c6\7^\2\2\u02c6\u02c7\7P\2\2\u02c7")
        buf.write("\u02c9\7w\2\2\u02c8\u02c2\3\2\2\2\u02c8\u02c5\3\2\2\2")
        buf.write("\u02c9\u0092\3\2\2\2\u02ca\u02cb\7^\2\2\u02cb\u02cc\7")
        buf.write("z\2\2\u02cc\u02d1\7k\2\2\u02cd\u02ce\7^\2\2\u02ce\u02cf")
        buf.write("\7Z\2\2\u02cf\u02d1\7k\2\2\u02d0\u02ca\3\2\2\2\u02d0\u02cd")
        buf.write("\3\2\2\2\u02d1\u0094\3\2\2\2\u02d2\u02d3\7^\2\2\u02d3")
        buf.write("\u02d4\7q\2\2\u02d4\u02d5\7o\2\2\u02d5\u02d6\7k\2\2\u02d6")
        buf.write("\u02d7\7e\2\2\u02d7\u02d8\7t\2\2\u02d8\u02d9\7q\2\2\u02d9")
        buf.write("\u02e3\7p\2\2\u02da\u02db\7^\2\2\u02db\u02dc\7Q\2\2\u02dc")
        buf.write("\u02dd\7o\2\2\u02dd\u02de\7k\2\2\u02de\u02df\7e\2\2\u02df")
        buf.write("\u02e0\7t\2\2\u02e0\u02e1\7q\2\2\u02e1\u02e3\7p\2\2\u02e2")
        buf.write("\u02d2\3\2\2\2\u02e2\u02da\3\2\2\2\u02e3\u0096\3\2\2\2")
        buf.write("\u02e4\u02e5\7^\2\2\u02e5\u02e6\7r\2\2\u02e6\u02eb\7k")
        buf.write("\2\2\u02e7\u02e8\7^\2\2\u02e8\u02e9\7R\2\2\u02e9\u02eb")
        buf.write("\7k\2\2\u02ea\u02e4\3\2\2\2\u02ea\u02e7\3\2\2\2\u02eb")
        buf.write("\u0098\3\2\2\2\u02ec\u02ed\7^\2\2\u02ed\u02ee\7t\2\2\u02ee")
        buf.write("\u02ef\7j\2\2\u02ef\u02f5\7q\2\2\u02f0\u02f1\7^\2\2\u02f1")
        buf.write("\u02f2\7T\2\2\u02f2\u02f3\7j\2\2\u02f3\u02f5\7q\2\2\u02f4")
        buf.write("\u02ec\3\2\2\2\u02f4\u02f0\3\2\2\2\u02f5\u009a\3\2\2\2")
        buf.write("\u02f6\u02f7\7^\2\2\u02f7\u02f8\7u\2\2\u02f8\u02f9\7k")
        buf.write("\2\2\u02f9\u02fa\7i\2\2\u02fa\u02fb\7o\2\2\u02fb\u0303")
        buf.write("\7c\2\2\u02fc\u02fd\7^\2\2\u02fd\u02fe\7U\2\2\u02fe\u02ff")
        buf.write("\7k\2\2\u02ff\u0300\7i\2\2\u0300\u0301\7o\2\2\u0301\u0303")
        buf.write("\7c\2\2\u0302\u02f6\3\2\2\2\u0302\u02fc\3\2\2\2\u0303")
        buf.write("\u009c\3\2\2\2\u0304\u0305\7^\2\2\u0305\u0306\7v\2\2\u0306")
        buf.write("\u0307\7c\2\2\u0307\u030d\7w\2\2\u0308\u0309\7^\2\2\u0309")
        buf.write("\u030a\7V\2\2\u030a\u030b\7c\2\2\u030b\u030d\7w\2\2\u030c")
        buf.write("\u0304\3\2\2\2\u030c\u0308\3\2\2\2\u030d\u009e\3\2\2\2")
        buf.write("\u030e\u030f\7^\2\2\u030f\u0310\7w\2\2\u0310\u0311\7r")
        buf.write("\2\2\u0311\u0312\7u\2\2\u0312\u0313\7k\2\2\u0313\u0314")
        buf.write("\7n\2\2\u0314\u0315\7q\2\2\u0315\u031f\7p\2\2\u0316\u0317")
        buf.write("\7^\2\2\u0317\u0318\7W\2\2\u0318\u0319\7r\2\2\u0319\u031a")
        buf.write("\7u\2\2\u031a\u031b\7k\2\2\u031b\u031c\7n\2\2\u031c\u031d")
        buf.write("\7q\2\2\u031d\u031f\7p\2\2\u031e\u030e\3\2\2\2\u031e\u0316")
        buf.write("\3\2\2\2\u031f\u00a0\3\2\2\2\u0320\u0321\7^\2\2\u0321")
        buf.write("\u0322\7r\2\2\u0322\u0323\7j\2\2\u0323\u0329\7k\2\2\u0324")
        buf.write("\u0325\7^\2\2\u0325\u0326\7R\2\2\u0326\u0327\7j\2\2\u0327")
        buf.write("\u0329\7k\2\2\u0328\u0320\3\2\2\2\u0328\u0324\3\2\2\2")
        buf.write("\u0329\u00a2\3\2\2\2\u032a\u032b\7^\2\2\u032b\u032c\7")
        buf.write("e\2\2\u032c\u032d\7j\2\2\u032d\u0333\7k\2\2\u032e\u032f")
        buf.write("\7^\2\2\u032f\u0330\7E\2\2\u0330\u0331\7j\2\2\u0331\u0333")
        buf.write("\7k\2\2\u0332\u032a\3\2\2\2\u0332\u032e\3\2\2\2\u0333")
        buf.write("\u00a4\3\2\2\2\u0334\u0335\7^\2\2\u0335\u0336\7r\2\2\u0336")
        buf.write("\u0337\7u\2\2\u0337\u033d\7k\2\2\u0338\u0339\7^\2\2\u0339")
        buf.write("\u033a\7R\2\2\u033a\u033b\7u\2\2\u033b\u033d\7k\2\2\u033c")
        buf.write("\u0334\3\2\2\2\u033c\u0338\3\2\2\2\u033d\u00a6\3\2\2\2")
        buf.write("\u033e\u033f\7^\2\2\u033f\u0340\7q\2\2\u0340\u0341\7o")
        buf.write("\2\2\u0341\u0342\7g\2\2\u0342\u0343\7i\2\2\u0343\u034b")
        buf.write("\7c\2\2\u0344\u0345\7^\2\2\u0345\u0346\7Q\2\2\u0346\u0347")
        buf.write("\7o\2\2\u0347\u0348\7g\2\2\u0348\u0349\7i\2\2\u0349\u034b")
        buf.write("\7c\2\2\u034a\u033e\3\2\2\2\u034a\u0344\3\2\2\2\u034b")
        buf.write("\u00a8\3\2\2\2\u034c\u0365\5y=\2\u034d\u0365\5{>\2\u034e")
        buf.write("\u0365\5}?\2\u034f\u0365\5\177@\2\u0350\u0365\5\u0081")
        buf.write("A\2\u0351\u0365\5\u0083B\2\u0352\u0365\5\u0085C\2\u0353")
        buf.write("\u0365\5\u0087D\2\u0354\u0365\5\u0089E\2\u0355\u0365\5")
        buf.write("\u008bF\2\u0356\u0365\5\u008dG\2\u0357\u0365\5\u008fH")
        buf.write("\2\u0358\u0365\5\u0091I\2\u0359\u0365\5\u0093J\2\u035a")
        buf.write("\u0365\5\u0095K\2\u035b\u0365\5\u0097L\2\u035c\u0365\5")
        buf.write("\u0099M\2\u035d\u0365\5\u009bN\2\u035e\u0365\5\u009dO")
        buf.write("\2\u035f\u0365\5\u009fP\2\u0360\u0365\5\u00a1Q\2\u0361")
        buf.write("\u0365\5\u00a3R\2\u0362\u0365\5\u00a5S\2\u0363\u0365\5")
        buf.write("\u00a7T\2\u0364\u034c\3\2\2\2\u0364\u034d\3\2\2\2\u0364")
        buf.write("\u034e\3\2\2\2\u0364\u034f\3\2\2\2\u0364\u0350\3\2\2\2")
        buf.write("\u0364\u0351\3\2\2\2\u0364\u0352\3\2\2\2\u0364\u0353\3")
        buf.write("\2\2\2\u0364\u0354\3\2\2\2\u0364\u0355\3\2\2\2\u0364\u0356")
        buf.write("\3\2\2\2\u0364\u0357\3\2\2\2\u0364\u0358\3\2\2\2\u0364")
        buf.write("\u0359\3\2\2\2\u0364\u035a\3\2\2\2\u0364\u035b\3\2\2\2")
        buf.write("\u0364\u035c\3\2\2\2\u0364\u035d\3\2\2\2\u0364\u035e\3")
        buf.write("\2\2\2\u0364\u035f\3\2\2\2\u0364\u0360\3\2\2\2\u0364\u0361")
        buf.write("\3\2\2\2\u0364\u0362\3\2\2\2\u0364\u0363\3\2\2\2\u0365")
        buf.write("\u00aa\3\2\2\2\u0366\u0368\t\6\2\2\u0367\u0366\3\2\2\2")
        buf.write("\u0368\u0369\3\2\2\2\u0369\u0367\3\2\2\2\u0369\u036a\3")
        buf.write("\2\2\2\u036a\u036b\3\2\2\2\u036b\u036c\bV\2\2\u036c\u00ac")
        buf.write("\3\2\2\2:\2\u0103\u0116\u011d\u0123\u012a\u0131\u0138")
        buf.write("\u013f\u0146\u014d\u0157\u0161\u016b\u0175\u017f\u0189")
        buf.write("\u0191\u0199\u01a1\u01ab\u01b5\u01bf\u01ed\u01f1\u01f6")
        buf.write("\u01fa\u01ff\u0201\u0206\u0230\u023c\u024a\u0258\u026a")
        buf.write("\u0276\u0280\u028e\u029a\u02a8\u02b8\u02c0\u02c8\u02d0")
        buf.write("\u02e2\u02ea\u02f4\u0302\u030c\u031e\u0328\u0332\u033c")
        buf.write("\u034a\u0364\u0369\3\b\2\2")
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
    VARIABLE = 49
    MIXNUMBER = 50
    INFINITY = 51
    EQ = 52
    LT = 53
    LTE = 54
    GT = 55
    GTE = 56
    BANG = 57
    GREEKLETTER = 58
    WS = 59

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
            "UNDERSCORE", "CARET", "COLON", "BACKSLASH", "NUMBER", "VARIABLE", 
            "MIXNUMBER", "INFINITY", "EQ", "LT", "LTE", "GT", "GTE", "BANG", 
            "GREEKLETTER", "WS" ]

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
                  "VARIABLE", "MIXNUMBER", "INFINITY", "EQ", "LT", "LTE", 
                  "GT", "GTE", "BANG", "ALPHA", "BETA", "GAMMA", "DELTA", 
                  "EPSILON", "ZETA", "ETA", "THETA", "IOTA", "KAPPA", "LAMBDA", 
                  "MU", "NU", "XI", "OMICRON", "PI", "RHO", "SIGMA", "TAU", 
                  "UPSILON", "PHI", "CHI", "PSI", "OMEGA", "GREEKLETTER", 
                  "WS" ]

    grammarFileName = "MatexLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


