import sys
import time
import math



T1 = time.perf_counter()
PrimeList = []

for i in range(1,int(sys.arv[1])):
	d = True
	for p in PrimeList:
		d = d and i % p != 0
	if d:
		PrimeList.add(i)

		
f = open(string(sys.arv[2]), 'w')
for p in PrimeList:
    f.write(p + '\n')
	
		
T2 = time.perf_counter()
print('Time required', T2 - T1, 'sec.')