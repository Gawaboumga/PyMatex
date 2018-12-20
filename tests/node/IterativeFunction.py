from tests import BaseTest

from pymatex.node import *


class IterativeFunctionTests(BaseTest.BaseTest):

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

    def test_read_integral(self):
        ast = self.parse(r'\int_{a}^{b} 3x dx')

        summation = Integral(Variable('x'), Variable('a'), Variable('b'), Multiplication(Constant('3'), Variable('x')))
        self.assertEqual(ast, summation)

    def test_read_nested_integral(self):
        ast = self.parse(r'\int_{a}^{b} \int_{c}^{d} 3x y dy dx')

        internal = Integral(Variable('y'), Variable('c'), Variable('d'), Multiplication(Multiplication(Constant('3'), Variable('x')), Variable('y')))
        outer = Integral(Variable('x'), Variable('a'), Variable('b'), internal)
        self.assertEqual(ast, outer)

    def test_read_function_call_zeta(self):
        ast = self.parse(r'\sum_{n=0}^{\infty} \zeta(2n) x^{2n}')
        two_n = Multiplication(Constant('2'), Variable('n'))
        self.assertEqual(ast, Summation(Variable('n'), Constant('0'), Constant('\\infty'), Multiplication(Function(Func.ZETA, two_n), Exponentiation(Variable('x'), two_n))))

    def test_read_simple_continued_fraction(self):
        ast = self.parse(r'1 + (2 K_{k=1}^{\infty} \frac{1}{1})')
        one = Constant('1')
        self.assertEqual(ast, Addition(one, Multiplication(Constant('2'), Fraction(Variable('k'), one, Constant('\\infty'), Division(one, one)))))
