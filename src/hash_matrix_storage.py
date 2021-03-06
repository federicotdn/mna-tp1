from matrix_storage import MatrixStorage

class HashMatrixStorage(MatrixStorage):
	def __init__(self, n):
		self._size = n
		self._vals = {}
		
	def get(self, i, j):
		key = hash((i, j))
		if key in self._vals:
			return self._vals[key]
		else:
			return 0
		
	def set(self, i, j, val):
		if val != 0:
			self._vals[hash((i, j))] = val
		else: 
			self.delete(i, j)
		
	def get_row(self, i):
		row = []
		for j in range(self._size):
			row.append(self.get(i, j))
			
		return row

	def get_quick_row(self,i):
		row=[]
		for j in range(self._size):
			val = self.get(i, j)
			if val:
				row.append((j,val))
		return row
		
	def get_col(self, j):
		col = []
		for i in range(self._size):
			col.append(self.get(i, j))
			
		return col

	def get_quick_col(self, j):
		col = []
		for i in range(self._size):
			val = self.get(i, j)
			if val:
				col.append((i, val))
			
		return col 
		
	def size(self):
		return self._size
		
	def clone(self):
		st = HashMatrixStorage(self.size())
		st._vals = self._vals.copy()
		return st

	def delete(self, i, j):
		key = hash((i, j))
		self._vals.pop(key, None)

	def shrink(self, n):
		for i in range(self._size - n):
			for j in range(self._size - n, self._size):
				self.delete(i, j)
				
		for i in range(self._size - n, self._size):
			for j in range(self._size):
				self.delete(i, j)
		
		self._size -= n
