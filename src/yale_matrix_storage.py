from matrix_storage import MatrixStorage

class YaleMatrixStorage(MatrixStorage):
	def __init__(self, n):
		self._size = n
		self._A = []
		self._IA = [ 0 ] * (n + 1)
		self._JA = []
		
	def get_with_offset(self, i, j):
		i1, i2 = self.ia_pair(i)
		if i2 - i1 == 0:
			return 0, 0
		
		offset = 0
		val = 0
		
		for col in range(i1, i2):
			stored_j = self._JA[col]
			if stored_j == j:
				val = self._A[col]
				break
			elif stored_j > j:
				break
			
			offset += 1
			
		return val, offset
		
	def get(self, i, j):
		return self.get_with_offset(i, j)[0]
		
	def ia_pair(self, i):
		index1 = self._IA[i]
		index2 = self._IA[i + 1]
		return index1, index2
		
	def set(self, i, j, val):
		i1, i2 = self.ia_pair(i)
		old_val, offset = self.get_with_offset(i, j)
		
		if old_val != 0:
			if val != 0:
				self._A[i1 + offset] = val
				self._JA[i1 + offset] = j
			else:
				del self._A[i1 + offset]
				del self._JA[i1 + offset]
				for row in range(i + 1, len(self._IA)):
					self._IA[row] -= 1
		else:
			if val != 0:
				self._A.insert(i1 + offset, val)
				self._JA.insert(i1 + offset, j)
				for row in range(i + 1, len(self._IA)):
					self._IA[row] += 1
			
	def print_info(self):
		print('A: ' + str(self._A))
		print('IA: ' + str(self._IA))	
		print('JA: ' + str(self._JA))	
			
		
	def get_row(self, i):
		i1, i2 = self.ia_pair(i)
		row = [ 0 ] * self._size
		
		for col in range(i1, i2):
			stored_j = self._JA[col]
			stored_val = self._A[col]
			row[stored_j] = stored_val
		
		return row

	def get_quick_row(self, i):
		i1, i2 = self.ia_pair(i)
		row = []
		
		for col in range(i1, i2):
			stored_j = self._JA[col]
			stored_val = self._A[col]
			row.append((stored_j, stored_val))
		
		return row
		
	def get_col(self, j):
		col = [ 0 ] * self._size
		current_row = 0
		
		for index, stored_j in enumerate(self._JA):
			if stored_j == j:
				i1, i2 = self.ia_pair(current_row)
				
				while not index in range(i1, i2):
					current_row += 1
					i1, i2 = self.ia_pair(current_row)
					
				col[current_row] = self._A[index]
				current_row += 1

		return col

	def get_quick_col(self, j):
		col = []
		current_row = 0
		for index, stored_j in enumerate(self._JA):
			if stored_j == j:
				i1, i2 = self.ia_pair(current_row)
				
				while not index in range(i1, i2):
					current_row += 1
					i1, i2 = self.ia_pair(current_row)
					
				col.append((current_row,self._A[index]))
				current_row += 1

		return col

	def size(self):
		return self._size

	def clone(self):
		st = YaleMatrixStorage(self.size())
		st._A = self._A[:]
		st._IA = self._IA[:]
		st._JA = self._JA[:]
		return st

	def shrink(self, n):
		for _ in range(n):
			i1, i2 = self.ia_pair(self._size - 1)
			self._A = self._A[:i1]
			self._JA = self._JA[:i1]
			self._IA = self._IA[:-1]
			
			to_remove = []
			
			current_row = 0
			for index, stored_j in enumerate(self._JA):
				if stored_j == self._size - 1:
					i1, i2 = self.ia_pair(current_row)
					
					while not index in range(i1, i2):
						current_row += 1
						i1, i2 = self.ia_pair(current_row)
						
					to_remove.append((index, current_row))
					current_row += 1
		
		
			counter = 0
			for index, row in to_remove:
				del self._A[index - counter]	
				del self._JA[index - counter]
				counter += 1
				
				for i in range(row + 1, len(self._IA)):
					self._IA[i] -= 1

				
				
			self._size -= 1
