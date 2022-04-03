import numpy as np


class FourierTransform:
    count = 0

    @staticmethod
    def function_values(arguments):
        function_values = list(map(lambda x: np.cos(5 * x) + np.sin(6 * x), arguments))

        return function_values

    @staticmethod
    def dft(self, values, direction):
        self.count = 0

        n = len(values)
        out_values = [complex(0, 0)] * n

        for m in range(n):
            for k in range(n):
                out_values[m] += values[k] * np.exp(direction * complex(0, -1) * 2 * np.pi * m * k / n)
                self.count += 1
            if direction == -1:
                out_values[m] /= n

        return out_values

    @staticmethod
    def fft(self, in_values, direction):
        self.count = 0
        out_values = self.fft_realise(self, in_values, direction)

        if direction == -1:
            n = len(in_values)
            for i in range(n):
                out_values[i] /= n

        return out_values

    @staticmethod
    def fft_realise(self, values, direction):
        n = len(values)

        if n == 1:
            return values

        values_even = [complex(0, 0)] * (int(n / 2))
        values_odd = [complex(0, 0)] * (int(n / 2))

        for i in range(n):
            if i % 2 == 0:
                values_even[int(i / 2)] = values[i]
            else:
                values_odd[int(i / 2)] = values[i]

        b_even = self.fft_realise(self, values_even, direction)
        b_odd = self.fft_realise(self, values_odd, direction)

        w_n = complex(np.exp(direction * 2 * np.pi * complex(0, -1) / n))
        w = 1
        y = [complex(0, 0)] * n

        for i in range(int(n / 2)):
            y[i] = b_even[i] + b_odd[i] * w
            y[i + int(n / 2)] = b_even[i] - b_odd[i] * w
            w = w * w_n
            self.count += 1

        return y

    @staticmethod
    def shift(values):
        length = len(values)

        first_half = values[0:int(length / 2)]
        second_half = first_half[:]
        first_half.reverse()
        shifted_result = first_half + second_half

        return shifted_result
