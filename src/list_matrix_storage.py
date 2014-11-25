from matrix_storage import MatrixStorage
import copy

class ListMatrixStorage(MatrixStorage):
	def __init__(self, n, values = None):
		self._size = n
		
		if not values:
			self._rows = []
			for i in range(n):
				row = []
				for j in range(n):
					row.append(0)
					
				self._rows.append(row)
		else:
			self._rows = values
		
	def get(self, i, j):
		if i < 0 or j < 0:
			raise IndexError()
		return self._rows[i][j]
		
	def set(self, i, j, val):
		self._rows[i][j] = val
		
	def get_row(self, i):
		return self._rows[i]
		
	def get_col(self, j):
		col = []
		for row in self._rows:
			col.append(row[j])
			
		return col
		
	def size(self):
		return self._size
		
	def clone(self):
		vals = copy.deepcopy(self._rows)
		st = ListMatrixStorage(self.size(), vals)
		return st
		
	def shrink(self, n):
		for i in range(0, len(self._rows) - n):
			self._rows[i] = self._rows[i][:-n]
		self._rows = self._rows[:-n]
		self._size -= n

