import numpy as np
from transfrom import Transform


class Functions:
    counter = 0

    @staticmethod
    def basic_correlation(first_sequence, second_sequence, operation):
        if operation != 1 and operation != -1:
            raise Exception('Must equal to 1 for Correlation or -1 for Convolution. Got {}'.format(operation))
        length = len(first_sequence)

        if length != len(second_sequence):
            raise Exception("Sequences lengths must be equal!")

        Functions.counter = 0

        result = []
        for i in range(length):
            temp = 0
            for j in range(length):
                k = (i + (j * operation)) % length
                temp += first_sequence[j] * second_sequence[k]

                Functions.counter += 1

            result.append(temp)

        return result

    @staticmethod
    def fft_based_correlation(first_sequence, second_sequence, operation):
        if operation != 1 and operation != -1:
            raise Exception('Operation number must equal to'
                            '1(correlation) ot -1(convolution). Got {}!'.format(operation))

        length = len(first_sequence)

        if length != len(second_sequence):
            raise Exception("Sequences lengths must be equal!")

        Functions.counter = 0

        first_fft = Transform.fft(Transform, first_sequence, 1)
        Functions.counter += Transform.counter

        second_fft = Transform.fft(Transform, second_sequence, 1)
        Functions.counter += Transform.counter

        processed_first_fft = first_fft
        if operation == 1:
            processed_first_fft = np.conj(first_fft)

        temp = np.multiply(processed_first_fft, second_fft)
        Functions.counter += length

        result = Transform.fft(Transform, temp, -1)
        Functions.counter += Transform.counter

        return result
