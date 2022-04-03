from functions import Functions
import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 8
    arguments = np.arange(0, n) * np.pi / 10
    function_y = list(map(lambda x: np.cos(5 * x), arguments))
    function_z = list(map(lambda x: np.sin(6 * x), arguments))

    basic_correlation = Functions.basic_correlation(function_y, function_z, 1)
    print('Сложность обычной корреляции: {}'.format(Functions.counter))
    basic_convolution = Functions.basic_correlation(function_y, function_z, -1)
    print('Сложность обычной свертки: {}'.format(Functions.counter))

    fft_based_correlation = Functions.fft_based_correlation(function_y, function_z, 1)
    print('Сложность корреляции на основе БПФ:'.format(Functions.counter))
    fft_based_convolution = Functions.fft_based_correlation(function_y, function_z, -1)
    print('Сложность свертки на основе БПФ: {}'.format(Functions.counter))

    _, represent = plt.subplots(3, 2)

    represent[0, 0].plot(arguments, function_y)
    represent[0, 0].set(title = 'y=cos(5x)')
    represent[0, 0].grid(True)

    represent[0, 1].plot(arguments, function_z)
    represent[0, 1].set(title = 'z=sin(6x)')
    represent[0, 1].grid(True)

    represent[1, 0].plot(arguments, basic_correlation)
    represent[1, 0].set(title = 'Стандартный метод корреляции')
    represent[1, 0].grid(True)

    represent[1, 1].plot(arguments, basic_convolution)
    represent[1, 1].set(title = 'Стандартный метод свертки')
    represent[1, 1].grid(True)

    represent[2, 0].plot(arguments, fft_based_correlation)
    represent[2, 0].set(title = 'Корреляция на основе БПФ')
    represent[2, 0].grid(True)

    represent[2, 1].plot(arguments, fft_based_convolution)
    represent[2, 1].set(title = 'Свертка на основе БПФ')
    represent[2, 1].grid(True)

    plt.subplots_adjust(wspace = 1, hspace = 1)

    plt.show()


if __name__ == '__main__':
    main()
