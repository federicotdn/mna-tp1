from matrix import Matrix

def calculate_matrix_A(m, L, delta1, delta2, alpha, beta):
	h = 1.0 / (m + 1)
	
	T = Matrix.toeplitz_tridiagonal(m, 1, -2, 1)
	I = Matrix.identity(m)
	
	tau1 = (1.0 / pow(h, 2)) * (delta1 / pow(L, 2))
	tau2 = (1.0 / pow(h, 2)) * (delta2 / pow(L, 2))
	
	mat11 = (T * tau1) + (I * (beta - 1))
	mat12 = (I * pow(alpha, 2))
	mat21 = (I * -beta)
	mat22 = (T * tau2) - (I * pow(alpha, 2))
	
	mat_list = [[ mat11, mat12 ], [ mat21, mat22 ]]

	return Matrix.from_mat_lists(mat_list)
