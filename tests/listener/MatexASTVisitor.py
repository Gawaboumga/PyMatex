from tests import BaseTest
from listener import MatexASTVisitor
from node import *


class TestVisitor(MatexASTVisitor.MatexASTVisitor):
    nodes = ["addition", "constant", "division", "exponentiation", "function", "indexed_variable", "integral",
             "multiplication", "negate", "product", "subtraction", "summation", "variable"]
    visited = {}

    def visit_addition(self, addition_node: Addition):
        self.visited["addition"] = True
        super().visit_addition(addition_node)

    def visit_constant(self, constant_node: Constant):
        self.visited["constant"] = True
        super().visit_constant(constant_node)

    def visit_division(self, division_node: Division):
        self.visited["division"] = True
        super().visit_division(division_node)

    def visit_exponentiation(self, exponentiation_node: Exponentiation):
        self.visited["exponentiation"] = True
        super().visit_exponentiation(exponentiation_node)

    def visit_function(self, function_node: Function):
        self.visited["function"] = True
        super().visit_function(function_node)

    def visit_indexed_variable(self, indexed_variable_node: IndexedVariable):
        self.visited["indexed_variable"] = True
        super().visit_indexed_variable(indexed_variable_node)

    def visit_integral(self, integral_node: Integral):
        self.visited["integral"] = True
        super().visit_integral(integral_node)

    def visit_multiplication(self, multiplication_node: Multiplication):
        self.visited["multiplication"] = True
        super().visit_multiplication(multiplication_node)

    def visit_negate(self, negate_node: Negate):
        self.visited["negate"] = True
        super().visit_negate(negate_node)

    def visit_product(self, product_node: Product):
        self.visited["product"] = True
        super().visit_product(product_node)

    def visit_subtraction(self, subtraction_node: Subtraction):
        self.visited["subtraction"] = True
        super().visit_subtraction(subtraction_node)

    def visit_summation(self, summation_node: Summation):
        self.visited["summation"] = True
        super().visit_summation(summation_node)

    def visit_variable(self, variable_node: Variable):
        self.visited["variable"] = True
        super().visit_variable(variable_node)

    def all_visited(self):
        for node in self.nodes:
            if node not in self.visited:
                print("Node: {} not visited".format(node))
                return False
        return True


class MatexASTVisitorTests(BaseTest.BaseTest):

    def test_visit_every_nodes(self):
        ast = self.parse(r'\sum_{i=0}^{\infty}{\sin{i}} + \prod_{i = 0}^{\infty}{i * B_{i} / i} - \int_{a}^{b}{5^{-2} dx}')
        visitor = TestVisitor()
        ast.accept(visitor)
        self.assertTrue(visitor.all_visited())
