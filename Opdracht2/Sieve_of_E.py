import sys
import time
import math
T1 = time.time()

N = int(sys.argv[1])




"""
PrimeList = []
for i in range(2,N):
	d = True
	for p in PrimeList:
		d = d and i % p != 0
	if d:
		PrimeList.append(i)
T2 = time.time()
"""
PrimeList = [True]*N
for p in range(2, math.ceil(math.sqrt(N))):
	if PrimeList[p]:
		for i in range(p*p, N, p):
			PrimeList[i] = False
			
			
T2 = time.time()	
number = 0
f = open(str(sys.argv[2]), 'w')
for p in range(2, N):
	if PrimeList[p]:
		number += 1
		f.write(str(p) + '\n')
	
		

print('number of primes', number)
#print('number of primes', len(PrimeList))
print('Time required', T2 - T1, 'sec.')