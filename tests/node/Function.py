from tests import BaseTest

from pymatex.node import Addition, Constant, Func, Function, Multiplication, Variable


class FunctionTests(BaseTest.BaseTest):

    def test_read_sqrt(self):
        ast = self.parse('\\sqrt{2x + 3}')
        self.assertEqual(ast, Function(Func.SQRT, Addition(Multiplication(Constant('2'), Variable('x')), Constant('3'))))

    def test_write_sqrt(self):
        ast = self.parse('\\sqrt{2x + 3}')
        self.assertEqual(str(ast), '\\sqrt{((2 * x) + 3)}')

    def test_read_sin(self):
        ast = self.parse('\\sin{2x + 3}')
        self.assertEqual(ast, Function(Func.SIN, Addition(Multiplication(Constant('2'), Variable('x')), Constant('3'))))

    def test_read_alternative_sin(self):
        ast = self.parse('sin(2x + 3)')
        self.assertEqual(ast, Function(Func.SIN, Addition(Multiplication(Constant('2'), Variable('x')), Constant('3'))))

    def test_write_sin(self):
        ast = self.parse('\\sin{2x + 3}')
        self.assertEqual(str(ast), '\\sin{((2 * x) + 3)}')

    def test_read_factorial(self):
        ast = self.parse('x!')
        self.assertEqual(ast, Function(Func.FACTORIAL, Variable('x')))

        ast = self.parse('3!')
        self.assertEqual(ast, Function(Func.FACTORIAL, Constant('3')))

        ast = self.parse('(2 * x)!')
        self.assertEqual(ast, Function(Func.FACTORIAL, Multiplication(Constant('2'), Variable('x'))))

        ast = self.parse('4 * x!')
        self.assertEqual(ast, Multiplication(Constant('4'), Function(Func.FACTORIAL, Variable('x'))))

    def test_write_factorial(self):
        ast = self.parse('x!')
        self.assertEqual(str(ast), '(x)!')

    def test_read_absolute(self):
        ast = self.parse('|x + 3|')
        self.assertEqual(ast, Function(Func.ABS, Addition(Variable('x'), Constant('3'))))

    def test_write_absolute(self):
        ast = self.parse('|x + 3|')
        self.assertEqual(str(ast), '|(x + 3)|')

    def test_read_zeta(self):
        ast = self.parse(r'\zeta(x)')
        self.assertEqual(ast, Function(Func.ZETA, Variable('x')))
