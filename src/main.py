import problem1
import problem2
import problem3
import sys

def print_help():
	print('Uso: python3 main.py problema[ 1 | 2 | 3 ] m L delta1 delta2 alpha beta')
	print(' - Ejemplo: python3 main.py problema1 100 0.51302 0.008 0.004 2 5.45')

def main():
	
	if (len(sys.argv) != 8):
		print_help()
		return

		
	m = int(sys.argv[2])
	L = float(sys.argv[3])
	delta1 = float(sys.argv[4])
	delta2 = float(sys.argv[5])
	alpha = float(sys.argv[6])
	beta = float(sys.argv[7])
	
	option = sys.argv[1]
	
	if option == 'problema1':
		print('Ejecutando problema 1.')
		A = problem1.calculate_matrix_A(m, L, delta1, delta2, alpha, beta)
		print('Matriz A: (formato MatrixMarket .mtx)')
		A.print_as_list()
		
	elif option == 'problema2':
		print('Ejecutando problema 2.')
		egs = problem2.calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta)
		print('Autovalores de A:')
		for val in egs:
			print(val)
			
	elif option == 'problema3':
		print('Ejecutando problema 3.')
		egs = problem3.calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta)
		print('Autovalores de A:')
		for val in egs:
			print(val)
			
	else:
		raise Error()


if __name__ == '__main__':
	main()
