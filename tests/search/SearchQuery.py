from tests import BaseTest
from pymatex.search import SearchQuery


class SearchQueryTests(BaseTest.BaseTest):

    def test_read(self):
        s = SearchQuery(path='tests/search/resources/search-content-simple-tests.txt')

    def test_search_simple(self):
        s = SearchQuery(path='tests/search/resources/search-content-simple-tests.txt')
        results = s.search(r'(ky+o)')

        self.assertListEqual(list(map(lambda x: x[0], results)), [2, 1])

    def test_search_less_simple(self):
        s = SearchQuery(path='tests/search/resources/search-content-simple-tests.txt')
        results = s.search(r'(ky+o) * (uy^{2} + vy + n)')

        self.assertListEqual(list(map(lambda x: x[0], results)), [1, 2])

    def test_search_summation_and_bound_variables(self):
        s = SearchQuery(path='tests/search/resources/search-content-summation-tests.txt')
        results = s.search(r'\sum_{k=0}^{\infty} k')

        self.assertListEqual(list(map(lambda x: x[0], results)), [2, 1])

    def test_remove(self):
        s = SearchQuery(path='tests/search/resources/search-content-simple-tests.txt')
        results = s.search(r'(ky+o) * (uy^{2} + vy + n)')

        self.assertListEqual(list(map(lambda x: x[0], results)), [1, 2])

        s.remove(1)

        results = s.search(r'(ky+o) * (uy^{2} + vy + n)')
        self.assertListEqual(list(map(lambda x: x[0], results)), [2])
