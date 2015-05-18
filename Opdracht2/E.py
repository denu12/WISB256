first = input()
second = input()
third = input()

strings = []
strings.append(first)
strings.append(second)
strings.append(third)

rows = []

for t in range (0,3):
	temp = []
	for i in range(0,3):
		temp.append(int(strings[t][i]))
		
	rows.append(temp)
	
columns = []

for t in range (0,3):
	temp = []
	for i in range(0,3):
		temp.append(int(strings[i][t]))
	columns.append(temp)
	
cross = []
temp = []
temp.append(int(strings[0][0]))
temp.append(int(strings[1][1]))
temp.append(int(strings[2][2]))
cross.append(temp)

temp = []
temp.append(int(strings[0][2]))
temp.append(int(strings[1][1]))
temp.append(int(strings[2][0]))
cross.append(temp)

notsolved = True

for t in range (0,3):
	if( (sum(columns[t]) == 3 or sum(rows[t]) == 3) and notsolved):
		print("Player 1 wins")
		notsolved = False
	if( (sum(columns[t]) == 6 or sum(rows[t]) == 6) and notsolved):
		print("Player 2 wins")
		notsolved = False

for t in range (0, 2):
	if( (sum(cross[t]) == 3) and notsolved):
		print("Player 1 wins")
		notsolved = False
	if( (sum(cross[t]) == 6) and notsolved):
		print("Player 2 wins")
		notsolved = False
if(notsolved):
	print('No winner')
