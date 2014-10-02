from matrix import Matrix
from problem1 import calculate_matrix_A

def calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta):
	A = calculate_matrix_A(m, L, delta1, delta2, alpha, beta)


def calculate_Q(mat):
	q_list = [Vector(mat.get_col(0)).normalize()]


	for i in range(1, mat._size):
		vector = Vector(mat.get_col(i))

		aux_vec = Vector([0] * mat._size)
		for j in range(i)
			aux_vec += q_list[j] * vector.dot_product(q_list[j])

		e = vector - aux_vec
		q_list.append(e.normalize)


	
