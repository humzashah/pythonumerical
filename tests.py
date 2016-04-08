import unittest
from core.bisection_method import BisectionMethod

class TestBisectionMethod(unittest.TestCase):
    def test_bisection_method(self):
        math_function = lambda x: ((16 * x) + 37)
        bound_one = -10
        bound_two = 10
        margin = 0.01
        iterations = 200

        instance = BisectionMethod(math_function, bound_one, bound_two)
        root = instance.fetch_root(margin, iterations)
        value_at_root = math_function(root)

        assert(abs(value_at_root) <= margin)


unittest.main()
