from matrix import Matrix
from problem1 import calculate_matrix_A
from vector import Vector
import math
import numpy
import time

def calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta):
	A = calculate_matrix_A(m, L, delta1, delta2, alpha, beta)
	B = [[2.261463012947533, 1.0942684935262337, 0, 0, 0, 4.0, 0, 0, 0, 0],
		[1.0942684935262337, 2.261463012947533, 1.0942684935262337, 0, 0, 0, 4.0, 0, 0, 0],
		[0, 1.0942684935262337, 2.261463012947533, 1.0942684935262337, 0, 0, 0, 4.0, 0, 0],
		[0, 0, 1.0942684935262337, 2.261463012947533, 1.0942684935262337, 0, 0, 0, 4.0, 0],
		[0, 0, 0, 1.0942684935262337, 2.261463012947533, 0, 0, 0, 0, 4.0],
		[-5.45, 0, 0, 0, 0, -5.094268493526234, 0.5471342467631168, 0, 0, 0],
		[0, -5.45, 0, 0, 0, 0.5471342467631168, -5.094268493526234, 0.5471342467631168, 0, 0],
		[0, 0, -5.45, 0, 0, 0, 0.5471342467631168, -5.094268493526234, 0.5471342467631168, 0],
		[0, 0, 0, -5.45, 0, 0, 0, 0.5471342467631168, -5.094268493526234, 0.5471342467631168],
		[0, 0, 0, 0, -5.45, 0, 0, 0, 0.5471342467631168, -5.094268493526234]]
	e, n = numpy.linalg.eig(B)
	print(e)
	print('\n----------------------------------------------------------------------------\n')

	start_time = time.time()

	n = A.size()
	eigs = []
	while n != 1 and n != 2:
		Q = calculate_Q(A)
		A = Q.transpose() * A * Q
		if( abs(A.get(n-1, n-2)) < 0.0000000000001):
			eigs.append(A.get(n-1, n-1))
			n -=1
			A.shrink(1)
		elif abs(A.get(n-2, n-3)) < 0.0000000000001:
			eigs.extend(get_egien_man(A,n-1,n-1))
			n-=2
			A.shrink(2)
	if (n ==1):
		eigs.append(A.get(0,0))
	else:
		eigs.extend(get_egien_man(A, 1,1))
		
	elapsed = time.time() - start_time
	print('Tiempo tardado: ' + '{:.10f}'.format(elapsed) + ' segundos.')
	
	return eigs

def calculate_Q(mat):
	q_list = [Vector(mat.get_col(0)).normalize()]

	for i in range(1, mat.size()):
		vector = Vector(mat.get_col(i))

		aux_vec = Vector([0] * mat.size())
		for j in range(i):
			aux_vec += q_list[j] * vector.dot_product(q_list[j])

		e = vector - aux_vec
		q_list.append(e.normalize())

	return Matrix.from_col_lists([x.get_values() for x in q_list])

def get_egien_man(mat, row, col):
	a = mat.get(row-1, col-1)
	b = mat.get(row-1, col)
	c = mat.get(row, col-1)
	d = mat.get(row, col)
	eg = numpy.roots([1, -d -a, (a*d) - (b*c)])
	return eg

def get_eigenvalues(mat):
	values = []
	skip = False
	for i in range(1, mat.size()):
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
		values.append(mat.get(mat.size() -1 , mat.size() -1))

	return values

			


	
