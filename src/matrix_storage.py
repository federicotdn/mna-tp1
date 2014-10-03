class MatrixStorage:
	def __init__(self, n):
		raise NotImplementedError()
		
	def get(self, i, j):
		raise NotImplementedError()
		
	def set(self, i, j, val):
		raise NotImplementedError()
		
	def get_row(self, i):
		raise NotImplementedError()
		
	def get_col(self, j):
		raise NotImplementedError()

	def size(self):
		raise NotImplementedError()

	def clone(self):
		raise NotImplementedError()
