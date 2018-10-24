from pymatex.listener import MatexASTVisitor
from pymatex.node import *


class IndexSearchVisitor(MatexASTVisitor.MatexASTVisitor):

    def __init__(self, data: dict):
        self.data = data
        self.results = {}
        self.seen_constants = {}
        self.seen_variables = {}
        self.bound_variables = set()

    def get_results(self):
        return self.results

    def visit_addition(self, addition_node: Addition):
        depth_lhs = addition_node.lhs.accept(self)
        depth_rhs = addition_node.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.search(node_depth, NodeType.ADDITION)
        return node_depth

    def visit_constant(self, constant_node: Constant):
        node_depth = 0
        self.search_constant(node_depth, NodeType.CONSTANT, constant_node.value)
        return node_depth

    def visit_division(self, division_node: Division):
        depth_lhs = division_node.lhs.accept(self)
        depth_rhs = division_node.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.search(node_depth, NodeType.DIVISION)
        return node_depth

    def visit_exponentiation(self, exponentiation_node: Exponentiation):
        depth_expr = exponentiation_node.lhs.accept(self)
        depth_exponent = exponentiation_node.rhs.accept(self)

        node_depth = max(depth_expr, depth_exponent) + 1
        self.search(node_depth, NodeType.EXPONENTIATION)
        return node_depth

    def visit_function(self, function_node: Function):
        depth = function_node.expression.accept(self)

        node_depth = depth + 1
        self.search(node_depth, NodeType.FUNCTION)
        return node_depth

    def visit_indexed_variable(self, indexed_variable_node: IndexedVariable):
        depth = indexed_variable_node.index.accept(self)

        node_depth = depth + 1
        self.search_variable(node_depth, NodeType.INDEXEDVARIABLE, indexed_variable_node.variable)
        return node_depth

    def visit_integral(self, integral_node: Integral):
        integral_node.variable.accept(self)
        integral_node.start_range.accept(self)
        integral_node.end_range.accept(self)
        self.add_bound_variable(integral_node.variable)
        depth_expression = integral_node.expression.accept(self)
        self.remove_bound_variable(integral_node.variable)

        node_depth = depth_expression + 1
        self.search(node_depth, NodeType.SUMMATION)
        return node_depth

    def visit_multiplication(self, multiplication_node: Multiplication):
        depth_lhs = multiplication_node.lhs.accept(self)
        depth_rhs = multiplication_node.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.search(node_depth, NodeType.MULTIPLICATION)
        return node_depth

    def visit_negate(self, negate_node: Negate):
        depth = negate_node.node.accept(self)

        self.search(depth + 1, NodeType.NEGATE)
        return depth

    def visit_product(self, product_node: Product):
        product_node.variable.accept(self)
        product_node.start_range.accept(self)
        product_node.end_range.accept(self)
        self.add_bound_variable(product_node.variable)
        depth_expression = product_node.expression.accept(self)
        self.remove_bound_variable(product_node.variable)

        node_depth = depth_expression + 1
        self.search(node_depth, NodeType.SUMMATION)
        return node_depth

    def visit_subtraction(self, subtraction_node: Subtraction):
        depth_lhs = subtraction_node.lhs.accept(self)
        depth_rhs = subtraction_node.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.search(node_depth, NodeType.SUBTRACTION)
        return node_depth

    def visit_summation(self, summation_node: Summation):
        summation_node.variable.accept(self)
        summation_node.start_range.accept(self)
        summation_node.end_range.accept(self)
        self.add_bound_variable(summation_node.variable)
        depth_expression = summation_node.expression.accept(self)
        self.remove_bound_variable(summation_node.variable)

        node_depth = depth_expression + 1
        self.search(node_depth, NodeType.SUMMATION)
        return node_depth

    def visit_variable(self, variable_node: Variable):
        node_depth = 0
        if str(variable_node.variable) in self.bound_variables:
            self.search_bound_variable(node_depth, NodeType.BOUNDVARIABLE, variable_node.variable)
        else:
            self.search_free_variable(node_depth, NodeType.VARIABLE, variable_node.variable)
        return node_depth

    def search(self, node_depth: int, node_type: NodeType):
        nodes = self.data.get(node_depth, None)
        if nodes is None:
            return

        objects = nodes.get(node_type, None)
        if objects:
            self.__add(objects, 100)

    def search_constant(self, node_depth: int, node_type: NodeType, external_data: str):
        nodes = self.data.get(node_depth, None)
        if nodes is None:
            return

        objects = nodes.get(node_type, None)
        if objects is None:
            return

        associated = objects.get(external_data, None)
        if associated:
            self.__add(associated, 100)
        else:
            for mathematical_objects in objects.values():
                self.__add(mathematical_objects, 70)

    def search_bound_variable(self, node_depth: int, node_type: NodeType, external_data: str):
        nodes = self.data.get(node_depth, None)
        if nodes is None:
            return

        objects = nodes.get(node_type, None)
        if objects is None:
            return

        associated = objects.get(external_data, None)
        if associated:
            self.__add(associated, 100)
        else:
            for mathematical_objects in objects.values():
                self.__add(mathematical_objects, 70)

        free_variables = nodes.get(node_type, None)
        if objects is None:
            return
        for mathematical_objects in free_variables.values():
            self.__add(mathematical_objects, 30)

    def search_free_variable(self, node_depth: int, node_type: NodeType, external_data: str):
        nodes = self.data.get(node_depth, None)
        if nodes is None:
            return

        objects = nodes.get(node_type, None)
        if objects is None:
            return

        associated = objects.get(external_data, None)
        if associated:
            self.__add(associated, 100)
        else:
            for mathematical_objects in objects.values():
                self.__add(mathematical_objects, 70)

    def __add(self, items, value):
        for item in items:
            new_value = self.results.get(item, 0) + value
            self.results[item] = new_value

    def add_bound_variable(self, variable: Variable):
        self.bound_variables.add(str(variable))

    def remove_bound_variable(self, variable: Variable):
        self.bound_variables.remove(str(variable))
