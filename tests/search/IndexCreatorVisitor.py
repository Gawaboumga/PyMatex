from tests import BaseTest
from node import NodeType
from search import IndexCreatorVisitor


class IndexCreatorVisitorTests(BaseTest.BaseTest):

    def test_visit_basic_addition(self):
        ast = self.parse(r'3 + x')
        data = {}
        pk = 1
        visitor = IndexCreatorVisitor(data, pk)
        ast.accept(visitor)

        self.assertTrue(self.has(data[0][NodeType.CONSTANT], pk, '3'))
        self.assertTrue(self.has(data[0][NodeType.VARIABLE], pk, 'x'))
        self.assertTrue(pk in data[1][NodeType.ADDITION])

    def test_visit_addition_mixed_with_multiplication(self):
        ast = self.parse(r'3 * x + y * 5')
        data = {}
        pk = 1
        visitor = IndexCreatorVisitor(data, pk)
        ast.accept(visitor)

        self.assertTrue(self.has(data[0][NodeType.CONSTANT], pk, '3'))
        self.assertTrue(self.has(data[0][NodeType.VARIABLE], pk, 'x'))
        self.assertTrue(self.has(data[0][NodeType.VARIABLE], pk, 'y'))
        self.assertTrue(self.has(data[0][NodeType.CONSTANT], pk, '5'))
        self.assertTrue(pk in data[1][NodeType.MULTIPLICATION])
        self.assertTrue(pk in data[2][NodeType.ADDITION])

    def test_visit_summation(self):
        ast = self.parse(r'\sum_{i=0}^{\infty} i * i')
        data = {}
        pk = 1
        visitor = IndexCreatorVisitor(data, pk)
        ast.accept(visitor)

        self.assertTrue(self.has(data[0][NodeType.CONSTANT], pk, '0'))
        self.assertTrue(self.has(data[0][NodeType.VARIABLE], pk, 'i'))
        self.assertTrue(self.has(data[0][NodeType.CONSTANT], pk, '\\infty'))
        self.assertTrue(pk in data[1][NodeType.MULTIPLICATION])
        self.assertTrue(pk in data[2][NodeType.SUMMATION])

    def test_visit_exponentiation_and_function(self):
        ast = self.parse(r'e^{x!}')
        data = {}
        pk = 1
        visitor = IndexCreatorVisitor(data, pk)
        ast.accept(visitor)

        self.assertTrue(self.has(data[0][NodeType.VARIABLE], pk, 'e'))
        self.assertTrue(self.has(data[0][NodeType.VARIABLE], pk, 'x'))
        self.assertTrue(pk in data[1][NodeType.FUNCTION])
        self.assertTrue(pk in data[2][NodeType.EXPONENTIATION])

    def test_visit_indexed_variable(self):
        ast = self.parse(r'3*B_{2n}')
        data = {}
        pk = 1
        visitor = IndexCreatorVisitor(data, pk)
        ast.accept(visitor)

        self.assertTrue(self.has(data[0][NodeType.CONSTANT], pk, '2'))
        self.assertTrue(self.has(data[0][NodeType.CONSTANT], pk, '3'))
        self.assertTrue(self.has(data[0][NodeType.VARIABLE], pk, 'n'))
        self.assertTrue(pk in data[1][NodeType.MULTIPLICATION])
        self.assertTrue(self.has(data[2][NodeType.INDEXEDVARIABLE], pk, 'B'))
        self.assertTrue(pk in data[3][NodeType.MULTIPLICATION])

    def has(self, data: dict, pk: int, constant_value: str):
        self.assertIn(constant_value, data)
        self.assertIn(pk, data[constant_value])
        return True
