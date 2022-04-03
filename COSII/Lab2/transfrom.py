import numpy as np


class Transform:
    counter = 0

    @staticmethod
    def fft(self, in_values, direction):
        self.counter = 0
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
            self.counter += 1

        return y
