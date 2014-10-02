import problem1
import problem2

from matrix import Matrix

def main():
	
	m = 100
	L = 0.51302
	delta1 = 0.008
	delta2 = 0.004
	alpha = 2
	beta = 5.45
	
	problem2.calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta)

if __name__ == '__main__':
	main()
