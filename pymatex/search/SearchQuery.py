from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from pymatex.search import IndexCreatorVisitor, IndexSearchVisitor
from pymatex.listener import MatexAST
from pymatex.grammar import MatexLexer, MatexParser
import operator


class SearchQuery:

    def __init__(self, path: str):

        self.data = {}
        self.number_of_different_nodes = {}

        if path:
            with open(path, 'r') as f:
                for line in f:
                    tokens = line.split(':')
                    pk = int(tokens[0])
                    latex = tokens[1].strip()

                    ast = self.__parse(latex)

                    visitor = IndexCreatorVisitor(self.data, pk)
                    ast.accept(visitor)

                    self.number_of_different_nodes[pk] = visitor.get_number_of_nodes_of_different_nodes()

    def add(self, pk: int, latex: str):
        ast = self.__parse(latex)

        visitor = IndexCreatorVisitor(self.data, pk)
        ast.accept(visitor)

        self.number_of_different_nodes[pk] = visitor.get_number_of_nodes_of_different_nodes()

    def is_valid(self, content: str):
        MatexAST.get_tree(content)

    def remove(self, pk: int):
        self.number_of_different_nodes.pop(pk)
        self.__internal_remove(self.data, pk)

    def search(self, content: str):
        ast = self.__parse(content)

        visitor = IndexSearchVisitor(self.data)
        ast.accept(visitor)

        results = visitor.get_results()

        for result in results:
            results[result] = int(results[result] / self.number_of_different_nodes[result])

        sorted_result = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_result

    def __internal_remove(self, data, pk: int):
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, dict) or isinstance(v, set):
                    self.__internal_remove(v, pk)
                else:
                    if v == pk:
                        del data[k]
        elif isinstance(data, set):
            data.discard(pk)

    def __parse(self, content: str):
        return MatexAST.parse(content)
