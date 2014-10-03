import math

class Vector:

	def __init__(self, values):
		self._values = values

	def normalize(self):
		total = 0
		for i in self._values:
			total += i**2
		norm = math.sqrt(total)
		return Vector([x/norm for x in self._values])

	def dot_product(self, other):
		total = 0
		for i, j in zip(self._values, other._values):
			total += i*j
		return total

	def __add__(self, other):
		return Vector([x+y for x,y in zip(self._values, other._values)])

	def __iadd__(self, other):
		return self + other

	def __sub__(self, other):
		return Vector([x - y for x,y in zip(self._values, other._values)])

	def __isub__(self, other):
		return self - other

	def __mul__(self, num):
		return Vector([x*num for x in self._values])

	def __truediv__(self, num):
		return self * (1/num)

	def get_values(self):
		return self._values

	def __str__(self):
		return str(self._values)

