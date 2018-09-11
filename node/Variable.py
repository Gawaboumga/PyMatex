
class Variable:

    def __init__(self, variable: str):
        super().__init__()

        self.variable = variable

    def __eq__(self, other):
        return self.variable == other.variable

    def __str__(self):
        return self.variable
