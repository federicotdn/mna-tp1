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
				mat_str += str(i).center(5)
				mat_str += ' '
			mat_str += '|\n'
		
		return mat_str
	
	def get(self, row, col):
		return self._rows[row][col]
		
	def set(self, row, col, val):
		self._rows[row][col] = val
		
	def get_row(self, row):
		return self._rows[row]
		
	def get_col(self, col):
		column = []
		for row in self._rows:
			column.append(row[col])
			
		return column
	
	@classmethod
	def from_val_lists(cls, rows):
		row_count = len(rows)
		mat = cls(row_count)
		
		for i, row in enumerate(rows):
			if len(row) != row_count:
				raise MatrixException('List must contain N number of N-sized lists')
			
			for j, val in enumerate(row):
				mat.set(i, j, val)
				
		return mat
	
	@classmethod
	def from_mat_lists(cls, matrices):
		row_count = len(matrices)
		mat_sizes = matrices[0][0]._size
		
		mat = cls(row_count * mat_sizes)
		
		for i, row in enumerate(matrices):
			if len(row) != row_count:
				raise MatrixException('List must contain N number of N-sized lists')
			
			for j, matrix in enumerate(row):
				if matrix._size != mat_sizes:
					raise MatrixException('Every matrix must share the same size')
				
				mat.copy_from_matrix_offset(i * mat_sizes, j * mat_sizes, matrix)
		
		return mat
				
				
	def copy_from_matrix_offset(self, off_i, off_j, other):
		def copy_offset(i, j):
			val = other.get(i, j)
			self.set(off_i + i, off_j + j, val)
		
		other.for_each_pos(copy_offset)
	
	def print_as_list(self, skip_zeroes=True):
		print(self._size, ' ', self._size)
		
		for j in range(self._size):
			for i in range(self._size):
				val = self.get(i, j)
				if val != 0 or not skip_zeroes:
					print(str(i + 1).center(6), end='')
					print(str(j + 1).center(6), end='')
					print(str(val))


	@classmethod
	def toeplitz_tridiagonal(cls, n, c, d, e):
		mat = cls(n)
		
		def fill_tridiagonal(i, j):
			val = 0
				
			if i == j:
				val = d
			elif i == j + 1:
				val = c
			elif i + 1 == j:
				val = e
					
			mat._rows[i][j] = val
		
		mat.for_each_pos(fill_tridiagonal)
		
		return mat

	def for_each_pos(self, fn):
		for i in range(self._size):
			for j in range(self._size):
				fn(i, j)

	@classmethod
	def copy(cls, other):
		mat = cls(other._size)
		
		def copy_val(i, j):
			mat.set(i, j, other.get(i, j))
			
		mat.for_each_pos(copy_val)
		
		return mat

	@classmethod
	def identity(cls, n):
		mat = cls(n)
		
		def fill_identity(i, j):
			if i == j:
				mat.set(i, j, 1)
				
		mat.for_each_pos(fill_identity)	
		return mat

	def add(self, other):
		if other._size != self._size:
			raise MatrixException('Matrices must be the same size in order to add.')
		
		def add_values(i, j):
			self._rows[i][j] += other.get(i, j)
		
		self.for_each_pos(add_values)
		
		return self
		
	def __add__(self, other):
		if other._size != self._size:
			raise MatrixException('Matrices must be the same size in order to add.')
		
		mat = Matrix.copy(self)
		mat.add(other)
		return mat
		
	def subtract(self, other):
		if other._size != self._size:
			raise MatrixException('Matrices must be the same size in order to subtract.')
		
		def sub_values(i, j):
			self._rows[i][j] -= other.get(i, j)
		
		self.for_each_pos(sub_values)
		
		return self
		
	def __sub__(self, other):
		if other._size != self._size:
			raise MatrixException('Matrices must be the same size in order to subtract.')
		
		mat = Matrix.copy(self)
		mat.subtract(other)
		return mat
	
	def multiply_scalar(self, k):
		def multiply_scalar_vals(i, j):
			val = self.get(i, j)
			self.set(i, j, val * k)
			
		self.for_each_pos(multiply_scalar_vals)
		return self
	
	def __mul__(self, other):
		if isinstance(other, Matrix):			
			if other._size != self._size:
				raise MatrixException('Matrices must be the same size in order to multiply.')
			
			mat = Matrix(self._size)
			
			def multiply_values(i, j):
				row = self.get_row(i)
				col = other.get_col(j)
				total = 0
				
				for v1, v2 in zip(row, col):
					total += v1 * v2
					
				mat.set(i, j, total)
				
			mat.for_each_pos(multiply_values)
			return mat
		
		else:
			mat = Matrix.copy(self)
			return mat.multiply_scalar(other)
