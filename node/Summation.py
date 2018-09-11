from .IterativeFunction import *


class Summation(IterativeFunction):

    def __init__(self, variable, start_range, end_range, expression):
        super().__init__(IterativeType.SUM, variable, start_range, end_range, expression)
