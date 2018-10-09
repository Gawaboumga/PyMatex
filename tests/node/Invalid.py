from tests import BaseTest


class InvalidTests(BaseTest.BaseTest):

    def test_read_invalid(self):
        self.assertRaises(Exception, self.parse, '^')
