import numpy as np

class Distribution:
    def __init__(self, value: list[int], numbers: list[int] = None):
        self.value = np.array(value)

        if numbers is not None and len(numbers) != len(value):
            raise Exception('The size of the vectors is not equal')

        if numbers is None:
            self.numbers = np.ones(len(value), dtype=int)
            self.sum = len(value)
        else:
            self.numbers = np.array(numbers)
            self.sum = np.sum(self.numbers)
        self.probably = self.numbers / self.sum

    def expected_value(self) -> float:
        return float(self.value.dot(self.probably))

    def variance(self):
        square_values = np.square(self.value)
        expected_square_value = float(square_values.dot(self.probably))
        return expected_square_value - np.square(self.expected_value())