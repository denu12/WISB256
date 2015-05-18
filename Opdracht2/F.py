n = int(input())
string = input()
result = 0
people = 0


	
people = int(string[0])
for t in range(1,n + 1):
	if (int(string[t]) != 0) and (t - people) > 0:
		result = result + (t - people)
		people = people + t - people
	people = people + int(string[t])
	
print(result)