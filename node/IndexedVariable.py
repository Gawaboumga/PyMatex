from node.Variable import Variable


class IndexedVariable(Variable):

    def __init__(self, variable: str, index):
        super().__init__(variable)

        self.index = index

    def __eq__(self, other):
        return super().__eq__(other) and self.index == other.index

    def __str__(self):
        return '{}_{{{}}}'.format(self.variable, self.index)
