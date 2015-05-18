n = int(input())

strings = []
for t in range(0,n):
	strings.append(input())

for t in range(0,n):
	string = strings[t].split()
	if(len(string) > 4):
		print('Crackers!')
	else:
		print(strings[t] + ' ' + 'krAh!')