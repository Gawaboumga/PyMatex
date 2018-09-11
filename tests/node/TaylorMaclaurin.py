from tests import BaseTest

from node import Addition, Constant, Division, Exponentiation, Func, Function, Multiplication, Summation, Variable


class TaylorMaclaurinTests(BaseTest.BaseTest):

    def test_read_exponential(self):
        ast = self.parse(r'\sum_{n=0}^{\infty} \frac{x^n}{n!}')
        self.assertEqual(ast, Summation(Variable('n'), Constant('0'), Constant('\\infty'),
                                        Division(Exponentiation(Variable('x'), Variable('n')),
                                                 Function(Func.FACTORIAL, Variable('n')))))

    def test_read_logarithm(self):
        ast = self.parse(r'\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} x^{n}')
        self.assertEqual(ast, Summation(Variable('n'), Constant('1'), Constant('\\infty'), Multiplication(
            Division(Exponentiation(Constant('-1'), Addition(Variable('n'), Constant('1'))), Variable('n')),
            Exponentiation(Variable('x'), Variable('n')))))

    def test_read_geometric(self):
        ast = self.parse(r'\sum_{n=0}^{\infty} x^n')
        self.assertEqual(ast, Summation(Variable('n'), Constant('0'), Constant('\\infty'),
                                        Exponentiation(Variable('x'), Variable('n'))))

    def test_read_sin(self):
        ast = self.parse(r'\sum_{n=0}^{\infty} \frac{(-1)^n}{(2n + 1)!} x^{2n + 1}')
        two_times_n_plus_one = Addition(Multiplication(Constant('2'), Variable('n')), Constant('1'))
        self.assertEqual(ast, Summation(Variable('n'), Constant('0'), Constant('\\infty'), Multiplication(
            Division(Exponentiation(Constant('-1'), Variable('n')), Function(Func.FACTORIAL, two_times_n_plus_one)),
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
