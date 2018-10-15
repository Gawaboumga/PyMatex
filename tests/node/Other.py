from tests import BaseTest

from pymatex.node import *


class OtherTests(BaseTest.BaseTest):

    def test_read_zeta(self):
        ast = self.parse(r'\frac{1}{1 - 2^{1-s}} \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^s}')
        one = Constant('1')
        s = Variable('s')
        n = Variable('n')
        self.assertEqual(ast, Multiplication(
            Division(one, Subtraction(one, Exponentiation(Constant('2'), Subtraction(one, s)))),
            Summation(n, one, Constant('\\infty'),
                      Division(Exponentiation(Negate(one), Addition(n, one)), Exponentiation(n, s)))))

    def test_read_multi_multiplication_of_expression(self):
        ast = self.parse(r'x y \sum_{n=1}^{\infty} n')
        n = Variable('n')
        self.assertEqual(ast, Multiplication(Multiplication(Variable('x'), Variable('y')), Summation(n, Constant('1'), Constant('\\infty'), n)))
