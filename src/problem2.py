import math
import numpy

def calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta):
	"""
	From collection.ps
	"""
	
	h = 1.0 / (m + 1)
	
	tau1 = (1.0 / pow(h, 2)) * (delta1 / pow(L, 2))
	tau2 = (1.0 / pow(h, 2)) * (delta2 / pow(L, 2))
	
	t_eigs = []
	a_eigs = []
	a_eigs2 = []
	
	for j in range(m):
		val = -2 * (1 - math.cos(math.pi * (j + 1) * h))
		t_eigs.append(val)
		
	for j in range(m):
		coeffs = []
		coeffs.append(1)
		
		val = pow(alpha, 2) - (beta - 1) - (tau1 + tau2) * t_eigs[j]
		coeffs.append(val)
		
		val = (beta * pow(alpha, 2)) + (tau1 * tau2 * pow(t_eigs[j], 2)) + (tau2 * (beta - 1) * t_eigs[j]) - \
			(pow(alpha, 2) * tau1 * t_eigs[j]) - (pow(alpha, 2) * (beta - 1))
		coeffs.append(val)

		d = numpy.roots(coeffs)
		
		a_eigs.append(d[0])
		a_eigs2.append(d[1])
		
	return a_eigs + a_eigs2
		
