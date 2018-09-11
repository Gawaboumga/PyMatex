import math


class Constant:

    def __init__(self, constant: str):
        super().__init__()

        self.value = None

        if constant == '\\pi':
            self.value = math.pi
        elif constant == '\\infty':
            self.value = math.inf
        else:
            _ = float(constant)
            self.value = constant

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        if self.value == math.pi:
            return '\pi'
        if self.value == math.inf:
            return '\\infty'

        if self.value[0] == '-':
            return '({})'.format(self.value)
        else:
            return self.value
