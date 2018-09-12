from tests import BaseTest

from node import Constant, Negate


class ConstantTests(BaseTest.BaseTest):

    def test_read_number(self):
        ast = self.parse('3')
        self.assertEqual(ast, Constant('3'))

    def test_write_number(self):
        ast = self.parse('3')
        self.assertEqual(str(ast), '3')

    def test_read_negative_number(self):
        ast = self.parse('-3')
        self.assertEqual(ast, Constant('-3'))

    def test_write_negative_number(self):
        ast = self.parse('-3')
        self.assertEqual(str(ast), '(-3)')
