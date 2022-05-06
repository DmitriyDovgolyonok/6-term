#include <iostream>
#include <iomanip>
#include <immintrin.h>
#include <windows.h>
#include <ctime>
#include <chrono>

#define SIZE 100
#define x 16;
using namespace std;
using namespace chrono;

void fill_matrix(size_t height, size_t width, double** matrix, int key) {
	srand(clock() + key);
	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			matrix[i][j] = 1 + rand() % 15;
		}
	}
}

void no_vec_mul(int height_A, int width_B, int width_A, double** A, double** B, double** C) {
	auto start = chrono::high_resolution_clock::now();
	for (int i = 0; i < height_A; i++)
	{
		double* c = C[i];
		for (int k = 0; k < width_A; k++)
		{
			const double* b = B[k];
			double a = A[i][k];
#pragma loop(no_vector)
			for (int j = 0; j < width_B; j++)
				c[j] += a * b[j];
		}
	}
	auto end = chrono::high_resolution_clock::now();
	chrono::duration<double> result = end - start;
	cout << "Without vec mul: " << result.count() << " seconds" << endl;
}

void vec_mul(int height_A, int width_B, int width_A, double** A, double** B, double** C) {
	auto start = chrono::high_resolution_clock::now();
	for (int i = 0; i < height_A; i++)
	{
		double* c = C[i];
		for (int k = 0; k < width_A; k++)
		{
			const double* b = B[k];
			double a = A[i][k];
			for (int j = 0; j < width_B; j++)
				c[j] += a * b[j];
		}
	}
	auto end = chrono::high_resolution_clock::now();
	chrono::duration<double> result = end - start;
	cout << "Vec mul: " << result.count() << " seconds" << endl;
}

void AVX(int height_A, int width_B, int width_A, double** A, double** B, double** C) {
	auto start = chrono::high_resolution_clock::now();
	for (int i = 0; i < height_A; i++)
	{
		double* c = C[i];
		for (int k = 0; k < width_A; k++)
		{
			const double* b = B[k];
			const double a = A[i][k];
			for (int j = 0; j < width_B; j += 8) {
				_mm256_storeu_pd(c + j, _mm256_add_pd(_mm256_loadu_pd(c + j), _mm256_mul_pd(_mm256_set1_pd(a), _mm256_loadu_pd(b + j))));
			}
		}
	}
	auto end = chrono::high_resolution_clock::now();
	chrono::duration<double> result = end - start;
	cout << "AVX mul: " << result.count() << " seconds" << endl;
}

bool is_equal(double** matrix_C, double** matrix_AVX) {
	for (int i = 0; i < SIZE * 16; i++)
		for (int j = 0; j < SIZE * 16; j++)
		{
			if (matrix_C[i][j] == matrix_AVX[i][j])
				return TRUE;
			else
				return FALSE;
		}
}

int main() {
	double** matrix_A, **matrix_B, **matrix_C, **matrix_AVX;

	matrix_A = new double* [SIZE * 16];
	for (int i = 0; i < SIZE * 16; i++) {
		matrix_A[i] = new double[SIZE * 16];
		ZeroMemory(matrix_A[i], SIZE * 16 * sizeof(double));
	}

	matrix_B = new double* [SIZE * 16];
	for (int i = 0; i < SIZE * 16; i++) {
		matrix_B[i] = new double[SIZE * 16];
		ZeroMemory(matrix_B[i], SIZE * 16 * sizeof(double));
	}

	matrix_C = new double* [SIZE * 16];
	for (int i = 0; i < SIZE * 16; i++) {
		matrix_C[i] = new double[SIZE * 16];
		ZeroMemory(matrix_C[i], SIZE * 16 * sizeof(double));
	}

	matrix_AVX = new double* [SIZE * 16];
	for (int i = 0; i < SIZE * 16; i++) {
		matrix_AVX[i] = new double[SIZE * 16];
		ZeroMemory(matrix_AVX[i], SIZE * 16 * sizeof(double));
	}

	fill_matrix(SIZE * 16, SIZE * 16,matrix_A, 15);
	fill_matrix(SIZE * 16, SIZE * 16,matrix_B, 40);

	no_vec_mul(SIZE * 16, SIZE * 16, SIZE * 16, matrix_A, matrix_B, matrix_C);

	for (int i = 0; i < SIZE * 16; i++)
		ZeroMemory(matrix_C[i], SIZE * 16 * sizeof(double));

	AVX(SIZE * 16, SIZE * 16, SIZE * 16, matrix_A, matrix_B, matrix_AVX);
	vec_mul(SIZE * 16, SIZE * 16, SIZE * 16, matrix_A, matrix_B, matrix_C);

	if (is_equal(matrix_C, matrix_AVX) == TRUE) {
		cout << endl << "equal!";
	}
	else
	{
		cout << endl <<"not equal!";
	}




	

	return 0;
}