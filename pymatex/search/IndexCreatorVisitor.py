from pymatex.listener import MatexASTVisitor
from pymatex.node import *


class IndexCreatorVisitor(MatexASTVisitor.MatexASTVisitor):

    def __init__(self, data: dict, pk: int):
        self.data = data
        self.pk = pk
        self.nodes_seen = {}
        self.bound_variables = set()

    def get_number_of_nodes_of_different_nodes(self):
        return len(self.nodes_seen)

    def visit_addition(self, addition_node: Addition):
        depth_lhs = addition_node.lhs.accept(self)
        depth_rhs = addition_node.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.add(node_depth, NodeType.ADDITION)
        return node_depth

    def visit_constant(self, constant_node: Constant):
        node_depth = 0
        self.add(node_depth, NodeType.CONSTANT, constant_node.value)
        return node_depth

    def visit_division(self, division_node: Division):
        depth_lhs = division_node.lhs.accept(self)
        depth_rhs = division_node.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.add(node_depth, NodeType.DIVISION)
        return node_depth

    def visit_exponentiation(self, exponentiation_node: Exponentiation):
        depth_expr = exponentiation_node.lhs.accept(self)
        depth_exponent = exponentiation_node.rhs.accept(self)

        node_depth = max(depth_expr, depth_exponent) + 1
        self.add(node_depth, NodeType.EXPONENTIATION)
        return node_depth

    def visit_fraction(self, fraction_node: Fraction):
        if fraction_node.variable:
            fraction_node.variable.accept(self)
        fraction_node.start_range.accept(self)
        if fraction_node.end_range:
            fraction_node.end_range.accept(self)

        if fraction_node.variable:
            self.add_bound_variable(fraction_node.variable)
        depth_expression = fraction_node.expression.accept(self)
        if fraction_node.variable:
            self.remove_bound_variable(fraction_node.variable)

        node_depth = depth_expression + 1
        self.add(node_depth, NodeType.FRACTION)
        return node_depth

    def visit_function(self, function_node: Function):
        first_argument = function_node.argument(0)
        depth = first_argument.accept(self)
        for i in range(1, function_node.number_of_arguments()):
            depth = min(depth, function_node.argument(i).accept(self))

        node_depth = depth + 1
        self.add(node_depth, NodeType.FUNCTION)
        return node_depth

    def visit_indexed_variable(self, indexed_variable_node: IndexedVariable):
        depth = indexed_variable_node.index.accept(self)

        node_depth = depth + 1
        self.add(node_depth, NodeType.INDEXEDVARIABLE, indexed_variable_node.variable)
        return node_depth

    def visit_integral(self, integral_node: Integral):
        integral_node.variable.accept(self)
        integral_node.start_range.accept(self)
        integral_node.end_range.accept(self)
        self.add_bound_variable(integral_node.variable)
        depth_expression = integral_node.expression.accept(self)
        self.remove_bound_variable(integral_node.variable)

        node_depth = depth_expression + 1
        self.add(node_depth, NodeType.SUMMATION)
        return node_depth

    def visit_multiplication(self, multiplication_node: Multiplication):
        depth_lhs = multiplication_node.lhs.accept(self)
        depth_rhs = multiplication_node.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.add(node_depth, NodeType.MULTIPLICATION)
        return node_depth

    def visit_negate(self, negate_node: Negate):
        depth = negate_node.node.accept(self)

        self.add(depth + 1, NodeType.NEGATE)
        return depth

    def visit_product(self, product_node: Product):
        if product_node.variable:
            product_node.variable.accept(self)
        product_node.start_range.accept(self)
        if product_node.end_range:
            product_node.end_range.accept(self)

        if product_node.variable:
            self.add_bound_variable(product_node.variable)
        depth_expression = product_node.expression.accept(self)
        if product_node.variable:
            self.remove_bound_variable(product_node.variable)

        node_depth = depth_expression + 1
        self.add(node_depth, NodeType.PRODUCT)
        return node_depth

    def visit_set(self, set_node: Set):
        depth_lhs = set_node.lhs.accept(self)
        depth_rhs = set_node.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.add(node_depth, NodeType.SET)
        return node_depth

    def visit_set_difference(self, set_difference: SetDifference):
        depth_lhs = set_difference.lhs.accept(self)
        depth_rhs = set_difference.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.add(node_depth, NodeType.SET_DIFFERENCE)
        return node_depth

    def visit_subtraction(self, subtraction_node: Subtraction):
        depth_lhs = subtraction_node.lhs.accept(self)
        depth_rhs = subtraction_node.rhs.accept(self)

        node_depth = max(depth_lhs, depth_rhs) + 1
        self.add(node_depth, NodeType.SUBTRACTION)
        return node_depth

    def visit_summation(self, summation_node: Summation):
        if summation_node.variable:
            summation_node.variable.accept(self)
        summation_node.start_range.accept(self)
        if summation_node.end_range:
            summation_node.end_range.accept(self)

        if summation_node.variable:
            self.add_bound_variable(summation_node.variable)
        depth_expression = summation_node.expression.accept(self)
        if summation_node.variable:
            self.remove_bound_variable(summation_node.variable)

        node_depth = depth_expression + 1
        self.add(node_depth, NodeType.SUMMATION)
        return node_depth

    def visit_variable(self, variable_node: Variable):
        node_depth = 0
        if str(variable_node.variable) in self.bound_variables:
            self.add(node_depth, NodeType.BOUNDVARIABLE, variable_node.variable)
        else:
            self.add(node_depth, NodeType.VARIABLE, variable_node.variable)
        return node_depth

    def add(self, node_depth: int, node_type: NodeType, external_data=None):
        nodes = self.data.get(node_depth, dict())
        if external_data is None:
            objects = nodes.get(node_type, set())
            objects.add(self.pk)
        else:
            objects = nodes.get(node_type, dict())
            associated = objects.get(external_data, set())
            associated.add(self.pk)
            objects[external_data] = associated
        nodes[node_type] = objects
        self.data[node_depth] = nodes

        nodes_depth = self.nodes_seen.get(node_depth, set())
        if nodes_depth is None:
            nodes_depth.add(node_type)
        else:
            if node_type not in nodes_depth:
                nodes_depth.add(node_type)

        self.nodes_seen[node_depth] = nodes_depth

    def add_bound_variable(self, variable: Variable):
        self.bound_variables.add(str(variable))

    def remove_bound_variable(self, variable: Variable):
        self.bound_variables.remove(str(variable))
