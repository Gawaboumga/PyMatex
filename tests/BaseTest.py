from pymatex.listener import MatexAST
import unittest


class BaseTest(unittest.TestCase):

    def parse(self, text):
        return MatexAST.parse(text)
