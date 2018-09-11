from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from listener import MatexAST
from grammar import MatexLexer, MatexParser
import unittest


class BaseTest(unittest.TestCase):

    def parse(self, text):
        lexer = MatexLexer.MatexLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        parser = MatexParser.MatexParser(stream)
        tree = parser.math()
        ast = MatexAST.MatexAST()
        walker = ParseTreeWalker()
        walker.walk(ast, tree)
        return ast
