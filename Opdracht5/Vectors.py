from math import sqrt
from array import array

class Vector:
	def __init__(self, number, content = 0):
		if isinstance(content, list) or isinstance(content, array):
			self.indices = array('d', content)
		else:
			self.indices = array('d', [content]*number)
	
	def __str__(self):
		result = []
		for i in range(len(self.indices)):
			result.append(self.indices[i])
		for t in range(len(result)):
			result[t] = "{:.6f}".format(result[t])	
		result = "\n".join(result)
		return result
		
	def lincomb(self, other, alpha, beta):
		result = []
		for i in range(len(self.indices)):
			result.append(alpha*self.indices[i] + beta * other.indices[i])
		return Vector(len(self.indices), result)
	
	def scalar(self, alpha):
		return self.lincomb(Vector(len(self.indices)), alpha, 0)
	
	def inner(self, other):
		result = []
		for t in range(len(self.indices)):
			result.append(self.indices[t]*other.indices[t])
		return sum(result)
		
	def norm(self):
		return sqrt(self.inner(self))
		
	
			