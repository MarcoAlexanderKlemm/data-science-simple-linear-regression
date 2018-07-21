class SimpleLinearRegression():
    def __init__(self, possible_ms, possible_bs):
        self.possible_ms = possible_ms
        self.possible_bs = possible_bs
    def __get_y(self, m, b, x):
        return m * x + b
    def __calculate_error(self, m, b, datapoint):
        x_datapoint = datapoint[0]
        y_datapoint = datapoint[1]
        y_value = self.__get_y(m, b, x_datapoint)
        error = abs(y_value - y_datapoint)
        return error
    def __calculate_total_error(self, m, b, datapoints):
        total_error = 0
        for point in datapoints:
            total_error += self.__calculate_error(m, b, point)
        return total_error
    def get_linear_function(self, datapoints):
        smallest_error = float("inf")
        best_m = 0
        best_b = 0
        for m in self.possible_ms:
            for b in self.possible_bs:
                error = self.__calculate_total_error(m, b, datapoints)
                if error < smallest_error:
                    smallest_error = error
                    best_m = m
                    best_b = b
        return "y = f(x) = " + str(best_m) + "x + " + str(best_b) 
        
possible_ms = [round(m * 0.1,1) for m in range(-100, 101)]
possible_bs = possible_ms
datapoints = [(3, 7), (5, 10), (7, 8), (9, 10), (11, 9)]

simple_linear_regression = SimpleLinearRegression(possible_ms, possible_bs)
linear_function = simple_linear_regression.get_linear_function(datapoints)
print(linear_function)
