class MatrixException(Exception):
	pass

class Matrix:
	
	"""
	N x N square matrix
	"""
	
	def __init__(self, n):
		self._rows = []
		self._size = n
		
		for i in range(n):
			row = []
			for j in range(n):
				row.append(0)
				
			self._rows.append(row)

	def __str__(self):
		mat_str = ''
		for row in self._rows:
			mat_str += '| '
			for i in row:
				mat_str += str(i)
				mat_str += ' '
			mat_str += '|\n'
		
		return mat_str
	
	def get(self, row, col):
		return self._rows[row][col]
	
	@classmethod
	def toeplitz_tridiagonal(cls, n, c, d, e):
		mat = cls(n)
		
		for i in range(n):
			for j in range(n):
				val = 0
				
				if i == j:
					val = d
				elif i == j + 1:
					val = c
				elif i + 1 == j:
					val = e
					
				mat._rows[i][j] = val
		
		return mat

	@classmethod
	def identity(cls, n):
		mat = cls(n)
		
		for i in range(n):
			for j in range(n):
				if i == j:
					mat._rows[i][j] = 1
					
		return mat

	def add(self, other):
		if other._size != self._size:
			raise MatrixException('Matrices must be the same size to add.')
		
		for i in range(self._size):
			for j in range(self._size):
				self._rows[i][j] += other.get(i, j)
		
		return self
