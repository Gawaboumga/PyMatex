from search import IndexCreatorVisitor, IndexSearchVisitor
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from listener import MatexAST
from grammar import MatexLexer, MatexParser
import operator


class SearchQuery:

    def __init__(self, path: str):

        self.data = {}
        self.number_of_different_nodes = {}

        with open(path, 'r') as f:
            for line in f:
                tokens = line.split(':')
                pk = int(tokens[0])
                latex = tokens[1].strip()

                ast = self.__parse(latex)

                visitor = IndexCreatorVisitor(self.data, pk)
                ast.accept(visitor)

                self.number_of_different_nodes[pk] = visitor.get_number_of_nodes_of_different_nodes()


    def search(self, content: str):
        ast = self.__parse(content)

        visitor = IndexSearchVisitor(self.data)
        ast.accept(visitor)

        results = visitor.get_results()

        for result in results:
            results[result] = int(results[result] / self.number_of_different_nodes[result])

        sorted_result = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_result

    def __parse(self, content: str):
        return MatexAST.parse(content)
