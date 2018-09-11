from tests import BaseTest

from node import Constant, Division, Multiplication, Variable


class MultiplicativeTests(BaseTest.BaseTest):

    def test_read_multiplication_of_constants(self):
        ast = self.parse('3 * 2')
        self.assertEqual(ast, Multiplication(Constant('3'), Constant('2')))

    def test_write_multiplication_of_constants(self):
        ast = self.parse('3*2')
        self.assertEqual(str(ast), '(3 * 2)')

    def test_read_multiplication_of_multiple_constants(self):
        ast = self.parse('3 * 2 * 5')
        self.assertEqual(ast, Multiplication(Multiplication(Constant('3'), Constant('2')), Constant('5')))

    def test_read_multiplication_of_variables(self):
        ast = self.parse('x * y')
        self.assertEqual(ast, Multiplication(Variable('x'), Variable('y')))

    def test_write_multiplication_of_variables(self):
        ast = self.parse('x*y')
        self.assertEqual(str(ast), '(x * y)')

    def test_read_division_of_constants(self):
        ast = self.parse('3 / 2')
        self.assertEqual(ast, Division(Constant('3'), Constant('2')))

    def test_write_division_of_constants(self):
        ast = self.parse('3/2')
        self.assertEqual(str(ast), '\\frac{3}{2}')

    def test_read_division_of_multiple_constants(self):
        ast = self.parse('3 / 2 / 5')
        self.assertEqual(ast, Division(Division(Constant('3'), Constant('2')), Constant('5')))

    def test_read_division_of_variables(self):
        ast = self.parse('x / y')
        self.assertEqual(ast, Division(Variable('x'), Variable('y')))

    def test_write_division_of_variables(self):
        ast = self.parse('x/y')
        self.assertEqual(str(ast), '\\frac{x}{y}')

    def test_read_frac_of_variables(self):
        ast = self.parse('\\frac{x}{y}')
        self.assertEqual(ast, Division(Variable('x'), Variable('y')))

    def test_write_frac_of_variables(self):
        ast = self.parse('\\frac{x}{y}')
        self.assertEqual(str(ast), '\\frac{x}{y}')

    def test_read_mixed_operations_of_constants(self):
        ast = self.parse('3 * 2 / 4 * 5')
        self.assertEqual(ast, Division(Multiplication(Constant('3'), Constant('2')), Multiplication(Constant('4'), Constant('5'))))

    def test_read_mixed(self):
        ast = self.parse('3x')
        self.assertEqual(ast, Multiplication(Constant('3'), Variable('x')))

    def test_read_mixed_with_frac(self):
        ast = self.parse(r'\frac{1}{2} * \frac{3}{4} * \frac{5}{6}')
        self.assertEqual(ast, Multiplication(
            Multiplication(Division(Constant('1'), Constant('2')), Division(Constant('3'), Constant('4'))),
            Division(Constant('5'), Constant('6'))))

    def test_read_mixed_without_times_frac(self):
        ast = self.parse(r'\frac{1}{4} \frac{x}{2}')
        self.assertEqual(ast, Multiplication(Division(Constant('1'), Constant('4')), Division(Variable('x'), Constant('2'))))
