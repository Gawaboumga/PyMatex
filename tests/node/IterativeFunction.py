from tests import BaseTest

from node import Addition, Constant, Multiplication, Product, Subtraction, Summation, Variable


class SummationTests(BaseTest.BaseTest):

    def test_read_simple_summation(self):
        ast = self.parse(r'\sum_{i=0}^{\infty} (i + 1)')
        self.assertEqual(ast, Summation(Variable('i'), Constant('0'), Constant('\\infty'), Addition(Variable('i'), Constant('1'))))

    def test_write_simple_summation(self):
        ast = self.parse(r'\sum_{i=0}^{\infty} (i + 1)')
        self.assertEqual(str(ast), '\sum_{i=0}^{\infty}{(i + 1)}')

    def test_read_nested_summation(self):
        ast = self.parse(r'\sum_{i = 1}^{\infty}\sum_{j = 1}^{\infty} (i + j)')
        self.assertEqual(ast, Summation(Variable('i'), Constant('1'), Constant('\\infty'),
                                        Summation(Variable('j'), Constant('1'), Constant('\\infty'),
                                                  Addition(Variable('i'), Variable('j')))))

    def test_read_simple_product(self):
        ast = self.parse(r'\prod_{i=0}^{\infty} (i + 1)')
        self.assertEqual(ast, Product(Variable('i'), Constant('0'), Constant('\\infty'), Addition(Variable('i'), Constant('1'))))

    def test_write_simple_product(self):
        ast = self.parse(r'\prod_{i=0}^{\infty} (i + 1)')
        self.assertEqual(str(ast), '\\prod_{i=0}^{\\infty}{(i + 1)}')

    def test_read_addition_of_summation_and_product(self):
        ast = self.parse(r'\sum_{i=0}^{\infty} i + \prod_{i=0}^{\infty} i')

        summation = Summation(Variable('i'), Constant('0'), Constant('\\infty'), Variable('i'))
        product = Product(Variable('i'), Constant('0'), Constant('\\infty'), Variable('i'))
        self.assertEqual(ast, Addition(summation, product))

    def test_read_subtraction_of_product_and_summation(self):
        ast = self.parse(r'\prod_{i=0}^{\infty} i - \sum_{i=0}^{\infty} i')

        summation = Summation(Variable('i'), Constant('0'), Constant('\\infty'), Variable('i'))
        product = Product(Variable('i'), Constant('0'), Constant('\\infty'), Variable('i'))
        self.assertEqual(ast, Subtraction(product, summation))

    def test_read_multiplication_of_summations(self):
        ast = self.parse(r'\sum_{i=0}^{\infty} i * \sum_{i=0}^{\infty} i * \sum_{i=0}^{\infty} i')

        summation = Summation(Variable('i'), Constant('0'), Constant('\\infty'), Variable('i'))
        self.assertEqual(ast, Multiplication(Multiplication(summation, summation), summation))
