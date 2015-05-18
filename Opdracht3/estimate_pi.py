import sys
import math
import random


N   = int(sys.argv[1])
L   = int(sys.argv[2])
t   = 0
hit = 0

while t < N:
	x   =  random.random()
	phi =  random.vonmisesvariate(0,0)
	x   += L * math.cos(phi)
	t   += 1
	if x < 0 or x > 1:
		hit += 1
		
p = (2 * L * N) / hit
		
print("%d hits in %d tries" %(hit, N))
print("Pi = " + str(p))

