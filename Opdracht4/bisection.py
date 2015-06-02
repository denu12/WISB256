import math

def findRoot(func, a, b, e):
	m = a + (float(b) - float(a)) / 2.0
	if((b - a) / 2 <= e):
		return m
	else:
		if( (func(m) > 0 and func(a) < 0) or (func(a) > 0 and func(m) < 0)):
			return findRoot(func, a, m, e)
		else:
			return findRoot(func, m, b, e)
	
	
def f1(x):
	return math.sin(1/x)
	
print(findRoot(f1, 0.1, 1, 0.0001))
	

