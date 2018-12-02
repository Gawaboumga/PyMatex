from pymatex.node import *


class MatexASTVisitor:
    def visit_addition(self, addition_node: Addition):
        addition_node.lhs.accept(self)
        addition_node.rhs.accept(self)
    
    def visit_constant(self, constant_node: Constant):
        pass
    
    def visit_division(self, division_node: Division):
        division_node.lhs.accept(self)
        division_node.rhs.accept(self)

    def visit_exponentiation(self, exponentiation_node: Exponentiation):
        exponentiation_node.lhs.accept(self)
        exponentiation_node.rhs.accept(self)
    
    def visit_function(self, function_node: Function):
        for argument in function_node.arguments:
            argument.accept(self)
    
    def visit_indexed_variable(self, indexed_variable_node: IndexedVariable):
        indexed_variable_node.index.accept(self)
    
    def visit_integral(self, integral_node: Integral):
        integral_node.variable.accept(self)
        integral_node.start_range.accept(self)
        integral_node.end_range.accept(self)
        integral_node.expression.accept(self)

    def visit_multiplication(self, multiplication_node: Multiplication):
        multiplication_node.lhs.accept(self)
        multiplication_node.rhs.accept(self)

    def visit_negate(self, negate_node: Negate):
        negate_node.node.accept(self)

    def visit_product(self, product_node: Product):
        product_node.variable.accept(self)
        product_node.start_range.accept(self)
        product_node.end_range.accept(self)
        product_node.expression.accept(self)

    def visit_subtraction(self, subtraction_node: Subtraction):
        subtraction_node.lhs.accept(self)
        subtraction_node.rhs.accept(self)

    def visit_summation(self, summation_node: Summation):
        summation_node.variable.accept(self)
        summation_node.start_range.accept(self)
        summation_node.end_range.accept(self)
        summation_node.expression.accept(self)

    def visit_variable(self, variable_node: Variable):
        pass
