from tests import BaseTest

from node import *


class TaylorMaclaurinTests(BaseTest.BaseTest):

    def test_read_exponential(self):
        ast = self.parse(r'\sum_{n=0}^{\infty} \frac{x^n}{n!}')
        self.assertEqual(ast, Summation(Variable('n'), Constant('0'), Constant('\\infty'),
                                        Division(Exponentiation(Variable('x'), Variable('n')),
                                                 Function(Func.FACTORIAL, Variable('n')))))

    def test_read_logarithm(self):
        ast = self.parse(r'\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} x^{n}')
        self.assertEqual(ast, Summation(Variable('n'), Constant('1'), Constant('\\infty'), Multiplication(
            Division(Exponentiation(Negate(Constant('1')), Addition(Variable('n'), Constant('1'))), Variable('n')),
            Exponentiation(Variable('x'), Variable('n')))))

    def test_read_geometric(self):
        ast = self.parse(r'\sum_{n=0}^{\infty} x^n')
        self.assertEqual(ast, Summation(Variable('n'), Constant('0'), Constant('\\infty'),
                                        Exponentiation(Variable('x'), Variable('n'))))

    def test_read_sin(self):
        ast = self.parse(r'\sum_{n=0}^{\infty} \frac{(-1)^n}{(2n + 1)!} x^{2n + 1}')
        two_times_n_plus_one = Addition(Multiplication(Constant('2'), Variable('n')), Constant('1'))
        self.assertEqual(ast, Summation(Variable('n'), Constant('0'), Constant('\\infty'), Multiplication(
            Division(Exponentiation(Negate(Constant('1')), Variable('n')), Function(Func.FACTORIAL, two_times_n_plus_one)),
            Exponentiation(Variable('x'), two_times_n_plus_one))))

    def test_read_arcsin(self):
        ast = self.parse(r'\sum_{n=0}^{\infty} \frac{(2n)!}{4^n (n!)^2 (2n + 1)} x^{2n + 1}')
        two_times_n = Multiplication(Constant('2'), Variable('n'))
        two_times_n_plus_one = Addition(two_times_n, Constant('1'))
        self.assertEqual(ast, Summation(Variable('n'), Constant('0'), Constant('\\infty'), Multiplication(
            Division(Function(Func.FACTORIAL, two_times_n),
                     Multiplication(Multiplication(Exponentiation(Constant('4'), Variable('n')),
                                    Exponentiation(Function(Func.FACTORIAL, Variable('n')), Constant('2'))),
                                    two_times_n_plus_one)),
            Exponentiation(Variable('x'), two_times_n_plus_one))))

    def test_read_tan(self):
        ast = self.parse(r'\sum_{n=1}^{\infty} |B_{2n}| \frac{4^n (4^n - 1)}{(2n)!} x^{2n - 1}')
        two_times_n = Multiplication(Constant('2'), Variable('n'))
        four_exponent_n = Exponentiation(Constant('4'), Variable('n'))

        self.assertEqual(ast, Summation(Variable('n'), Constant('1'), Constant('\\infty'), Multiplication(
            Multiplication(Function(Func.ABS, IndexedVariable('B', two_times_n)), Division(
                Multiplication(four_exponent_n, Subtraction(four_exponent_n, Constant('1'))),
                Function(Func.FACTORIAL, Multiplication(Constant('2'), Variable('n')))
            )), Exponentiation(Variable('x'), Subtraction(two_times_n, Constant('1'))))))
