class BisectionMethod():
    """
    This class takes in a function with 2 bound values and finds the root using the bisection method.

    You can instantiate the class with the function and the bound values; a method on the instance lets
    you find the root based on margin or error and the number of iterations - parameters that the accuracy
    depends on.

    Example:
        math_function = lambda x: (16 * x) + 32
        bound_one = -10
        bound_two = 10
        margin = 0.1
        iterations = 20
        root = BisectionMethod(math_function, bound_one, bound_two).fetch_root(margin, iterations)
    """

    def __init__(self, math_function, neighbour_one, neighbour_two):
        self.math_function = math_function
        self.neighbour_one = neighbour_one
        self.neighbour_two = neighbour_two
        self.__validate_neighbour_values()


    def fetch_root(self, margin, iterations):
        margin = abs(margin)

        if abs(self.neighbour_value_one) <= margin:
            return self.neighbour_one
        elif abs(self.neighbour_value_two) <= margin:
            return self.neighbour_two
        else:
            self.__validate_iterations(iterations)
            return self.__run_iterations(margin, iterations)

    def __run_iterations(self, margin, iterations):
        bound_one = self.neighbour_one
        value_one = self.neighbour_value_one

        bound_two = self.neighbour_two
        value_two = self.neighbour_value_two

        for iteration in range(iterations + 1):
            midpoint = (bound_one + bound_two) / 2.00
            midpoint_value = self.math_function(midpoint)
            if abs(midpoint_value) <= margin:
                return midpoint
            elif (value_one * midpoint_value) < 0:
                bound_two = midpoint
            elif (value_two * midpoint_value) < 0:
                bound_one = midpoint
            else:
                raise ValueError('Help!')

        return midpoint


    def __validate_neighbour_values(self):
        self.neighbour_value_one = self.math_function(self.neighbour_one)
        self.neighbour_value_two = self.math_function(self.neighbour_two)
        if (self.neighbour_value_one * self.neighbour_value_two) > 0:
            raise ValueError('Invalid neighbour values.')


    def __validate_iterations(self, iterations):
        if (iterations in [True, False]) or (isinstance(iterations, int) and (iterations <= 0)):
            raise ValueError("'iterations' should be a positive integer.")
