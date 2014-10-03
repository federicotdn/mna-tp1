from matrix_storage import MatrixStorage

class ListMatrixStorage(MatrixStorage):
	def __init__(self, n):
		self._rows = []
		self._size = n
		
		for i in range(n):
			row = []
			for j in range(n):
				row.append(0)
				
			self._rows.append(row)
		
	def get(self, i, j):
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
		

