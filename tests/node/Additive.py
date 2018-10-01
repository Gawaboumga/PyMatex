from tests import BaseTest

from pymatex.node import Addition, Constant, Negate, Subtraction, Variable


class AdditiveTests(BaseTest.BaseTest):

    def test_read_addition_of_constants(self):
        ast = self.parse('3 + 2')
        self.assertEqual(ast, Addition(Constant('3'), Constant('2')))

    def test_write_addition_of_constants(self):
        ast = self.parse('3 + 2')
        self.assertEqual(str(ast), '(3 + 2)')

    def test_read_addition_of_multiple_constants(self):
        ast = self.parse('3 + 2 + 5')
        self.assertEqual(ast, Addition(Addition(Constant('3'), Constant('2')), Constant('5')))

        ast = self.parse('3+2+5')
        self.assertEqual(ast, Addition(Addition(Constant('3'), Constant('2')), Constant('5')))

    def test_read_addition_of_variables(self):
        ast = self.parse('x + y')
        self.assertEqual(ast, Addition(Variable('x'), Variable('y')))

        ast = self.parse('x+y')
        self.assertEqual(ast, Addition(Variable('x'), Variable('y')))

    def test_write_addition_of_variables(self):
        ast = self.parse('x+y')
        self.assertEqual(str(ast), '(x + y)')

    def test_read_addition_of_constant_and_variable(self):
        ast = self.parse('n+1')
        self.assertEqual(ast, Addition(Variable('n'), Constant('1')))

    def test_read_subtraction_of_constants(self):
        ast = self.parse('3 - 2')
        self.assertEqual(ast, Subtraction(Constant('3'), Constant('2')))

    def test_write_subtraction_of_constants(self):
        ast = self.parse('3 - 2')
        self.assertEqual(str(ast), '(3 - 2)')

    def test_read_subtraction_of_multiple_constants(self):
        ast = self.parse('3 - 2 - 5')
        self.assertEqual(ast, Subtraction(Subtraction(Constant('3'), Constant('2')), Constant('5')))

    def test_read_subtraction_of_variables(self):
        ast = self.parse('x - y')
        self.assertEqual(ast, Subtraction(Variable('x'), Variable('y')))

    def test_write_subtraction_of_variables(self):
        ast = self.parse('x-y')
        self.assertEqual(str(ast), '(x - y)')

    def test_read_subtraction_of_negate_variable(self):
        ast = self.parse('x - -y')
        self.assertEqual(ast, Subtraction(Variable('x'), Negate(Variable('y'))))

    def test_read_substraction_of_constant_and_variable(self):
        ast = self.parse('n-1')
        self.assertEqual(ast, Subtraction(Variable('n'), Constant('1')))
