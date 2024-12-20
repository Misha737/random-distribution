import numpy as np

class Distribution:
    def __init__(self, values: list[int], quantities: list[int] = None):
        self.values = np.array(values)
        self.is_probably = False

        if quantities is not None and len(quantities) != len(values):
            raise Exception('The size of the vectors is not equal')

        if quantities is None:
            self.quantities = np.ones(len(values), dtype=int)
            self.sum = len(values)
        else:
            self.quantities = np.array(quantities)
            self.sum = np.sum(self.quantities)
            if self.sum == 1:
                self.is_probably = True

        self.probably = self.quantities / self.sum

    def expected_value(self) -> float:
        return float(self.values.dot(self.probably))

    def variance(self):
        square_values = np.square(self.values)
        expected_square_value = float(square_values.dot(self.probably))
        return expected_square_value - np.square(self.expected_value())