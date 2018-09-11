from tests import BaseTest

from node import Negate, Variable


class VariableTests(BaseTest.BaseTest):

    def test_read_variable(self):
        ast = self.parse('xyz')
        self.assertEqual(ast, Variable('xyz'))

    def test_write_variable(self):
        ast = self.parse('xyz')
        self.assertEqual(str(ast), 'xyz')

    def test_read_negative_variable(self):
        ast = self.parse('-x')
        self.assertEqual(ast, Negate(Variable('x')))

    def test_write_negative_variable(self):
        ast = self.parse('-x')
        self.assertEqual(str(ast), '-(x)')
