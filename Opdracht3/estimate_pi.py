import sys
import math
import random


N   = int(sys.argv[1])
L   = int(sys.argv[2])
if(L < 0):
	sys.exit("Error L should be between 0 and 1")
t   = 0
hit = 0

while t < N:
	x   =  random.random()
	phi =  random.vonmisesvariate(0,0)
	x   += L * math.cos(phi)
	t   += 1
	if x < 0 or x > 1:
		hit += 1

if(L <=1):		
	p = (2 * L * N) / hit
else:
	p = (2*L - 2*(math.sqrt(L*L-1) + math.asin( 1 / L)))/( hit / N - 1)
		
print("%d hits in %d tries" %(hit, N))
print("Pi = " + str(p))

