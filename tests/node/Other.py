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

    def test_read_multiplication_of_function(self):
        ast = self.parse(r'1/(n + 1/2) \sum_{k=1}^{n-1} \zeta(2k) \zeta(2n - 2k)')
        one = Constant('1')
        two = Constant('2')
        k = Variable('k')
        n = Variable('n')
        two_k = Multiplication(two, k)
        self.assertEqual(ast, Multiplication(Division(one, Addition(n, Division(one, two))),
                                             Summation(k, one, Subtraction(n, one),
                                                       Multiplication(Function(Func.ZETA, two_k), Function(Func.ZETA,
                                                                                                           Subtraction(
                                                                                                               Multiplication(
                                                                                                                   two,
                                                                                                                   n),
                                                                                                               two_k))))))