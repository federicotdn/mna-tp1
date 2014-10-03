from matrix import Matrix
from problem1 import calculate_matrix_A
from vector import Vector
import math
import numpy

def calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta):
	A = calculate_matrix_A(m, L, delta1, delta2, alpha, beta)
	A = Matrix.from_row_lists([[2,3,6], [ 4 , 5,  8], [9, 0, 1]])
	prev_eigen = None
	while not prev_eigen or math.fabs(A.get(0,0) - prev_eigen) > 0.01:

		prev_eigen = A.get(0,0)

		Q = calculate_Q(A)
		A = Q.transpose() * A * Q
	return get_eigenvalues(A)

def calculate_Q(mat):
	q_list = [Vector(mat.get_col(0)).normalize()]

	for i in range(1, mat._size):
		vector = Vector(mat.get_col(i))

		aux_vec = Vector([0] * mat._size)
		for j in range(i):
			aux_vec += q_list[j] * vector.dot_product(q_list[j])

		e = vector - aux_vec
		q_list.append(e.normalize())

	return Matrix.from_col_lists([x.get_values() for x in q_list])

def get_eigenvalues(mat):
	values = []
	skip = False
	for i in range(1, mat._size):
		if not skip:
			if  math.fabs(mat.get(i, i -1)) > 0.00001:
				a = mat.get(i-1, i-1)
				b = mat.get(i-1, i)
				c = mat.get(i, i-1)
				d = mat.get(i, i)
				eg = numpy.roots([1, -d -a, (a*d) - (b*c)])
				values.extend(eg)
				skip = True
			else:
				values.append(mat.get(i - 1, i -1))
				skip = False
		else:
			skip = False
		

	if not skip:
		values.append(mat.get(mat._size -1 , mat._size -1))

	return values

			


	
