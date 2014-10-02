import math

def calculate_eigenvalues_A(m, L, delta1, delta2, alpha, beta):
	"""
	From collection.ps
	"""
	
	h = 1.0 / (m + 1)
	
	tau1 = (1.0 / pow(h, 2)) * (delta1 / pow(L, 2))
	tau2 = (1.0 / pow(h, 2)) * (delta2 / pow(L, 2))
	
	t_eigs = []
		
	for j in range(m):
		val = -2 * (1 - math.cos(math.pi * (j + 1) * h))
		t_eigs.append(val)
		
	
