import math
import cmath
import time
import transform
import numpy as np
import matplotlib.pyplot as plt
from transform import FourierTransform


def main():
    n = 32
    arguments = np.arange(0, n) * np.pi / 10
    fun_values = FourierTransform.function_values(arguments)
    frequencies = [x for x in range(-int(n / 2), int(n / 2), 1)]

    dft_values = FourierTransform.dft(FourierTransform, fun_values, 1)
    i_dft_values = FourierTransform.dft(FourierTransform, dft_values, -1)

    for i in range(n):
        dft_values[i] /= n

    shifted_dft = FourierTransform.shift(dft_values)

    dft_pol = list(map(lambda x: cmath.polar(x), shifted_dft))

    dft_ph_value = []
    dft_amp_value = []

    for i in range(len(shifted_dft)):
        dft_amp_value.append(dft_pol[i][0])
        dft_ph_value.append(dft_pol[i][1])

    print('ДПФ число операций:', FourierTransform.count)

    fft_values = FourierTransform.fft(FourierTransform, fun_values, 1)
    i_fft_values = FourierTransform.fft(FourierTransform, fft_values, -1)

    for i in range(n):
        fft_values[i] /= n

    shifted_fft = FourierTransform.shift(fft_values)

    fft_pol = list(map(lambda x: cmath.polar(x), shifted_fft))

    fft_ph_value = []
    fft_amp_value = []

    for i in range(len(shifted_fft)):
        fft_amp_value.append(fft_pol[i][0])
        fft_ph_value.append(fft_pol[i][1])

    print('БПФ число операций:', FourierTransform.count)

    first, dff_x_arr = plt.subplots(2, 2, figsize = (6, 5))
    plt.tight_layout()

    dff_x_arr[0, 0].plot(arguments, fun_values)
    dff_x_arr[0, 0].set_title('Исходная функция')
    dff_x_arr[0, 0].grid(True)

    dff_x_arr[0, 1].stem(frequencies, dft_amp_value, markerfmt = ' ')
    dff_x_arr[0, 1].set_title('Амплитудный спектр ДПФ')
    dff_x_arr[0, 1].grid(True)

    dff_x_arr[1, 0].stem(frequencies, dft_ph_value, markerfmt = ' ')
    dff_x_arr[1, 0].set_title('Фазовый спектр ДПФ')
    dff_x_arr[1, 0].grid(True)

    dff_x_arr[1, 1].plot(arguments, i_dft_values)
    dff_x_arr[1, 1].set_title('Обратное преобразование ДПФ')
    dff_x_arr[1, 1].grid(True)

    second, fft_x_arr = plt.subplots(2, 2, figsize = (6, 5))
    plt.tight_layout()

    fft_x_arr[0, 0].plot(arguments, fun_values)
    fft_x_arr[0, 0].set_title('Исходная функция')
    fft_x_arr[0, 0].grid(True)

    fft_x_arr[0, 1].stem(frequencies, fft_amp_value, markerfmt = ' ')
    fft_x_arr[0, 1].set_title('Амплитудный спектр БПФ')
    fft_x_arr[0, 1].grid(True)

    fft_x_arr[1, 0].stem(frequencies, fft_ph_value, markerfmt = ' ')
    fft_x_arr[1, 0].set_title('Фазовый спектр БПФ')
    fft_x_arr[1, 0].grid(True)

    fft_x_arr[1, 1].plot(arguments, i_fft_values)
    fft_x_arr[1, 1].set_title('Обратное преобразование БПФ')
    fft_x_arr[1, 1].grid(True)

    plt.show()


if __name__ == '__main__':
    main()
