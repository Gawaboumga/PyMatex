from pymatex.listener import MatexASTVisitor
from pymatex.node.IterativeFunction import IterativeFunction, IterativeType


class Product(IterativeFunction):

    def __init__(self, variable, start_range, end_range, expression):
        super().__init__(IterativeType.PRODUCT, variable, start_range, end_range, expression)

    def __str__(self):
        return '\\prod_{{{}={}}}^{{{}}}{{{}}}'.format(self.variable, self.start_range, self.end_range,
                                                      self.expression)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_product(self)


class InequalityProduct(Product):

    def __init__(self, start_range, end_range, expression):
        super().__init__(None, start_range, end_range, expression)

    def __str__(self):
        if self.end_range:
            return r'\prod_{{{}}}^{{{}}}{{{}}}'.format(self.start_range, self.end_range, self.expression)
        else:
            return r'\prod_{{{}}}{{{}}}'.format(self.start_range, self.expression)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_product(self)


class SetProduct(Product):

    def __init__(self, start_range, end_range, expression):
        super().__init__(None, start_range, end_range, expression)

    def __str__(self):
        if self.end_range:
            return r'\prod_{{{}}}^{{{}}}{{{}}}'.format(self.start_range, self.end_range, self.expression)
        else:
            return r'\prod_{{{}}}{{{}}}'.format(self.start_range, self.expression)

    def accept(self, visitor: MatexASTVisitor):
        return visitor.visit_product(self)
