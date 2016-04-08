class FalsePositionMethod:
    """
    Theory: https://en.wikipedia.org/wiki/False_position_method

    This class takes in a function with 2 bound values and finds the root using the false position method.

    You can instantiate the class with the function and the bound values; a method on the instance lets
    you find the root based on margin of error.

    Example:
        math_function = lambda x: (3*(x**3) + 5*(x**2) + 7)
        bound_one = -10
        bound_two = 10
        margin = 0.01
        root = FalsePositionMethod(math_function, bound_one, bound_two).fetch_root(margin)
    """

    def __init__(self, math_function, bound_one, bound_two):
        self.math_function = math_function
        self.bound_one = bound_one
        self.bound_two = bound_two
        self.__validate_bound_values()


    def fetch_root(self, margin):
        if self.__acceptable(self.bound_value_one, margin):
            return self.bound_one
        elif self.__acceptable(self.bound_value_two, margin):
            return self.bound_two
        else:
            return self.__execute_method(margin)


    def __execute_method(self, margin):
        bound_one = self.bound_one
        value_one = self.bound_value_one

        bound_two = self.bound_two
        value_two = self.bound_value_two

        while True:
            linear_root = self.__find_linear_root(bound_one, value_one, bound_two, value_two)
            root = linear_root['x']
            root_value = linear_root['y']

            if self.__acceptable(root_value, margin):
                return root
            elif (root_value * value_one) < 0:
                bound_two = root
                value_two = root_value
            elif (root_value * value_two) < 0:
                bound_one = root
                value_one = root_value


    def __find_linear_root(self, x1, y1, x2, y2):
        x3_numerator = (x1 * y2) - (x2 * y1)
        x3_denominator = 1.00 * (y2 - y1)
        x3 = x3_numerator / x3_denominator
        y3 = self.math_function(x3)
        point = { 'x': x3, 'y': y3 }
        return point


    def __acceptable(self, val, margin):
        acceptable = abs(val) <= abs(margin)
        return acceptable


    def __validate_bound_values(self):
        self.bound_value_one = self.math_function(self.bound_one)
        self.bound_value_two = self.math_function(self.bound_two)
        if (self.bound_value_one * self.bound_value_two) > 0:
            raise ValueError('Invalid bound values.')
