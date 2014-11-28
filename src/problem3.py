from matrix import Matrix
from problem1 import calculate_matrix_A
from vector import Vector
import math
import numpy
import time

def calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta):
	A = calculate_matrix_A(m, L, delta1, delta2, alpha, beta)
	EPSILON = math.pow(10,-10)

	start_time = time.time()

	n = A.size()
	eigs = []
	while n != 1 and n != 2:
		Q, R = calculate_QR(A)
		A = R * Q
		if( cut_condition(EPSILON, A.get(n-1, n-2), A.get(n-2,n-2), A.get(n-1,n-1))):
			eigs.append(A.get(n-1, n-1))
			n -=1
			A.shrink(1)

		elif cut_condition(EPSILON, A.get(n-2, n-3),A.get(n-2,n-2), A.get(n-3,n-3)):
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

def cut_condition(tol, val, val2, val3):
	return abs(val) < (tol*(abs(val2) + abs(val3)))

def calculate_QR(mat):
	q_list = []
	R = Matrix(mat.size())

	for i in range(mat.size()):
		vector = Vector(mat.get_col(i))

		aux_vec = Vector([0] * mat.size())
		for j in range(i):
			prod = vector.dot_product(q_list[j])
			R.set(j,i, prod)
			aux_vec += q_list[j] * prod

		e = vector - aux_vec
		R.set(i,i,e.get_norm())
		q_list.append(e.normalize())

	return Matrix.from_col_lists([x.get_values() for x in q_list]), R

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

			


	
