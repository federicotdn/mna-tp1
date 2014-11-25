from list_matrix_storage import ListMatrixStorage
from hash_matrix_storage import HashMatrixStorage

class MatrixException(Exception):
	pass

class Matrix:
	
	"""
	N x N square matrix
	"""
	
	def __init__(self, n = None, storage = None):
		if not storage:
			self._storage = ListMatrixStorage(n)
		else:
			self._storage = storage

	def __str__(self):
		mat_str = ''
		rows = []
		for i in range(self.size()):
			rows.append(self.get_row(i))
			
		for row in rows:
			mat_str += '| '
			for i in row:
				mat_str += str(i).center(5)
				mat_str += ' '
			mat_str += '|\n'
		
		return mat_str
	
	def get(self, row, col):
		return self._storage.get(row, col)
		
	def set(self, row, col, val):
		self._storage.set(row, col, val)
		
	def get_row(self, row):
		return self._storage.get_row(row)
		
	def get_col(self, col):
		return self._storage.get_col(col)
		
	def size(self):
		return self._storage.size()
	
	def transpose(self):
		mat = Matrix.copy(self)
		
		for i in range(mat.size()):
			for j in range(mat.size()):
				if i < j:
					val = mat.get(i, j)
					mat.set(i, j, mat.get(j, i))
					mat.set(j, i, val)
					
		return mat
				
	
	@classmethod
	def from_row_lists(cls, rows):
		row_count = len(rows)
		mat = cls(row_count)
		
		for i, row in enumerate(rows):
			if len(row) != row_count:
				raise MatrixException('List must contain N number of N-sized lists')
			
			for j, val in enumerate(row):
				mat.set(i, j, val)
				
		return mat
	
	@classmethod
	def from_col_lists(cls, cols):
		col_count = len(cols)
		mat = cls(col_count)
		
		for j, col in enumerate(cols):
			if len(col) != col_count:
				raise MatrixException('List must contain N number of N-sized lists')
		
			for i, val in enumerate(col):
				mat.set(i, j, val)
		
		return mat
	
	@classmethod
	def from_mat_lists(cls, matrices):
		row_count = len(matrices)
		mat_sizes = matrices[0][0].size()
		
		mat = cls(row_count * mat_sizes)
		
		for i, row in enumerate(matrices):
			if len(row) != row_count:
				raise MatrixException('List must contain N number of N-sized lists')
			
			for j, matrix in enumerate(row):
				if matrix.size() != mat_sizes:
					raise MatrixException('Every matrix must share the same size')
				
				mat.copy_from_matrix_offset(i * mat_sizes, j * mat_sizes, matrix)
		
		return mat
				
				
	def copy_from_matrix_offset(self, off_i, off_j, other):
		def copy_offset(i, j):
			val = other.get(i, j)
			self.set(off_i + i, off_j + j, val)
		
		other.for_each_pos(copy_offset)
	
	def print_as_list(self, skip_zeroes=True):
		print(self.size(), ' ', self.size())
		
		for j in range(self.size()):
			for i in range(self.size()):
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
					
			mat.set(i, j, val)
		
		mat.for_each_pos(fill_tridiagonal)
		
		return mat

	def for_each_pos(self, fn):
		for i in range(self.size()):
			for j in range(self.size()):
				fn(i, j)

	@classmethod
	def copy(cls, other):
		storage = other._storage.clone()
		mat = Matrix(other.size(), storage)
		
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
		if other.size() != self.size():
			raise MatrixException('Matrices must be the same size in order to add.')
		
		def add_values(i, j):
			val = self.get(i, j)
			val += other.get(i, j)
			self.set(i, j, val)
		
		self.for_each_pos(add_values)
		
		return self
		
	def __add__(self, other):
		if other.size() != self.size():
			raise MatrixException('Matrices must be the same size in order to add.')
		
		mat = Matrix.copy(self)
		mat.add(other)
		return mat
		
	def subtract(self, other):
		if other.size() != self.size():
			raise MatrixException('Matrices must be the same size in order to subtract.')
		
		def sub_values(i, j):
			val = self.get(i, j)
			val -= other.get(i, j)
			self.set(i, j, val)
		
		self.for_each_pos(sub_values)
		
		return self

	def get_diagonal(self):
		diag = []
		for i in range(self.size()):
			diag.append(self.get(i, i))

		return diag
		
	def shrink(self, n):
		self._storage.shrink(n)
		
	def __sub__(self, other):
		if other.size() != self.size():
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
			if other.size() != self.size():
				raise MatrixException('Matrices must be the same size in order to multiply.')
			
			mat = Matrix(self.size())
			
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
