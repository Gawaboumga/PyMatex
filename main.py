import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from grammar import MatexLexer, MatexParser


def main(argv):
    input = FileStream(argv[1])
    lexer = MatexLexer.MatexLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MatexParser.MatexParser(stream)
    tree = parser.math()
    print(Trees.toStringTree(tree, None, parser))


if __name__ == '__main__':
    main(sys.argv)