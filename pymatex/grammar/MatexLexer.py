# Generated from .\pymatex\grammar\MatexLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0383\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u010c\n\20\3\21\3\21\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\5\24\u011f\n\24\3\24\3\24\3\24\3\24\3\25\5\25\u0126\n")
        buf.write("\25\3\25\3\25\3\25\3\26\5\26\u012c\n\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\5\27\u0133\n\27\3\27\3\27\3\27\3\27\3\30\5")
        buf.write("\30\u013a\n\30\3\30\3\30\3\30\3\30\3\31\5\31\u0141\n\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\5\32\u0148\n\32\3\32\3\32\3")
        buf.write("\32\3\32\3\33\5\33\u014f\n\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\5\34\u0156\n\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\35\5\35\u0160\n\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\5\36\u016a\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\37\5\37\u0174\n\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \5 \u017e\n \3 \3 \3 \3 \3 \3 \3 \3!\5!\u0188")
        buf.write("\n!\3!\3!\3!\3!\3!\3!\3!\3\"\5\"\u0192\n\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3#\5#\u019a\n#\3#\3#\3#\3#\3#\3$\5$\u01a2\n$")
        buf.write("\3$\3$\3$\3$\3$\3%\5%\u01aa\n%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("&\5&\u01b4\n&\3&\3&\3&\3&\3&\3&\3&\3\'\5\'\u01be\n\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\5(\u01c8\n(\3(\3(\3(\3(")
        buf.write("\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\7\63\u01f4\n\63\f\63\16\63\u01f7")
        buf.write("\13\63\3\63\5\63\u01fa\n\63\3\63\6\63\u01fd\n\63\r\63")
        buf.write("\16\63\u01fe\3\63\3\63\5\63\u0203\n\63\3\63\6\63\u0206")
        buf.write("\n\63\r\63\16\63\u0207\5\63\u020a\n\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\6\66\u0213\n\66\r\66\16\66\u0214")
        buf.write("\3\67\6\67\u0218\n\67\r\67\16\67\u0219\38\38\38\38\38")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3;\3;\3;\3<\3<\3=\3=\3=\3=\3")
        buf.write("=\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u0241\n")
        buf.write("?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u024d\n@\3A\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u025b\nA\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\5B\u0269\nB\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write("C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u027b\nC\3D\3D\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\5D\u0287\nD\3E\3E\3E\3E\3E\3E\3E\3E\5E\u0291")
        buf.write("\nE\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u029f\nF\3")
        buf.write("G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u02ab\nG\3H\3H\3H\3H\3")
        buf.write("H\3H\3H\3H\3H\3H\3H\3H\5H\u02b9\nH\3I\3I\3I\3I\3I\3I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\5I\u02c9\nI\3J\3J\3J\3J\3J\3J\5")
        buf.write("J\u02d1\nJ\3K\3K\3K\3K\3K\3K\5K\u02d9\nK\3L\3L\3L\3L\3")
        buf.write("L\3L\5L\u02e1\nL\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\5M\u02f3\nM\3N\3N\3N\3N\3N\3N\5N\u02fb\nN\3")
        buf.write("O\3O\3O\3O\3O\3O\3O\3O\5O\u0305\nO\3P\3P\3P\3P\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\5P\u0313\nP\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5")
        buf.write("Q\u031d\nQ\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3")
        buf.write("R\3R\5R\u032f\nR\3S\3S\3S\3S\3S\3S\3S\3S\5S\u0339\nS\3")
        buf.write("T\3T\3T\3T\3T\3T\3T\3T\5T\u0343\nT\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\5U\u034d\nU\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5")
        buf.write("V\u035b\nV\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3")
        buf.write("W\3W\3W\3W\3W\3W\3W\3W\3W\3W\5W\u0375\nW\3X\3X\3X\3Y\3")
        buf.write("Y\3Y\3Z\6Z\u037e\nZ\rZ\16Z\u037f\3Z\3Z\2\2[\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\2c\2e\62g\63i\64k\65m\66o\67q8s9u:w;y<{")
        buf.write("=}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b")
        buf.write("\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099")
        buf.write("\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9\2\u00ab\2\u00ad>\u00af?\u00b1@\u00b3A\3\2\7\4")
        buf.write("\2C\\c|\3\2\62;\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2\u03b9")
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
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u00ad\3\2")
        buf.write("\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\3")
        buf.write("\u00b5\3\2\2\2\5\u00b7\3\2\2\2\7\u00b9\3\2\2\2\t\u00bb")
        buf.write("\3\2\2\2\13\u00bd\3\2\2\2\r\u00bf\3\2\2\2\17\u00c1\3\2")
        buf.write("\2\2\21\u00c3\3\2\2\2\23\u00c5\3\2\2\2\25\u00c7\3\2\2")
        buf.write("\2\27\u00c9\3\2\2\2\31\u00cb\3\2\2\2\33\u00cd\3\2\2\2")
        buf.write("\35\u00cf\3\2\2\2\37\u010b\3\2\2\2!\u010d\3\2\2\2#\u0112")
        buf.write("\3\2\2\2%\u0117\3\2\2\2\'\u011e\3\2\2\2)\u0125\3\2\2\2")
        buf.write("+\u012b\3\2\2\2-\u0132\3\2\2\2/\u0139\3\2\2\2\61\u0140")
        buf.write("\3\2\2\2\63\u0147\3\2\2\2\65\u014e\3\2\2\2\67\u0155\3")
        buf.write("\2\2\29\u015f\3\2\2\2;\u0169\3\2\2\2=\u0173\3\2\2\2?\u017d")
        buf.write("\3\2\2\2A\u0187\3\2\2\2C\u0191\3\2\2\2E\u0199\3\2\2\2")
        buf.write("G\u01a1\3\2\2\2I\u01a9\3\2\2\2K\u01b3\3\2\2\2M\u01bd\3")
        buf.write("\2\2\2O\u01c7\3\2\2\2Q\u01ce\3\2\2\2S\u01d5\3\2\2\2U\u01db")
        buf.write("\3\2\2\2W\u01e0\3\2\2\2Y\u01e6\3\2\2\2[\u01e8\3\2\2\2")
        buf.write("]\u01ea\3\2\2\2_\u01ec\3\2\2\2a\u01ee\3\2\2\2c\u01f0\3")
        buf.write("\2\2\2e\u01f5\3\2\2\2g\u020b\3\2\2\2i\u020e\3\2\2\2k\u0210")
        buf.write("\3\2\2\2m\u0217\3\2\2\2o\u021b\3\2\2\2q\u0222\3\2\2\2")
        buf.write("s\u0224\3\2\2\2u\u0226\3\2\2\2w\u022b\3\2\2\2y\u022d\3")
        buf.write("\2\2\2{\u0232\3\2\2\2}\u0240\3\2\2\2\177\u024c\3\2\2\2")
        buf.write("\u0081\u025a\3\2\2\2\u0083\u0268\3\2\2\2\u0085\u027a\3")
        buf.write("\2\2\2\u0087\u0286\3\2\2\2\u0089\u0290\3\2\2\2\u008b\u029e")
        buf.write("\3\2\2\2\u008d\u02aa\3\2\2\2\u008f\u02b8\3\2\2\2\u0091")
        buf.write("\u02c8\3\2\2\2\u0093\u02d0\3\2\2\2\u0095\u02d8\3\2\2\2")
        buf.write("\u0097\u02e0\3\2\2\2\u0099\u02f2\3\2\2\2\u009b\u02fa\3")
        buf.write("\2\2\2\u009d\u0304\3\2\2\2\u009f\u0312\3\2\2\2\u00a1\u031c")
        buf.write("\3\2\2\2\u00a3\u032e\3\2\2\2\u00a5\u0338\3\2\2\2\u00a7")
        buf.write("\u0342\3\2\2\2\u00a9\u034c\3\2\2\2\u00ab\u035a\3\2\2\2")
        buf.write("\u00ad\u0374\3\2\2\2\u00af\u0376\3\2\2\2\u00b1\u0379\3")
        buf.write("\2\2\2\u00b3\u037d\3\2\2\2\u00b5\u00b6\7-\2\2\u00b6\4")
        buf.write("\3\2\2\2\u00b7\u00b8\7/\2\2\u00b8\6\3\2\2\2\u00b9\u00ba")
        buf.write("\7,\2\2\u00ba\b\3\2\2\2\u00bb\u00bc\7\61\2\2\u00bc\n\3")
        buf.write("\2\2\2\u00bd\u00be\7*\2\2\u00be\f\3\2\2\2\u00bf\u00c0")
        buf.write("\7+\2\2\u00c0\16\3\2\2\2\u00c1\u00c2\7}\2\2\u00c2\20\3")
        buf.write("\2\2\2\u00c3\u00c4\7\177\2\2\u00c4\22\3\2\2\2\u00c5\u00c6")
        buf.write("\7]\2\2\u00c6\24\3\2\2\2\u00c7\u00c8\7_\2\2\u00c8\26\3")
        buf.write("\2\2\2\u00c9\u00ca\7.\2\2\u00ca\30\3\2\2\2\u00cb\u00cc")
        buf.write("\7\60\2\2\u00cc\32\3\2\2\2\u00cd\u00ce\7~\2\2\u00ce\34")
        buf.write("\3\2\2\2\u00cf\u00d0\7^\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7o\2\2\u00d3\36\3\2\2\2\u00d4\u00d5")
        buf.write("\7^\2\2\u00d5\u00d6\7v\2\2\u00d6\u010c\7q\2\2\u00d7\u00d8")
        buf.write("\7^\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7k\2\2\u00da\u00db")
        buf.write("\7i\2\2\u00db\u00dc\7j\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\u010c\7y\2\2\u00e2\u00e3\7^\2\2\u00e3\u00e4")
        buf.write("\7T\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7i\2\2\u00e6\u00e7")
        buf.write("\7j\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7q\2\2\u00ec\u010c")
        buf.write("\7y\2\2\u00ed\u00ee\7^\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2\7i\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7i\2\2\u00f5\u00f6")
        buf.write("\7j\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7q\2\2\u00fb\u010c")
        buf.write("\7y\2\2\u00fc\u00fd\7^\2\2\u00fd\u00fe\7N\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7i\2\2\u0101\u0102")
        buf.write("\7t\2\2\u0102\u0103\7k\2\2\u0103\u0104\7i\2\2\u0104\u0105")
        buf.write("\7j\2\2\u0105\u0106\7v\2\2\u0106\u0107\7c\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108\u0109\7t\2\2\u0109\u010a\7q\2\2\u010a\u010c")
        buf.write("\7y\2\2\u010b\u00d4\3\2\2\2\u010b\u00d7\3\2\2\2\u010b")
        buf.write("\u00e2\3\2\2\2\u010b\u00ed\3\2\2\2\u010b\u00fc\3\2\2\2")
        buf.write("\u010c \3\2\2\2\u010d\u010e\7^\2\2\u010e\u010f\7k\2\2")
        buf.write("\u010f\u0110\7p\2\2\u0110\u0111\7v\2\2\u0111\"\3\2\2\2")
        buf.write("\u0112\u0113\7^\2\2\u0113\u0114\7u\2\2\u0114\u0115\7w")
        buf.write("\2\2\u0115\u0116\7o\2\2\u0116$\3\2\2\2\u0117\u0118\7^")
        buf.write("\2\2\u0118\u0119\7r\2\2\u0119\u011a\7t\2\2\u011a\u011b")
        buf.write("\7q\2\2\u011b\u011c\7f\2\2\u011c&\3\2\2\2\u011d\u011f")
        buf.write("\5_\60\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0121\7n\2\2\u0121\u0122\7q\2\2\u0122")
        buf.write("\u0123\7i\2\2\u0123(\3\2\2\2\u0124\u0126\5_\60\2\u0125")
        buf.write("\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127\u0128\7n\2\2\u0128\u0129\7p\2\2\u0129*\3\2\2\2")
        buf.write("\u012a\u012c\5_\60\2\u012b\u012a\3\2\2\2\u012b\u012c\3")
        buf.write("\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\7u\2\2\u012e\u012f")
        buf.write("\7k\2\2\u012f\u0130\7p\2\2\u0130,\3\2\2\2\u0131\u0133")
        buf.write("\5_\60\2\u0132\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134\u0135\7e\2\2\u0135\u0136\7q\2\2\u0136")
        buf.write("\u0137\7u\2\2\u0137.\3\2\2\2\u0138\u013a\5_\60\2\u0139")
        buf.write("\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u013c\7v\2\2\u013c\u013d\7c\2\2\u013d\u013e\7p")
        buf.write("\2\2\u013e\60\3\2\2\2\u013f\u0141\5_\60\2\u0140\u013f")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142")
        buf.write("\u0143\7e\2\2\u0143\u0144\7u\2\2\u0144\u0145\7e\2\2\u0145")
        buf.write("\62\3\2\2\2\u0146\u0148\5_\60\2\u0147\u0146\3\2\2\2\u0147")
        buf.write("\u0148\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\7u\2\2")
        buf.write("\u014a\u014b\7g\2\2\u014b\u014c\7e\2\2\u014c\64\3\2\2")
        buf.write("\2\u014d\u014f\5_\60\2\u014e\u014d\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\7e\2\2\u0151")
        buf.write("\u0152\7q\2\2\u0152\u0153\7v\2\2\u0153\66\3\2\2\2\u0154")
        buf.write("\u0156\5_\60\2\u0155\u0154\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u0157\u0158\7c\2\2\u0158\u0159\7")
        buf.write("t\2\2\u0159\u015a\7e\2\2\u015a\u015b\7u\2\2\u015b\u015c")
        buf.write("\7k\2\2\u015c\u015d\7p\2\2\u015d8\3\2\2\2\u015e\u0160")
        buf.write("\5_\60\2\u015f\u015e\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0162\7c\2\2\u0162\u0163\7t\2\2\u0163")
        buf.write("\u0164\7e\2\2\u0164\u0165\7e\2\2\u0165\u0166\7q\2\2\u0166")
        buf.write("\u0167\7u\2\2\u0167:\3\2\2\2\u0168\u016a\5_\60\2\u0169")
        buf.write("\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016c\7c\2\2\u016c\u016d\7t\2\2\u016d\u016e\7e")
        buf.write("\2\2\u016e\u016f\7v\2\2\u016f\u0170\7c\2\2\u0170\u0171")
        buf.write("\7p\2\2\u0171<\3\2\2\2\u0172\u0174\5_\60\2\u0173\u0172")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("\u0176\7c\2\2\u0176\u0177\7t\2\2\u0177\u0178\7e\2\2\u0178")
        buf.write("\u0179\7e\2\2\u0179\u017a\7u\2\2\u017a\u017b\7e\2\2\u017b")
        buf.write(">\3\2\2\2\u017c\u017e\5_\60\2\u017d\u017c\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\7c\2\2")
        buf.write("\u0180\u0181\7t\2\2\u0181\u0182\7e\2\2\u0182\u0183\7u")
        buf.write("\2\2\u0183\u0184\7g\2\2\u0184\u0185\7e\2\2\u0185@\3\2")
        buf.write("\2\2\u0186\u0188\5_\60\2\u0187\u0186\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\7c\2\2\u018a")
        buf.write("\u018b\7t\2\2\u018b\u018c\7e\2\2\u018c\u018d\7e\2\2\u018d")
        buf.write("\u018e\7q\2\2\u018e\u018f\7v\2\2\u018fB\3\2\2\2\u0190")
        buf.write("\u0192\5_\60\2\u0191\u0190\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193\u0194\7u\2\2\u0194\u0195\7")
        buf.write("k\2\2\u0195\u0196\7p\2\2\u0196\u0197\7j\2\2\u0197D\3\2")
        buf.write("\2\2\u0198\u019a\5_\60\2\u0199\u0198\3\2\2\2\u0199\u019a")
        buf.write("\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\7e\2\2\u019c")
        buf.write("\u019d\7q\2\2\u019d\u019e\7u\2\2\u019e\u019f\7j\2\2\u019f")
        buf.write("F\3\2\2\2\u01a0\u01a2\5_\60\2\u01a1\u01a0\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\7v\2\2")
        buf.write("\u01a4\u01a5\7c\2\2\u01a5\u01a6\7p\2\2\u01a6\u01a7\7j")
        buf.write("\2\2\u01a7H\3\2\2\2\u01a8\u01aa\5_\60\2\u01a9\u01a8\3")
        buf.write("\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac")
        buf.write("\7c\2\2\u01ac\u01ad\7t\2\2\u01ad\u01ae\7u\2\2\u01ae\u01af")
        buf.write("\7k\2\2\u01af\u01b0\7p\2\2\u01b0\u01b1\7j\2\2\u01b1J\3")
        buf.write("\2\2\2\u01b2\u01b4\5_\60\2\u01b3\u01b2\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\7c\2\2\u01b6")
        buf.write("\u01b7\7t\2\2\u01b7\u01b8\7e\2\2\u01b8\u01b9\7q\2\2\u01b9")
        buf.write("\u01ba\7u\2\2\u01ba\u01bb\7j\2\2\u01bbL\3\2\2\2\u01bc")
        buf.write("\u01be\5_\60\2\u01bd\u01bc\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c0\7c\2\2\u01c0\u01c1\7")
        buf.write("t\2\2\u01c1\u01c2\7v\2\2\u01c2\u01c3\7c\2\2\u01c3\u01c4")
        buf.write("\7p\2\2\u01c4\u01c5\7j\2\2\u01c5N\3\2\2\2\u01c6\u01c8")
        buf.write("\5_\60\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u01ca\7u\2\2\u01ca\u01cb\7s\2\2\u01cb")
        buf.write("\u01cc\7t\2\2\u01cc\u01cd\7v\2\2\u01cdP\3\2\2\2\u01ce")
        buf.write("\u01cf\7^\2\2\u01cf\u01d0\7v\2\2\u01d0\u01d1\7k\2\2\u01d1")
        buf.write("\u01d2\7o\2\2\u01d2\u01d3\7g\2\2\u01d3\u01d4\7u\2\2\u01d4")
        buf.write("R\3\2\2\2\u01d5\u01d6\7^\2\2\u01d6\u01d7\7e\2\2\u01d7")
        buf.write("\u01d8\7f\2\2\u01d8\u01d9\7q\2\2\u01d9\u01da\7v\2\2\u01da")
        buf.write("T\3\2\2\2\u01db\u01dc\7^\2\2\u01dc\u01dd\7f\2\2\u01dd")
        buf.write("\u01de\7k\2\2\u01de\u01df\7x\2\2\u01dfV\3\2\2\2\u01e0")
        buf.write("\u01e1\7^\2\2\u01e1\u01e2\7h\2\2\u01e2\u01e3\7t\2\2\u01e3")
        buf.write("\u01e4\7c\2\2\u01e4\u01e5\7e\2\2\u01e5X\3\2\2\2\u01e6")
        buf.write("\u01e7\7a\2\2\u01e7Z\3\2\2\2\u01e8\u01e9\7`\2\2\u01e9")
        buf.write("\\\3\2\2\2\u01ea\u01eb\7<\2\2\u01eb^\3\2\2\2\u01ec\u01ed")
        buf.write("\7^\2\2\u01ed`\3\2\2\2\u01ee\u01ef\t\2\2\2\u01efb\3\2")
        buf.write("\2\2\u01f0\u01f1\t\3\2\2\u01f1d\3\2\2\2\u01f2\u01f4\5")
        buf.write("c\62\2\u01f3\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f8\u01fa\7\60\2\2\u01f9\u01f8\3\2\2")
        buf.write("\2\u01f9\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2\u01fb\u01fd")
        buf.write("\5c\62\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0209\3\2\2\2")
        buf.write("\u0200\u0202\t\4\2\2\u0201\u0203\t\5\2\2\u0202\u0201\3")
        buf.write("\2\2\2\u0202\u0203\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u0206")
        buf.write("\5c\62\2\u0205\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u020a\3\2\2\2")
        buf.write("\u0209\u0200\3\2\2\2\u0209\u020a\3\2\2\2\u020af\3\2\2")
        buf.write("\2\u020b\u020c\7f\2\2\u020c\u020d\5a\61\2\u020dh\3\2\2")
        buf.write("\2\u020e\u020f\5a\61\2\u020fj\3\2\2\2\u0210\u0212\5e\63")
        buf.write("\2\u0211\u0213\5i\65\2\u0212\u0211\3\2\2\2\u0213\u0214")
        buf.write("\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215")
        buf.write("l\3\2\2\2\u0216\u0218\5i\65\2\u0217\u0216\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2")
        buf.write("\u021an\3\2\2\2\u021b\u021c\7^\2\2\u021c\u021d\7k\2\2")
        buf.write("\u021d\u021e\7p\2\2\u021e\u021f\7h\2\2\u021f\u0220\7v")
        buf.write("\2\2\u0220\u0221\7{\2\2\u0221p\3\2\2\2\u0222\u0223\7?")
        buf.write("\2\2\u0223r\3\2\2\2\u0224\u0225\7>\2\2\u0225t\3\2\2\2")
        buf.write("\u0226\u0227\7^\2\2\u0227\u0228\7n\2\2\u0228\u0229\7g")
        buf.write("\2\2\u0229\u022a\7s\2\2\u022av\3\2\2\2\u022b\u022c\7@")
        buf.write("\2\2\u022cx\3\2\2\2\u022d\u022e\7^\2\2\u022e\u022f\7i")
        buf.write("\2\2\u022f\u0230\7g\2\2\u0230\u0231\7s\2\2\u0231z\3\2")
        buf.write("\2\2\u0232\u0233\7#\2\2\u0233|\3\2\2\2\u0234\u0235\7^")
        buf.write("\2\2\u0235\u0236\7c\2\2\u0236\u0237\7n\2\2\u0237\u0238")
        buf.write("\7r\2\2\u0238\u0239\7j\2\2\u0239\u0241\7c\2\2\u023a\u023b")
        buf.write("\7^\2\2\u023b\u023c\7C\2\2\u023c\u023d\7n\2\2\u023d\u023e")
        buf.write("\7r\2\2\u023e\u023f\7j\2\2\u023f\u0241\7c\2\2\u0240\u0234")
        buf.write("\3\2\2\2\u0240\u023a\3\2\2\2\u0241~\3\2\2\2\u0242\u0243")
        buf.write("\7^\2\2\u0243\u0244\7d\2\2\u0244\u0245\7g\2\2\u0245\u0246")
        buf.write("\7v\2\2\u0246\u024d\7c\2\2\u0247\u0248\7^\2\2\u0248\u0249")
        buf.write("\7D\2\2\u0249\u024a\7g\2\2\u024a\u024b\7v\2\2\u024b\u024d")
        buf.write("\7c\2\2\u024c\u0242\3\2\2\2\u024c\u0247\3\2\2\2\u024d")
        buf.write("\u0080\3\2\2\2\u024e\u024f\7^\2\2\u024f\u0250\7i\2\2\u0250")
        buf.write("\u0251\7c\2\2\u0251\u0252\7o\2\2\u0252\u0253\7o\2\2\u0253")
        buf.write("\u025b\7c\2\2\u0254\u0255\7^\2\2\u0255\u0256\7I\2\2\u0256")
        buf.write("\u0257\7c\2\2\u0257\u0258\7o\2\2\u0258\u0259\7o\2\2\u0259")
        buf.write("\u025b\7c\2\2\u025a\u024e\3\2\2\2\u025a\u0254\3\2\2\2")
        buf.write("\u025b\u0082\3\2\2\2\u025c\u025d\7^\2\2\u025d\u025e\7")
        buf.write("f\2\2\u025e\u025f\7g\2\2\u025f\u0260\7n\2\2\u0260\u0261")
        buf.write("\7v\2\2\u0261\u0269\7c\2\2\u0262\u0263\7^\2\2\u0263\u0264")
        buf.write("\7F\2\2\u0264\u0265\7g\2\2\u0265\u0266\7n\2\2\u0266\u0267")
        buf.write("\7v\2\2\u0267\u0269\7c\2\2\u0268\u025c\3\2\2\2\u0268\u0262")
        buf.write("\3\2\2\2\u0269\u0084\3\2\2\2\u026a\u026b\7^\2\2\u026b")
        buf.write("\u026c\7g\2\2\u026c\u026d\7r\2\2\u026d\u026e\7u\2\2\u026e")
        buf.write("\u026f\7k\2\2\u026f\u0270\7n\2\2\u0270\u0271\7q\2\2\u0271")
        buf.write("\u027b\7p\2\2\u0272\u0273\7^\2\2\u0273\u0274\7G\2\2\u0274")
        buf.write("\u0275\7r\2\2\u0275\u0276\7u\2\2\u0276\u0277\7k\2\2\u0277")
        buf.write("\u0278\7n\2\2\u0278\u0279\7q\2\2\u0279\u027b\7p\2\2\u027a")
        buf.write("\u026a\3\2\2\2\u027a\u0272\3\2\2\2\u027b\u0086\3\2\2\2")
        buf.write("\u027c\u027d\7^\2\2\u027d\u027e\7|\2\2\u027e\u027f\7g")
        buf.write("\2\2\u027f\u0280\7v\2\2\u0280\u0287\7c\2\2\u0281\u0282")
        buf.write("\7^\2\2\u0282\u0283\7\\\2\2\u0283\u0284\7g\2\2\u0284\u0285")
        buf.write("\7v\2\2\u0285\u0287\7c\2\2\u0286\u027c\3\2\2\2\u0286\u0281")
        buf.write("\3\2\2\2\u0287\u0088\3\2\2\2\u0288\u0289\7^\2\2\u0289")
        buf.write("\u028a\7g\2\2\u028a\u028b\7v\2\2\u028b\u0291\7c\2\2\u028c")
        buf.write("\u028d\7^\2\2\u028d\u028e\7G\2\2\u028e\u028f\7v\2\2\u028f")
        buf.write("\u0291\7c\2\2\u0290\u0288\3\2\2\2\u0290\u028c\3\2\2\2")
        buf.write("\u0291\u008a\3\2\2\2\u0292\u0293\7^\2\2\u0293\u0294\7")
        buf.write("v\2\2\u0294\u0295\7j\2\2\u0295\u0296\7g\2\2\u0296\u0297")
        buf.write("\7v\2\2\u0297\u029f\7c\2\2\u0298\u0299\7^\2\2\u0299\u029a")
        buf.write("\7V\2\2\u029a\u029b\7j\2\2\u029b\u029c\7g\2\2\u029c\u029d")
        buf.write("\7v\2\2\u029d\u029f\7c\2\2\u029e\u0292\3\2\2\2\u029e\u0298")
        buf.write("\3\2\2\2\u029f\u008c\3\2\2\2\u02a0\u02a1\7^\2\2\u02a1")
        buf.write("\u02a2\7k\2\2\u02a2\u02a3\7q\2\2\u02a3\u02a4\7v\2\2\u02a4")
        buf.write("\u02ab\7c\2\2\u02a5\u02a6\7^\2\2\u02a6\u02a7\7K\2\2\u02a7")
        buf.write("\u02a8\7q\2\2\u02a8\u02a9\7v\2\2\u02a9\u02ab\7c\2\2\u02aa")
        buf.write("\u02a0\3\2\2\2\u02aa\u02a5\3\2\2\2\u02ab\u008e\3\2\2\2")
        buf.write("\u02ac\u02ad\7^\2\2\u02ad\u02ae\7m\2\2\u02ae\u02af\7c")
        buf.write("\2\2\u02af\u02b0\7r\2\2\u02b0\u02b1\7r\2\2\u02b1\u02b9")
        buf.write("\7c\2\2\u02b2\u02b3\7^\2\2\u02b3\u02b4\7M\2\2\u02b4\u02b5")
        buf.write("\7c\2\2\u02b5\u02b6\7r\2\2\u02b6\u02b7\7r\2\2\u02b7\u02b9")
        buf.write("\7c\2\2\u02b8\u02ac\3\2\2\2\u02b8\u02b2\3\2\2\2\u02b9")
        buf.write("\u0090\3\2\2\2\u02ba\u02bb\7^\2\2\u02bb\u02bc\7n\2\2\u02bc")
        buf.write("\u02bd\7c\2\2\u02bd\u02be\7o\2\2\u02be\u02bf\7d\2\2\u02bf")
        buf.write("\u02c0\7f\2\2\u02c0\u02c9\7c\2\2\u02c1\u02c2\7^\2\2\u02c2")
        buf.write("\u02c3\7N\2\2\u02c3\u02c4\7c\2\2\u02c4\u02c5\7o\2\2\u02c5")
        buf.write("\u02c6\7d\2\2\u02c6\u02c7\7f\2\2\u02c7\u02c9\7c\2\2\u02c8")
        buf.write("\u02ba\3\2\2\2\u02c8\u02c1\3\2\2\2\u02c9\u0092\3\2\2\2")
        buf.write("\u02ca\u02cb\7^\2\2\u02cb\u02cc\7o\2\2\u02cc\u02d1\7w")
        buf.write("\2\2\u02cd\u02ce\7^\2\2\u02ce\u02cf\7O\2\2\u02cf\u02d1")
        buf.write("\7w\2\2\u02d0\u02ca\3\2\2\2\u02d0\u02cd\3\2\2\2\u02d1")
        buf.write("\u0094\3\2\2\2\u02d2\u02d3\7^\2\2\u02d3\u02d4\7p\2\2\u02d4")
        buf.write("\u02d9\7w\2\2\u02d5\u02d6\7^\2\2\u02d6\u02d7\7P\2\2\u02d7")
        buf.write("\u02d9\7w\2\2\u02d8\u02d2\3\2\2\2\u02d8\u02d5\3\2\2\2")
        buf.write("\u02d9\u0096\3\2\2\2\u02da\u02db\7^\2\2\u02db\u02dc\7")
        buf.write("z\2\2\u02dc\u02e1\7k\2\2\u02dd\u02de\7^\2\2\u02de\u02df")
        buf.write("\7Z\2\2\u02df\u02e1\7k\2\2\u02e0\u02da\3\2\2\2\u02e0\u02dd")
        buf.write("\3\2\2\2\u02e1\u0098\3\2\2\2\u02e2\u02e3\7^\2\2\u02e3")
        buf.write("\u02e4\7q\2\2\u02e4\u02e5\7o\2\2\u02e5\u02e6\7k\2\2\u02e6")
        buf.write("\u02e7\7e\2\2\u02e7\u02e8\7t\2\2\u02e8\u02e9\7q\2\2\u02e9")
        buf.write("\u02f3\7p\2\2\u02ea\u02eb\7^\2\2\u02eb\u02ec\7Q\2\2\u02ec")
        buf.write("\u02ed\7o\2\2\u02ed\u02ee\7k\2\2\u02ee\u02ef\7e\2\2\u02ef")
        buf.write("\u02f0\7t\2\2\u02f0\u02f1\7q\2\2\u02f1\u02f3\7p\2\2\u02f2")
        buf.write("\u02e2\3\2\2\2\u02f2\u02ea\3\2\2\2\u02f3\u009a\3\2\2\2")
        buf.write("\u02f4\u02f5\7^\2\2\u02f5\u02f6\7r\2\2\u02f6\u02fb\7k")
        buf.write("\2\2\u02f7\u02f8\7^\2\2\u02f8\u02f9\7R\2\2\u02f9\u02fb")
        buf.write("\7k\2\2\u02fa\u02f4\3\2\2\2\u02fa\u02f7\3\2\2\2\u02fb")
        buf.write("\u009c\3\2\2\2\u02fc\u02fd\7^\2\2\u02fd\u02fe\7t\2\2\u02fe")
        buf.write("\u02ff\7j\2\2\u02ff\u0305\7q\2\2\u0300\u0301\7^\2\2\u0301")
        buf.write("\u0302\7T\2\2\u0302\u0303\7j\2\2\u0303\u0305\7q\2\2\u0304")
        buf.write("\u02fc\3\2\2\2\u0304\u0300\3\2\2\2\u0305\u009e\3\2\2\2")
        buf.write("\u0306\u0307\7^\2\2\u0307\u0308\7u\2\2\u0308\u0309\7k")
        buf.write("\2\2\u0309\u030a\7i\2\2\u030a\u030b\7o\2\2\u030b\u0313")
        buf.write("\7c\2\2\u030c\u030d\7^\2\2\u030d\u030e\7U\2\2\u030e\u030f")
        buf.write("\7k\2\2\u030f\u0310\7i\2\2\u0310\u0311\7o\2\2\u0311\u0313")
        buf.write("\7c\2\2\u0312\u0306\3\2\2\2\u0312\u030c\3\2\2\2\u0313")
        buf.write("\u00a0\3\2\2\2\u0314\u0315\7^\2\2\u0315\u0316\7v\2\2\u0316")
        buf.write("\u0317\7c\2\2\u0317\u031d\7w\2\2\u0318\u0319\7^\2\2\u0319")
        buf.write("\u031a\7V\2\2\u031a\u031b\7c\2\2\u031b\u031d\7w\2\2\u031c")
        buf.write("\u0314\3\2\2\2\u031c\u0318\3\2\2\2\u031d\u00a2\3\2\2\2")
        buf.write("\u031e\u031f\7^\2\2\u031f\u0320\7w\2\2\u0320\u0321\7r")
        buf.write("\2\2\u0321\u0322\7u\2\2\u0322\u0323\7k\2\2\u0323\u0324")
        buf.write("\7n\2\2\u0324\u0325\7q\2\2\u0325\u032f\7p\2\2\u0326\u0327")
        buf.write("\7^\2\2\u0327\u0328\7W\2\2\u0328\u0329\7r\2\2\u0329\u032a")
        buf.write("\7u\2\2\u032a\u032b\7k\2\2\u032b\u032c\7n\2\2\u032c\u032d")
        buf.write("\7q\2\2\u032d\u032f\7p\2\2\u032e\u031e\3\2\2\2\u032e\u0326")
        buf.write("\3\2\2\2\u032f\u00a4\3\2\2\2\u0330\u0331\7^\2\2\u0331")
        buf.write("\u0332\7r\2\2\u0332\u0333\7j\2\2\u0333\u0339\7k\2\2\u0334")
        buf.write("\u0335\7^\2\2\u0335\u0336\7R\2\2\u0336\u0337\7j\2\2\u0337")
        buf.write("\u0339\7k\2\2\u0338\u0330\3\2\2\2\u0338\u0334\3\2\2\2")
        buf.write("\u0339\u00a6\3\2\2\2\u033a\u033b\7^\2\2\u033b\u033c\7")
        buf.write("e\2\2\u033c\u033d\7j\2\2\u033d\u0343\7k\2\2\u033e\u033f")
        buf.write("\7^\2\2\u033f\u0340\7E\2\2\u0340\u0341\7j\2\2\u0341\u0343")
        buf.write("\7k\2\2\u0342\u033a\3\2\2\2\u0342\u033e\3\2\2\2\u0343")
        buf.write("\u00a8\3\2\2\2\u0344\u0345\7^\2\2\u0345\u0346\7r\2\2\u0346")
        buf.write("\u0347\7u\2\2\u0347\u034d\7k\2\2\u0348\u0349\7^\2\2\u0349")
        buf.write("\u034a\7R\2\2\u034a\u034b\7u\2\2\u034b\u034d\7k\2\2\u034c")
        buf.write("\u0344\3\2\2\2\u034c\u0348\3\2\2\2\u034d\u00aa\3\2\2\2")
        buf.write("\u034e\u034f\7^\2\2\u034f\u0350\7q\2\2\u0350\u0351\7o")
        buf.write("\2\2\u0351\u0352\7g\2\2\u0352\u0353\7i\2\2\u0353\u035b")
        buf.write("\7c\2\2\u0354\u0355\7^\2\2\u0355\u0356\7Q\2\2\u0356\u0357")
        buf.write("\7o\2\2\u0357\u0358\7g\2\2\u0358\u0359\7i\2\2\u0359\u035b")
        buf.write("\7c\2\2\u035a\u034e\3\2\2\2\u035a\u0354\3\2\2\2\u035b")
        buf.write("\u00ac\3\2\2\2\u035c\u0375\5}?\2\u035d\u0375\5\177@\2")
        buf.write("\u035e\u0375\5\u0081A\2\u035f\u0375\5\u0083B\2\u0360\u0375")
        buf.write("\5\u0085C\2\u0361\u0375\5\u0087D\2\u0362\u0375\5\u0089")
        buf.write("E\2\u0363\u0375\5\u008bF\2\u0364\u0375\5\u008dG\2\u0365")
        buf.write("\u0375\5\u008fH\2\u0366\u0375\5\u0091I\2\u0367\u0375\5")
        buf.write("\u0093J\2\u0368\u0375\5\u0095K\2\u0369\u0375\5\u0097L")
        buf.write("\2\u036a\u0375\5\u0099M\2\u036b\u0375\5\u009bN\2\u036c")
        buf.write("\u0375\5\u009dO\2\u036d\u0375\5\u009fP\2\u036e\u0375\5")
        buf.write("\u00a1Q\2\u036f\u0375\5\u00a3R\2\u0370\u0375\5\u00a5S")
        buf.write("\2\u0371\u0375\5\u00a7T\2\u0372\u0375\5\u00a9U\2\u0373")
        buf.write("\u0375\5\u00abV\2\u0374\u035c\3\2\2\2\u0374\u035d\3\2")
        buf.write("\2\2\u0374\u035e\3\2\2\2\u0374\u035f\3\2\2\2\u0374\u0360")
        buf.write("\3\2\2\2\u0374\u0361\3\2\2\2\u0374\u0362\3\2\2\2\u0374")
        buf.write("\u0363\3\2\2\2\u0374\u0364\3\2\2\2\u0374\u0365\3\2\2\2")
        buf.write("\u0374\u0366\3\2\2\2\u0374\u0367\3\2\2\2\u0374\u0368\3")
        buf.write("\2\2\2\u0374\u0369\3\2\2\2\u0374\u036a\3\2\2\2\u0374\u036b")
        buf.write("\3\2\2\2\u0374\u036c\3\2\2\2\u0374\u036d\3\2\2\2\u0374")
        buf.write("\u036e\3\2\2\2\u0374\u036f\3\2\2\2\u0374\u0370\3\2\2\2")
        buf.write("\u0374\u0371\3\2\2\2\u0374\u0372\3\2\2\2\u0374\u0373\3")
        buf.write("\2\2\2\u0375\u00ae\3\2\2\2\u0376\u0377\5\u00adW\2\u0377")
        buf.write("\u0378\5\17\b\2\u0378\u00b0\3\2\2\2\u0379\u037a\5\u00ad")
        buf.write("W\2\u037a\u037b\5\13\6\2\u037b\u00b2\3\2\2\2\u037c\u037e")
        buf.write("\t\6\2\2\u037d\u037c\3\2\2\2\u037e\u037f\3\2\2\2\u037f")
        buf.write("\u037d\3\2\2\2\u037f\u0380\3\2\2\2\u0380\u0381\3\2\2\2")
        buf.write("\u0381\u0382\bZ\2\2\u0382\u00b4\3\2\2\2;\2\u010b\u011e")
        buf.write("\u0125\u012b\u0132\u0139\u0140\u0147\u014e\u0155\u015f")
        buf.write("\u0169\u0173\u017d\u0187\u0191\u0199\u01a1\u01a9\u01b3")
        buf.write("\u01bd\u01c7\u01f5\u01f9\u01fe\u0202\u0207\u0209\u0214")
        buf.write("\u0219\u0240\u024c\u025a\u0268\u027a\u0286\u0290\u029e")
        buf.write("\u02aa\u02b8\u02c8\u02d0\u02d8\u02e0\u02f2\u02fa\u0304")
        buf.write("\u0312\u031c\u032e\u0338\u0342\u034c\u035a\u0374\u037f")
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
    WORD = 52
    INFINITY = 53
    EQ = 54
    LT = 55
    LTE = 56
    GT = 57
    GTE = 58
    BANG = 59
    GREEKLETTER = 60
    GREEKFUNCTIONBRACE = 61
    GREEKFUNCTIONPAREN = 62
    WS = 63

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
            "VARIABLE", "MIXNUMBER", "WORD", "INFINITY", "EQ", "LT", "LTE", 
            "GT", "GTE", "BANG", "GREEKLETTER", "GREEKFUNCTIONBRACE", "GREEKFUNCTIONPAREN", 
            "WS" ]

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
                  "DERIVATIVE", "VARIABLE", "MIXNUMBER", "WORD", "INFINITY", 
                  "EQ", "LT", "LTE", "GT", "GTE", "BANG", "ALPHA", "BETA", 
                  "GAMMA", "DELTA", "EPSILON", "ZETA", "ETA", "THETA", "IOTA", 
                  "KAPPA", "LAMBDA", "MU", "NU", "XI", "OMICRON", "PI", 
                  "RHO", "SIGMA", "TAU", "UPSILON", "PHI", "CHI", "PSI", 
                  "OMEGA", "GREEKLETTER", "GREEKFUNCTIONBRACE", "GREEKFUNCTIONPAREN", 
                  "WS" ]

    grammarFileName = "MatexLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


