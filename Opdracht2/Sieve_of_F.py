import sys
import time
import math
T1 = time.time()

N = int(sys.argv[1])




PrimeList = [True]*N

for t in range(1, N+1):
	PrimeList.append(t)

for j in range(1, N):
	for i in range(1, j + 1):
		x = i + j + 2*i*j
		if(x <= N):
			PrimeList.remove(x)

result = []

for int in PrimeList:
	result.append(2*int + 1)


T2 = time.time()	

number = 0
f = open(str(sys.argv[2]), 'w')
for p in result:
	f.write(str(p) + '\n')
	
		

print('number of primes', len(result))
#print('number of primes', len(Result))
print('Time required', T2 - T1, 'sec.')