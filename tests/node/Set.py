from tests import BaseTest

from pymatex.node import *


class SetTests(BaseTest.BaseTest):

    def test_read_set_summation(self):
        ast = self.parse(r'\sum_{\omega \in \Lambda \ {0}} \omega^2')
        omega = Variable('\omega')

        self.assertEqual(ast, SetSummation(Set(omega, SetDifference(Variable('\\Lambda'), Constant('0'))), None, Exponentiation(omega, Constant('2'))))

    def test_read_strange_product(self):
        ast = self.parse(r'\prod_{\omega \in \Lambda}^{\infty} \omega^2')
        omega = Variable('\omega')

        self.assertEqual(ast, SetProduct(Set(omega, Variable('\\Lambda')), Constant('\\infty'),
                                           Exponentiation(omega, Constant('2'))))

    def test_read_simplest(self):
        ast = self.parse(r'\prod_{a \in A} a')
        a = Variable('a')

        self.assertEqual(ast, SetProduct(Set(a, Variable('A')), None, a))
