# Generated from .\grammar\MatexLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u0370\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\5\63")
        buf.write("\u01ec\n\63\3\63\7\63\u01ef\n\63\f\63\16\63\u01f2\13\63")
        buf.write("\3\63\5\63\u01f5\n\63\3\63\6\63\u01f8\n\63\r\63\16\63")
        buf.write("\u01f9\3\63\3\63\5\63\u01fe\n\63\3\63\6\63\u0201\n\63")
        buf.write("\r\63\16\63\u0202\5\63\u0205\n\63\3\64\6\64\u0208\n\64")
        buf.write("\r\64\16\64\u0209\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\67\3\67\38\38\39\39\39\39\39\3:\3:\3;")
        buf.write("\3;\3;\3;\3;\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\5=\u0234\n=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u0240\n")
        buf.write(">\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u024e\n?\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u025c\n@\3A\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u026e\nA\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\3B\5B\u027a\nB\3C\3C\3C\3C\3C\3")
        buf.write("C\3C\3C\5C\u0284\nC\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3")
        buf.write("D\5D\u0292\nD\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u029e\n")
        buf.write("E\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u02ac\nF\3G\3")
        buf.write("G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u02bc\nG\3H\3")
        buf.write("H\3H\3H\3H\3H\5H\u02c4\nH\3I\3I\3I\3I\3I\3I\5I\u02cc\n")
        buf.write("I\3J\3J\3J\3J\3J\3J\5J\u02d4\nJ\3K\3K\3K\3K\3K\3K\3K\3")
        buf.write("K\3K\3K\3K\3K\3K\3K\3K\3K\5K\u02e6\nK\3L\3L\3L\3L\3L\3")
        buf.write("L\5L\u02ee\nL\3M\3M\3M\3M\3M\3M\3M\3M\5M\u02f8\nM\3N\3")
        buf.write("N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\5N\u0306\nN\3O\3O\3O\3")
        buf.write("O\3O\3O\3O\3O\5O\u0310\nO\3P\3P\3P\3P\3P\3P\3P\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\3P\5P\u0322\nP\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3")
        buf.write("Q\5Q\u032c\nQ\3R\3R\3R\3R\3R\3R\3R\3R\5R\u0336\nR\3S\3")
        buf.write("S\3S\3S\3S\3S\3S\3S\5S\u0340\nS\3T\3T\3T\3T\3T\3T\3T\3")
        buf.write("T\3T\3T\3T\3T\5T\u034e\nT\3U\3U\3U\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\5U\u0368\n")
        buf.write("U\3V\6V\u036b\nV\rV\16V\u036c\3V\3V\2\2W\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\2c\2e\62g\63i\64k\65m\66o\67q8s9u:w;y\2{\2}\2\177")
        buf.write("\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d")
        buf.write("\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b")
        buf.write("\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7\2\u00a9")
        buf.write("<\u00ab=\3\2\7\4\2C\\c|\3\2\62;\4\2GGgg\4\2--//\5\2\13")
        buf.write("\f\17\17\"\"\2\u03a6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\u00a9\3\2\2\2")
        buf.write("\2\u00ab\3\2\2\2\3\u00ad\3\2\2\2\5\u00af\3\2\2\2\7\u00b1")
        buf.write("\3\2\2\2\t\u00b3\3\2\2\2\13\u00b5\3\2\2\2\r\u00b7\3\2")
        buf.write("\2\2\17\u00b9\3\2\2\2\21\u00bb\3\2\2\2\23\u00bd\3\2\2")
        buf.write("\2\25\u00bf\3\2\2\2\27\u00c1\3\2\2\2\31\u00c3\3\2\2\2")
        buf.write("\33\u00c5\3\2\2\2\35\u00c7\3\2\2\2\37\u0103\3\2\2\2!\u0105")
        buf.write("\3\2\2\2#\u010a\3\2\2\2%\u010f\3\2\2\2\'\u0116\3\2\2\2")
        buf.write(")\u011d\3\2\2\2+\u0123\3\2\2\2-\u012a\3\2\2\2/\u0131\3")
        buf.write("\2\2\2\61\u0138\3\2\2\2\63\u013f\3\2\2\2\65\u0146\3\2")
        buf.write("\2\2\67\u014d\3\2\2\29\u0157\3\2\2\2;\u0161\3\2\2\2=\u016b")
        buf.write("\3\2\2\2?\u0175\3\2\2\2A\u017f\3\2\2\2C\u0189\3\2\2\2")
        buf.write("E\u0191\3\2\2\2G\u0199\3\2\2\2I\u01a1\3\2\2\2K\u01ab\3")
        buf.write("\2\2\2M\u01b5\3\2\2\2O\u01bf\3\2\2\2Q\u01c6\3\2\2\2S\u01cd")
        buf.write("\3\2\2\2U\u01d3\3\2\2\2W\u01d8\3\2\2\2Y\u01de\3\2\2\2")
        buf.write("[\u01e0\3\2\2\2]\u01e2\3\2\2\2_\u01e4\3\2\2\2a\u01e6\3")
        buf.write("\2\2\2c\u01e8\3\2\2\2e\u01eb\3\2\2\2g\u0207\3\2\2\2i\u020b")
        buf.write("\3\2\2\2k\u020e\3\2\2\2m\u0215\3\2\2\2o\u0217\3\2\2\2")
        buf.write("q\u0219\3\2\2\2s\u021e\3\2\2\2u\u0220\3\2\2\2w\u0225\3")
        buf.write("\2\2\2y\u0233\3\2\2\2{\u023f\3\2\2\2}\u024d\3\2\2\2\177")
        buf.write("\u025b\3\2\2\2\u0081\u026d\3\2\2\2\u0083\u0279\3\2\2\2")
        buf.write("\u0085\u0283\3\2\2\2\u0087\u0291\3\2\2\2\u0089\u029d\3")
        buf.write("\2\2\2\u008b\u02ab\3\2\2\2\u008d\u02bb\3\2\2\2\u008f\u02c3")
        buf.write("\3\2\2\2\u0091\u02cb\3\2\2\2\u0093\u02d3\3\2\2\2\u0095")
        buf.write("\u02e5\3\2\2\2\u0097\u02ed\3\2\2\2\u0099\u02f7\3\2\2\2")
        buf.write("\u009b\u0305\3\2\2\2\u009d\u030f\3\2\2\2\u009f\u0321\3")
        buf.write("\2\2\2\u00a1\u032b\3\2\2\2\u00a3\u0335\3\2\2\2\u00a5\u033f")
        buf.write("\3\2\2\2\u00a7\u034d\3\2\2\2\u00a9\u0367\3\2\2\2\u00ab")
        buf.write("\u036a\3\2\2\2\u00ad\u00ae\7-\2\2\u00ae\4\3\2\2\2\u00af")
        buf.write("\u00b0\7/\2\2\u00b0\6\3\2\2\2\u00b1\u00b2\7,\2\2\u00b2")
        buf.write("\b\3\2\2\2\u00b3\u00b4\7\61\2\2\u00b4\n\3\2\2\2\u00b5")
        buf.write("\u00b6\7*\2\2\u00b6\f\3\2\2\2\u00b7\u00b8\7+\2\2\u00b8")
        buf.write("\16\3\2\2\2\u00b9\u00ba\7}\2\2\u00ba\20\3\2\2\2\u00bb")
        buf.write("\u00bc\7\177\2\2\u00bc\22\3\2\2\2\u00bd\u00be\7]\2\2\u00be")
        buf.write("\24\3\2\2\2\u00bf\u00c0\7_\2\2\u00c0\26\3\2\2\2\u00c1")
        buf.write("\u00c2\7.\2\2\u00c2\30\3\2\2\2\u00c3\u00c4\7\60\2\2\u00c4")
        buf.write("\32\3\2\2\2\u00c5\u00c6\7~\2\2\u00c6\34\3\2\2\2\u00c7")
        buf.write("\u00c8\7^\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca\7k\2\2\u00ca")
        buf.write("\u00cb\7o\2\2\u00cb\36\3\2\2\2\u00cc\u00cd\7^\2\2\u00cd")
        buf.write("\u00ce\7v\2\2\u00ce\u0104\7q\2\2\u00cf\u00d0\7^\2\2\u00d0")
        buf.write("\u00d1\7t\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7i\2\2\u00d3")
        buf.write("\u00d4\7j\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6\7c\2\2\u00d6")
        buf.write("\u00d7\7t\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7q\2\2\u00d9")
        buf.write("\u0104\7y\2\2\u00da\u00db\7^\2\2\u00db\u00dc\7T\2\2\u00dc")
        buf.write("\u00dd\7k\2\2\u00dd\u00de\7i\2\2\u00de\u00df\7j\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7t\2\2\u00e2")
        buf.write("\u00e3\7t\2\2\u00e3\u00e4\7q\2\2\u00e4\u0104\7y\2\2\u00e5")
        buf.write("\u00e6\7^\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7q\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\u00ea\7i\2\2\u00ea\u00eb\7t\2\2\u00eb")
        buf.write("\u00ec\7k\2\2\u00ec\u00ed\7i\2\2\u00ed\u00ee\7j\2\2\u00ee")
        buf.write("\u00ef\7v\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1\7t\2\2\u00f1")
        buf.write("\u00f2\7t\2\2\u00f2\u00f3\7q\2\2\u00f3\u0104\7y\2\2\u00f4")
        buf.write("\u00f5\7^\2\2\u00f5\u00f6\7N\2\2\u00f6\u00f7\7q\2\2\u00f7")
        buf.write("\u00f8\7p\2\2\u00f8\u00f9\7i\2\2\u00f9\u00fa\7t\2\2\u00fa")
        buf.write("\u00fb\7k\2\2\u00fb\u00fc\7i\2\2\u00fc\u00fd\7j\2\2\u00fd")
        buf.write("\u00fe\7v\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7t\2\2\u0100")
        buf.write("\u0101\7t\2\2\u0101\u0102\7q\2\2\u0102\u0104\7y\2\2\u0103")
        buf.write("\u00cc\3\2\2\2\u0103\u00cf\3\2\2\2\u0103\u00da\3\2\2\2")
        buf.write("\u0103\u00e5\3\2\2\2\u0103\u00f4\3\2\2\2\u0104 \3\2\2")
        buf.write("\2\u0105\u0106\7^\2\2\u0106\u0107\7k\2\2\u0107\u0108\7")
        buf.write("p\2\2\u0108\u0109\7v\2\2\u0109\"\3\2\2\2\u010a\u010b\7")
        buf.write("^\2\2\u010b\u010c\7u\2\2\u010c\u010d\7w\2\2\u010d\u010e")
        buf.write("\7o\2\2\u010e$\3\2\2\2\u010f\u0110\7^\2\2\u0110\u0111")
        buf.write("\7r\2\2\u0111\u0112\7t\2\2\u0112\u0113\7q\2\2\u0113\u0114")
        buf.write("\7f\2\2\u0114&\3\2\2\2\u0115\u0117\5_\60\2\u0116\u0115")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("\u0119\7n\2\2\u0119\u011a\7q\2\2\u011a\u011b\7i\2\2\u011b")
        buf.write("(\3\2\2\2\u011c\u011e\5_\60\2\u011d\u011c\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\7n\2\2")
        buf.write("\u0120\u0121\7p\2\2\u0121*\3\2\2\2\u0122\u0124\5_\60\2")
        buf.write("\u0123\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125\3")
        buf.write("\2\2\2\u0125\u0126\7u\2\2\u0126\u0127\7k\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128,\3\2\2\2\u0129\u012b\5_\60\2\u012a\u0129")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012d\7e\2\2\u012d\u012e\7q\2\2\u012e\u012f\7u\2\2\u012f")
        buf.write(".\3\2\2\2\u0130\u0132\5_\60\2\u0131\u0130\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\7v\2\2")
        buf.write("\u0134\u0135\7c\2\2\u0135\u0136\7p\2\2\u0136\60\3\2\2")
        buf.write("\2\u0137\u0139\5_\60\2\u0138\u0137\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\7e\2\2\u013b")
        buf.write("\u013c\7u\2\2\u013c\u013d\7e\2\2\u013d\62\3\2\2\2\u013e")
        buf.write("\u0140\5_\60\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\u0142\7u\2\2\u0142\u0143\7")
        buf.write("g\2\2\u0143\u0144\7e\2\2\u0144\64\3\2\2\2\u0145\u0147")
        buf.write("\5_\60\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u0148\3\2\2\2\u0148\u0149\7e\2\2\u0149\u014a\7q\2\2\u014a")
        buf.write("\u014b\7v\2\2\u014b\66\3\2\2\2\u014c\u014e\5_\60\2\u014d")
        buf.write("\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write("\u014f\u0150\7c\2\2\u0150\u0151\7t\2\2\u0151\u0152\7e")
        buf.write("\2\2\u0152\u0153\7u\2\2\u0153\u0154\7k\2\2\u0154\u0155")
        buf.write("\7p\2\2\u01558\3\2\2\2\u0156\u0158\5_\60\2\u0157\u0156")
        buf.write("\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("\u015a\7c\2\2\u015a\u015b\7t\2\2\u015b\u015c\7e\2\2\u015c")
        buf.write("\u015d\7e\2\2\u015d\u015e\7q\2\2\u015e\u015f\7u\2\2\u015f")
        buf.write(":\3\2\2\2\u0160\u0162\5_\60\2\u0161\u0160\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\7c\2\2")
        buf.write("\u0164\u0165\7t\2\2\u0165\u0166\7e\2\2\u0166\u0167\7v")
        buf.write("\2\2\u0167\u0168\7c\2\2\u0168\u0169\7p\2\2\u0169<\3\2")
        buf.write("\2\2\u016a\u016c\5_\60\2\u016b\u016a\3\2\2\2\u016b\u016c")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\7c\2\2\u016e")
        buf.write("\u016f\7t\2\2\u016f\u0170\7e\2\2\u0170\u0171\7e\2\2\u0171")
        buf.write("\u0172\7u\2\2\u0172\u0173\7e\2\2\u0173>\3\2\2\2\u0174")
        buf.write("\u0176\5_\60\2\u0175\u0174\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177\u0178\7c\2\2\u0178\u0179\7")
        buf.write("t\2\2\u0179\u017a\7e\2\2\u017a\u017b\7u\2\2\u017b\u017c")
        buf.write("\7g\2\2\u017c\u017d\7e\2\2\u017d@\3\2\2\2\u017e\u0180")
        buf.write("\5_\60\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u0182\7c\2\2\u0182\u0183\7t\2\2\u0183")
        buf.write("\u0184\7e\2\2\u0184\u0185\7e\2\2\u0185\u0186\7q\2\2\u0186")
        buf.write("\u0187\7v\2\2\u0187B\3\2\2\2\u0188\u018a\5_\60\2\u0189")
        buf.write("\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u018c\7u\2\2\u018c\u018d\7k\2\2\u018d\u018e\7p")
        buf.write("\2\2\u018e\u018f\7j\2\2\u018fD\3\2\2\2\u0190\u0192\5_")
        buf.write("\60\2\u0191\u0190\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193\u0194\7e\2\2\u0194\u0195\7q\2\2\u0195\u0196")
        buf.write("\7u\2\2\u0196\u0197\7j\2\2\u0197F\3\2\2\2\u0198\u019a")
        buf.write("\5_\60\2\u0199\u0198\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u019c\7v\2\2\u019c\u019d\7c\2\2\u019d")
        buf.write("\u019e\7p\2\2\u019e\u019f\7j\2\2\u019fH\3\2\2\2\u01a0")
        buf.write("\u01a2\5_\60\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3\u01a4\7c\2\2\u01a4\u01a5\7")
        buf.write("t\2\2\u01a5\u01a6\7u\2\2\u01a6\u01a7\7k\2\2\u01a7\u01a8")
        buf.write("\7p\2\2\u01a8\u01a9\7j\2\2\u01a9J\3\2\2\2\u01aa\u01ac")
        buf.write("\5_\60\2\u01ab\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01ad\u01ae\7c\2\2\u01ae\u01af\7t\2\2\u01af")
        buf.write("\u01b0\7e\2\2\u01b0\u01b1\7q\2\2\u01b1\u01b2\7u\2\2\u01b2")
        buf.write("\u01b3\7j\2\2\u01b3L\3\2\2\2\u01b4\u01b6\5_\60\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b8\7c\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba\7v")
        buf.write("\2\2\u01ba\u01bb\7c\2\2\u01bb\u01bc\7p\2\2\u01bc\u01bd")
        buf.write("\7j\2\2\u01bdN\3\2\2\2\u01be\u01c0\5_\60\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("\u01c2\7u\2\2\u01c2\u01c3\7s\2\2\u01c3\u01c4\7t\2\2\u01c4")
        buf.write("\u01c5\7v\2\2\u01c5P\3\2\2\2\u01c6\u01c7\7^\2\2\u01c7")
        buf.write("\u01c8\7v\2\2\u01c8\u01c9\7k\2\2\u01c9\u01ca\7o\2\2\u01ca")
        buf.write("\u01cb\7g\2\2\u01cb\u01cc\7u\2\2\u01ccR\3\2\2\2\u01cd")
        buf.write("\u01ce\7^\2\2\u01ce\u01cf\7e\2\2\u01cf\u01d0\7f\2\2\u01d0")
        buf.write("\u01d1\7q\2\2\u01d1\u01d2\7v\2\2\u01d2T\3\2\2\2\u01d3")
        buf.write("\u01d4\7^\2\2\u01d4\u01d5\7f\2\2\u01d5\u01d6\7k\2\2\u01d6")
        buf.write("\u01d7\7x\2\2\u01d7V\3\2\2\2\u01d8\u01d9\7^\2\2\u01d9")
        buf.write("\u01da\7h\2\2\u01da\u01db\7t\2\2\u01db\u01dc\7c\2\2\u01dc")
        buf.write("\u01dd\7e\2\2\u01ddX\3\2\2\2\u01de\u01df\7a\2\2\u01df")
        buf.write("Z\3\2\2\2\u01e0\u01e1\7`\2\2\u01e1\\\3\2\2\2\u01e2\u01e3")
        buf.write("\7<\2\2\u01e3^\3\2\2\2\u01e4\u01e5\7^\2\2\u01e5`\3\2\2")
        buf.write("\2\u01e6\u01e7\t\2\2\2\u01e7b\3\2\2\2\u01e8\u01e9\t\3")
        buf.write("\2\2\u01e9d\3\2\2\2\u01ea\u01ec\7/\2\2\u01eb\u01ea\3\2")
        buf.write("\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01f0\3\2\2\2\u01ed\u01ef")
        buf.write("\5c\62\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f4\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f3\u01f5\7\60\2\2\u01f4\u01f3")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f7\3\2\2\2\u01f6")
        buf.write("\u01f8\5c\62\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2")
        buf.write("\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u0204\3")
        buf.write("\2\2\2\u01fb\u01fd\t\4\2\2\u01fc\u01fe\t\5\2\2\u01fd\u01fc")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0200\3\2\2\2\u01ff")
        buf.write("\u0201\5c\62\2\u0200\u01ff\3\2\2\2\u0201\u0202\3\2\2\2")
        buf.write("\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0205\3")
        buf.write("\2\2\2\u0204\u01fb\3\2\2\2\u0204\u0205\3\2\2\2\u0205f")
        buf.write("\3\2\2\2\u0206\u0208\5a\61\2\u0207\u0206\3\2\2\2\u0208")
        buf.write("\u0209\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a\3\2\2\2")
        buf.write("\u020ah\3\2\2\2\u020b\u020c\5e\63\2\u020c\u020d\5g\64")
        buf.write("\2\u020dj\3\2\2\2\u020e\u020f\7^\2\2\u020f\u0210\7k\2")
        buf.write("\2\u0210\u0211\7p\2\2\u0211\u0212\7h\2\2\u0212\u0213\7")
        buf.write("v\2\2\u0213\u0214\7{\2\2\u0214l\3\2\2\2\u0215\u0216\7")
        buf.write("?\2\2\u0216n\3\2\2\2\u0217\u0218\7>\2\2\u0218p\3\2\2\2")
        buf.write("\u0219\u021a\7^\2\2\u021a\u021b\7n\2\2\u021b\u021c\7g")
        buf.write("\2\2\u021c\u021d\7s\2\2\u021dr\3\2\2\2\u021e\u021f\7@")
        buf.write("\2\2\u021ft\3\2\2\2\u0220\u0221\7^\2\2\u0221\u0222\7i")
        buf.write("\2\2\u0222\u0223\7g\2\2\u0223\u0224\7s\2\2\u0224v\3\2")
        buf.write("\2\2\u0225\u0226\7#\2\2\u0226x\3\2\2\2\u0227\u0228\7^")
        buf.write("\2\2\u0228\u0229\7c\2\2\u0229\u022a\7n\2\2\u022a\u022b")
        buf.write("\7r\2\2\u022b\u022c\7j\2\2\u022c\u0234\7c\2\2\u022d\u022e")
        buf.write("\7^\2\2\u022e\u022f\7C\2\2\u022f\u0230\7n\2\2\u0230\u0231")
        buf.write("\7r\2\2\u0231\u0232\7j\2\2\u0232\u0234\7c\2\2\u0233\u0227")
        buf.write("\3\2\2\2\u0233\u022d\3\2\2\2\u0234z\3\2\2\2\u0235\u0236")
        buf.write("\7^\2\2\u0236\u0237\7d\2\2\u0237\u0238\7g\2\2\u0238\u0239")
        buf.write("\7v\2\2\u0239\u0240\7c\2\2\u023a\u023b\7^\2\2\u023b\u023c")
        buf.write("\7D\2\2\u023c\u023d\7g\2\2\u023d\u023e\7v\2\2\u023e\u0240")
        buf.write("\7c\2\2\u023f\u0235\3\2\2\2\u023f\u023a\3\2\2\2\u0240")
        buf.write("|\3\2\2\2\u0241\u0242\7^\2\2\u0242\u0243\7i\2\2\u0243")
        buf.write("\u0244\7c\2\2\u0244\u0245\7o\2\2\u0245\u0246\7o\2\2\u0246")
        buf.write("\u024e\7c\2\2\u0247\u0248\7^\2\2\u0248\u0249\7I\2\2\u0249")
        buf.write("\u024a\7c\2\2\u024a\u024b\7o\2\2\u024b\u024c\7o\2\2\u024c")
        buf.write("\u024e\7c\2\2\u024d\u0241\3\2\2\2\u024d\u0247\3\2\2\2")
        buf.write("\u024e~\3\2\2\2\u024f\u0250\7^\2\2\u0250\u0251\7f\2\2")
        buf.write("\u0251\u0252\7g\2\2\u0252\u0253\7n\2\2\u0253\u0254\7v")
        buf.write("\2\2\u0254\u025c\7c\2\2\u0255\u0256\7^\2\2\u0256\u0257")
        buf.write("\7F\2\2\u0257\u0258\7g\2\2\u0258\u0259\7n\2\2\u0259\u025a")
        buf.write("\7v\2\2\u025a\u025c\7c\2\2\u025b\u024f\3\2\2\2\u025b\u0255")
        buf.write("\3\2\2\2\u025c\u0080\3\2\2\2\u025d\u025e\7^\2\2\u025e")
        buf.write("\u025f\7g\2\2\u025f\u0260\7r\2\2\u0260\u0261\7u\2\2\u0261")
        buf.write("\u0262\7k\2\2\u0262\u0263\7n\2\2\u0263\u0264\7q\2\2\u0264")
        buf.write("\u026e\7p\2\2\u0265\u0266\7^\2\2\u0266\u0267\7G\2\2\u0267")
        buf.write("\u0268\7r\2\2\u0268\u0269\7u\2\2\u0269\u026a\7k\2\2\u026a")
        buf.write("\u026b\7n\2\2\u026b\u026c\7q\2\2\u026c\u026e\7p\2\2\u026d")
        buf.write("\u025d\3\2\2\2\u026d\u0265\3\2\2\2\u026e\u0082\3\2\2\2")
        buf.write("\u026f\u0270\7^\2\2\u0270\u0271\7|\2\2\u0271\u0272\7g")
        buf.write("\2\2\u0272\u0273\7v\2\2\u0273\u027a\7c\2\2\u0274\u0275")
        buf.write("\7^\2\2\u0275\u0276\7\\\2\2\u0276\u0277\7g\2\2\u0277\u0278")
        buf.write("\7v\2\2\u0278\u027a\7c\2\2\u0279\u026f\3\2\2\2\u0279\u0274")
        buf.write("\3\2\2\2\u027a\u0084\3\2\2\2\u027b\u027c\7^\2\2\u027c")
        buf.write("\u027d\7g\2\2\u027d\u027e\7v\2\2\u027e\u0284\7c\2\2\u027f")
        buf.write("\u0280\7^\2\2\u0280\u0281\7G\2\2\u0281\u0282\7v\2\2\u0282")
        buf.write("\u0284\7c\2\2\u0283\u027b\3\2\2\2\u0283\u027f\3\2\2\2")
        buf.write("\u0284\u0086\3\2\2\2\u0285\u0286\7^\2\2\u0286\u0287\7")
        buf.write("v\2\2\u0287\u0288\7j\2\2\u0288\u0289\7g\2\2\u0289\u028a")
        buf.write("\7v\2\2\u028a\u0292\7c\2\2\u028b\u028c\7^\2\2\u028c\u028d")
        buf.write("\7V\2\2\u028d\u028e\7j\2\2\u028e\u028f\7g\2\2\u028f\u0290")
        buf.write("\7v\2\2\u0290\u0292\7c\2\2\u0291\u0285\3\2\2\2\u0291\u028b")
        buf.write("\3\2\2\2\u0292\u0088\3\2\2\2\u0293\u0294\7^\2\2\u0294")
        buf.write("\u0295\7k\2\2\u0295\u0296\7q\2\2\u0296\u0297\7v\2\2\u0297")
        buf.write("\u029e\7c\2\2\u0298\u0299\7^\2\2\u0299\u029a\7K\2\2\u029a")
        buf.write("\u029b\7q\2\2\u029b\u029c\7v\2\2\u029c\u029e\7c\2\2\u029d")
        buf.write("\u0293\3\2\2\2\u029d\u0298\3\2\2\2\u029e\u008a\3\2\2\2")
        buf.write("\u029f\u02a0\7^\2\2\u02a0\u02a1\7m\2\2\u02a1\u02a2\7c")
        buf.write("\2\2\u02a2\u02a3\7r\2\2\u02a3\u02a4\7r\2\2\u02a4\u02ac")
        buf.write("\7c\2\2\u02a5\u02a6\7^\2\2\u02a6\u02a7\7M\2\2\u02a7\u02a8")
        buf.write("\7c\2\2\u02a8\u02a9\7r\2\2\u02a9\u02aa\7r\2\2\u02aa\u02ac")
        buf.write("\7c\2\2\u02ab\u029f\3\2\2\2\u02ab\u02a5\3\2\2\2\u02ac")
        buf.write("\u008c\3\2\2\2\u02ad\u02ae\7^\2\2\u02ae\u02af\7n\2\2\u02af")
        buf.write("\u02b0\7c\2\2\u02b0\u02b1\7o\2\2\u02b1\u02b2\7d\2\2\u02b2")
        buf.write("\u02b3\7f\2\2\u02b3\u02bc\7c\2\2\u02b4\u02b5\7^\2\2\u02b5")
        buf.write("\u02b6\7N\2\2\u02b6\u02b7\7c\2\2\u02b7\u02b8\7o\2\2\u02b8")
        buf.write("\u02b9\7d\2\2\u02b9\u02ba\7f\2\2\u02ba\u02bc\7c\2\2\u02bb")
        buf.write("\u02ad\3\2\2\2\u02bb\u02b4\3\2\2\2\u02bc\u008e\3\2\2\2")
        buf.write("\u02bd\u02be\7^\2\2\u02be\u02bf\7o\2\2\u02bf\u02c4\7w")
        buf.write("\2\2\u02c0\u02c1\7^\2\2\u02c1\u02c2\7O\2\2\u02c2\u02c4")
        buf.write("\7w\2\2\u02c3\u02bd\3\2\2\2\u02c3\u02c0\3\2\2\2\u02c4")
        buf.write("\u0090\3\2\2\2\u02c5\u02c6\7^\2\2\u02c6\u02c7\7p\2\2\u02c7")
        buf.write("\u02cc\7w\2\2\u02c8\u02c9\7^\2\2\u02c9\u02ca\7P\2\2\u02ca")
        buf.write("\u02cc\7w\2\2\u02cb\u02c5\3\2\2\2\u02cb\u02c8\3\2\2\2")
        buf.write("\u02cc\u0092\3\2\2\2\u02cd\u02ce\7^\2\2\u02ce\u02cf\7")
        buf.write("z\2\2\u02cf\u02d4\7k\2\2\u02d0\u02d1\7^\2\2\u02d1\u02d2")
        buf.write("\7Z\2\2\u02d2\u02d4\7k\2\2\u02d3\u02cd\3\2\2\2\u02d3\u02d0")
        buf.write("\3\2\2\2\u02d4\u0094\3\2\2\2\u02d5\u02d6\7^\2\2\u02d6")
        buf.write("\u02d7\7q\2\2\u02d7\u02d8\7o\2\2\u02d8\u02d9\7k\2\2\u02d9")
        buf.write("\u02da\7e\2\2\u02da\u02db\7t\2\2\u02db\u02dc\7q\2\2\u02dc")
        buf.write("\u02e6\7p\2\2\u02dd\u02de\7^\2\2\u02de\u02df\7Q\2\2\u02df")
        buf.write("\u02e0\7o\2\2\u02e0\u02e1\7k\2\2\u02e1\u02e2\7e\2\2\u02e2")
        buf.write("\u02e3\7t\2\2\u02e3\u02e4\7q\2\2\u02e4\u02e6\7p\2\2\u02e5")
        buf.write("\u02d5\3\2\2\2\u02e5\u02dd\3\2\2\2\u02e6\u0096\3\2\2\2")
        buf.write("\u02e7\u02e8\7^\2\2\u02e8\u02e9\7r\2\2\u02e9\u02ee\7k")
        buf.write("\2\2\u02ea\u02eb\7^\2\2\u02eb\u02ec\7R\2\2\u02ec\u02ee")
        buf.write("\7k\2\2\u02ed\u02e7\3\2\2\2\u02ed\u02ea\3\2\2\2\u02ee")
        buf.write("\u0098\3\2\2\2\u02ef\u02f0\7^\2\2\u02f0\u02f1\7t\2\2\u02f1")
        buf.write("\u02f2\7j\2\2\u02f2\u02f8\7q\2\2\u02f3\u02f4\7^\2\2\u02f4")
        buf.write("\u02f5\7T\2\2\u02f5\u02f6\7j\2\2\u02f6\u02f8\7q\2\2\u02f7")
        buf.write("\u02ef\3\2\2\2\u02f7\u02f3\3\2\2\2\u02f8\u009a\3\2\2\2")
        buf.write("\u02f9\u02fa\7^\2\2\u02fa\u02fb\7u\2\2\u02fb\u02fc\7k")
        buf.write("\2\2\u02fc\u02fd\7i\2\2\u02fd\u02fe\7o\2\2\u02fe\u0306")
        buf.write("\7c\2\2\u02ff\u0300\7^\2\2\u0300\u0301\7U\2\2\u0301\u0302")
        buf.write("\7k\2\2\u0302\u0303\7i\2\2\u0303\u0304\7o\2\2\u0304\u0306")
        buf.write("\7c\2\2\u0305\u02f9\3\2\2\2\u0305\u02ff\3\2\2\2\u0306")
        buf.write("\u009c\3\2\2\2\u0307\u0308\7^\2\2\u0308\u0309\7v\2\2\u0309")
        buf.write("\u030a\7c\2\2\u030a\u0310\7w\2\2\u030b\u030c\7^\2\2\u030c")
        buf.write("\u030d\7V\2\2\u030d\u030e\7c\2\2\u030e\u0310\7w\2\2\u030f")
        buf.write("\u0307\3\2\2\2\u030f\u030b\3\2\2\2\u0310\u009e\3\2\2\2")
        buf.write("\u0311\u0312\7^\2\2\u0312\u0313\7w\2\2\u0313\u0314\7r")
        buf.write("\2\2\u0314\u0315\7u\2\2\u0315\u0316\7k\2\2\u0316\u0317")
        buf.write("\7n\2\2\u0317\u0318\7q\2\2\u0318\u0322\7p\2\2\u0319\u031a")
        buf.write("\7^\2\2\u031a\u031b\7W\2\2\u031b\u031c\7r\2\2\u031c\u031d")
        buf.write("\7u\2\2\u031d\u031e\7k\2\2\u031e\u031f\7n\2\2\u031f\u0320")
        buf.write("\7q\2\2\u0320\u0322\7p\2\2\u0321\u0311\3\2\2\2\u0321\u0319")
        buf.write("\3\2\2\2\u0322\u00a0\3\2\2\2\u0323\u0324\7^\2\2\u0324")
        buf.write("\u0325\7r\2\2\u0325\u0326\7j\2\2\u0326\u032c\7k\2\2\u0327")
        buf.write("\u0328\7^\2\2\u0328\u0329\7R\2\2\u0329\u032a\7j\2\2\u032a")
        buf.write("\u032c\7k\2\2\u032b\u0323\3\2\2\2\u032b\u0327\3\2\2\2")
        buf.write("\u032c\u00a2\3\2\2\2\u032d\u032e\7^\2\2\u032e\u032f\7")
        buf.write("e\2\2\u032f\u0330\7j\2\2\u0330\u0336\7k\2\2\u0331\u0332")
        buf.write("\7^\2\2\u0332\u0333\7E\2\2\u0333\u0334\7j\2\2\u0334\u0336")
        buf.write("\7k\2\2\u0335\u032d\3\2\2\2\u0335\u0331\3\2\2\2\u0336")
        buf.write("\u00a4\3\2\2\2\u0337\u0338\7^\2\2\u0338\u0339\7r\2\2\u0339")
        buf.write("\u033a\7u\2\2\u033a\u0340\7k\2\2\u033b\u033c\7^\2\2\u033c")
        buf.write("\u033d\7R\2\2\u033d\u033e\7u\2\2\u033e\u0340\7k\2\2\u033f")
        buf.write("\u0337\3\2\2\2\u033f\u033b\3\2\2\2\u0340\u00a6\3\2\2\2")
        buf.write("\u0341\u0342\7^\2\2\u0342\u0343\7q\2\2\u0343\u0344\7o")
        buf.write("\2\2\u0344\u0345\7g\2\2\u0345\u0346\7i\2\2\u0346\u034e")
        buf.write("\7c\2\2\u0347\u0348\7^\2\2\u0348\u0349\7Q\2\2\u0349\u034a")
        buf.write("\7o\2\2\u034a\u034b\7g\2\2\u034b\u034c\7i\2\2\u034c\u034e")
        buf.write("\7c\2\2\u034d\u0341\3\2\2\2\u034d\u0347\3\2\2\2\u034e")
        buf.write("\u00a8\3\2\2\2\u034f\u0368\5y=\2\u0350\u0368\5{>\2\u0351")
        buf.write("\u0368\5}?\2\u0352\u0368\5\177@\2\u0353\u0368\5\u0081")
        buf.write("A\2\u0354\u0368\5\u0083B\2\u0355\u0368\5\u0085C\2\u0356")
        buf.write("\u0368\5\u0087D\2\u0357\u0368\5\u0089E\2\u0358\u0368\5")
        buf.write("\u008bF\2\u0359\u0368\5\u008dG\2\u035a\u0368\5\u008fH")
        buf.write("\2\u035b\u0368\5\u0091I\2\u035c\u0368\5\u0093J\2\u035d")
        buf.write("\u0368\5\u0095K\2\u035e\u0368\5\u0097L\2\u035f\u0368\5")
        buf.write("\u0099M\2\u0360\u0368\5\u009bN\2\u0361\u0368\5\u009dO")
        buf.write("\2\u0362\u0368\5\u009fP\2\u0363\u0368\5\u00a1Q\2\u0364")
        buf.write("\u0368\5\u00a3R\2\u0365\u0368\5\u00a5S\2\u0366\u0368\5")
        buf.write("\u00a7T\2\u0367\u034f\3\2\2\2\u0367\u0350\3\2\2\2\u0367")
        buf.write("\u0351\3\2\2\2\u0367\u0352\3\2\2\2\u0367\u0353\3\2\2\2")
        buf.write("\u0367\u0354\3\2\2\2\u0367\u0355\3\2\2\2\u0367\u0356\3")
        buf.write("\2\2\2\u0367\u0357\3\2\2\2\u0367\u0358\3\2\2\2\u0367\u0359")
        buf.write("\3\2\2\2\u0367\u035a\3\2\2\2\u0367\u035b\3\2\2\2\u0367")
        buf.write("\u035c\3\2\2\2\u0367\u035d\3\2\2\2\u0367\u035e\3\2\2\2")
        buf.write("\u0367\u035f\3\2\2\2\u0367\u0360\3\2\2\2\u0367\u0361\3")
        buf.write("\2\2\2\u0367\u0362\3\2\2\2\u0367\u0363\3\2\2\2\u0367\u0364")
        buf.write("\3\2\2\2\u0367\u0365\3\2\2\2\u0367\u0366\3\2\2\2\u0368")
        buf.write("\u00aa\3\2\2\2\u0369\u036b\t\6\2\2\u036a\u0369\3\2\2\2")
        buf.write("\u036b\u036c\3\2\2\2\u036c\u036a\3\2\2\2\u036c\u036d\3")
        buf.write("\2\2\2\u036d\u036e\3\2\2\2\u036e\u036f\bV\2\2\u036f\u00ac")
        buf.write("\3\2\2\2;\2\u0103\u0116\u011d\u0123\u012a\u0131\u0138")
        buf.write("\u013f\u0146\u014d\u0157\u0161\u016b\u0175\u017f\u0189")
        buf.write("\u0191\u0199\u01a1\u01ab\u01b5\u01bf\u01eb\u01f0\u01f4")
        buf.write("\u01f9\u01fd\u0202\u0204\u0209\u0233\u023f\u024d\u025b")
        buf.write("\u026d\u0279\u0283\u0291\u029d\u02ab\u02bb\u02c3\u02cb")
        buf.write("\u02d3\u02e5\u02ed\u02f7\u0305\u030f\u0321\u032b\u0335")
        buf.write("\u033f\u034d\u0367\u036c\3\b\2\2")
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


