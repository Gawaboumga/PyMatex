from .IterativeFunction import *


class Product(IterativeFunction):

    def __init__(self, variable, start_range, end_range, expression):
        super().__init__(IterativeType.PRODUCT, variable, start_range, end_range, expression)
