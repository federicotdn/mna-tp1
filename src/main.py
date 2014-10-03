import problem1
import problem2
import problem3

from matrix import Matrix

def main():
	
	m = 2
	L = 0.51302
	delta1 = 0.008
	delta2 = 0.004
	alpha = 2
	beta = 5.45
	
	mt = Matrix.identity(4)
	m2 = Matrix.toeplitz_tridiagonal(4, 1, 3, -7)
	print(mt * m2)
	
	m3 = Matrix.from_row_lists([[1, 2], [3, 4]])
	m4 = Matrix.from_row_lists([[2, 0], [1, 2]])
	print(m3 - m4)
	
	
	
	#A = problem1.calculate_matrix_A(m, L, delta1, delta2, alpha, beta)
	#print(A)
	
	#egs = problem2.calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta)
	#print(egs)
	
	egs = problem3.calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta)
	print(egs)

if __name__ == '__main__':
	main()
