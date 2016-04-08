from core.bisection_method import BisectionMethod
from core.false_position_method import FalsePositionMethod

import unittest

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

        acceptable = abs(value_at_root) <= margin
        assert(acceptable)


    def test_false_position_method(self):
        math_function = lambda x: (3*(x**3) + 5*(x**2) + 7)
        bound_one = -10
        bound_two = 10
        margin = 0.01

        instance = FalsePositionMethod(math_function, bound_one, bound_two)
        root = instance.fetch_root(margin)
        value_at_root = math_function(root)

        acceptable = abs(value_at_root) <= margin
        assert(acceptable)


unittest.main()
