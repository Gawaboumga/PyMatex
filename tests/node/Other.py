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

    def test_read_neville_theta_function(self):
        ast = self.parse(r'\frac{\sqrt{2\pi} q(m)^{1/4}}{m^{1/4} \sqrt{K(m)}} \sum_{k=0}^{\infty} (q(m))^{k (k+1)} \cos{\frac{(2k+1)\pi z}{2 K(m)}}')
        one = Constant('1')
        two = Constant('2')
        k = Variable('k')
        m = Variable('m')
        pi = Variable('\\pi')
        one_fourth = Division(one, Constant('4'))

        first_division = Division(Multiplication(Function(Func.SQRT, Multiplication(two, pi)), Exponentiation(Function('q', m), one_fourth)),
                                  Multiplication(Exponentiation(m, one_fourth), Function(Func.SQRT, Function('K', m))))
        q_m_exponent = Exponentiation(Function('q', m), Multiplication(k, Addition(k, one)))
        cos_thing = Function(Func.COS, Division(Multiplication(Multiplication(Addition(Multiplication(two, k), one), pi), Variable('z')), Multiplication(two, Function('K', m))))
        summation = Summation(k, Constant('0'), Constant('\\infty'), Multiplication(q_m_exponent, cos_thing))
        self.assertEqual(ast, Multiplication(first_division, summation))
