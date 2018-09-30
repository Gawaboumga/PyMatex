from tests import BaseTest

from node import Multiplication, Negate, Variable


class VariableTests(BaseTest.BaseTest):

    def test_read_variable(self):
        ast = self.parse('xyz')
        self.assertEqual(ast, Multiplication(Multiplication(Variable('x'), Variable('y')), Variable('z')))

    def test_write_variable(self):
        ast = self.parse('xyz')
        self.assertEqual(str(ast), '((x * y) * z)')

    def test_read_negative_variable(self):
        ast = self.parse('-x')
        self.assertEqual(ast, Negate(Variable('x')))

    def test_write_negative_variable(self):
        ast = self.parse('-x')
        self.assertEqual(str(ast), '-(x)')

    def test_read_special_variable(self):
        ast = self.parse('\pi')
        self.assertEqual(ast, Variable('\pi'))

    def test_write_special_variable(self):
        ast = self.parse('\pi')
        self.assertEqual(str(ast), '\pi')
