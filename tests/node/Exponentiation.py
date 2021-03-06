from tests import BaseTest

from pymatex.node import Addition, Constant, Division, Exponentiation, Multiplication, Subtraction, Variable


class ExponentiationTests(BaseTest.BaseTest):

    def test_read_normal_exponent(self):
        ast = self.parse('x^{2}')
        self.assertEqual(ast, Exponentiation(Variable('x'), Constant('2')))

    def test_write_normal_exponent(self):
        ast = self.parse('x^{2}')
        self.assertEqual(str(ast), 'x^{2}')

    def test_read_short_exponent(self):
        ast = self.parse('x^2')
        self.assertEqual(ast, Exponentiation(Variable('x'), Constant('2')))

    def test_write_short_exponent(self):
        ast = self.parse('x^2')
        self.assertEqual(str(ast), 'x^{2}')

    def test_read_complex_exponent(self):
        ast = self.parse('x^{2y + 3}')
        self.assertEqual(ast, Exponentiation(Variable('x'), Addition(Multiplication(Constant('2'), Variable('y')), Constant('3'))))

    def test_write_complex_exponent(self):
        ast = self.parse('x^{2y + 3}')
        self.assertEqual(str(ast), 'x^{((2 * y) + 3)}')

    def test_read_priority_of_operations(self):
        ast = self.parse('4a^2')

        self.assertEqual(ast, Multiplication(Constant('4'), Exponentiation(Variable('a'), Constant('2'))))

    def test_read_priority_of_operations_two(self):
        ast = self.parse(r'\frac{1}{1 - 2^{1-s}}')
        one = Constant('1')
        self.assertEqual(ast, Division(one, Subtraction(one, Exponentiation(Constant('2'), Subtraction(one, Variable('s'))))))
