from matrix import Matrix

def main():
	print('test')
	m = Matrix.identity(6)
	print(str(m))
	
	m2 = Matrix.toeplitz_tridiagonal(6, 1, -2, 1)
	m2.add(m).add(m)
	
	print(str(m2))

if __name__ == '__main__':
	main()
