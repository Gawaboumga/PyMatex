
class Negate:

    def __init__(self, node):
        super().__init__()

        self.node = node

    def __eq__(self, other):
        return self.node == other.node

    def __str__(self):
        return '-({})'.format(self.node)
