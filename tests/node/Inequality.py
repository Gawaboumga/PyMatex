from tests import BaseTest

from pymatex.node import *


class InequalityTests(BaseTest.BaseTest):

    def test_read_simple_inequality(self):
        ast = self.parse(r'\sum_{i < j} i')
        i = Variable('i')
        self.assertEqual(ast, InequalitySummation(Inequality(i, Variable('j'), '<'), None, i))

    def test_read_simple_inequality_with_constant(self):
        ast = self.parse(r'\sum_{0 < j} i')
        i = Variable('i')
        self.assertEqual(ast, InequalitySummation(Inequality(Constant('0'), Variable('j'), '<'), None, i))

    def test_read_multi_inequality(self):
        ast = self.parse(r'\sum_{0 < i \leq j} i')
        i = Variable('i')
        self.assertEqual(ast, InequalitySummation(Inequality(Inequality(Constant('0'), i, '<'), Variable('j'), '\\leq'), None, i))
