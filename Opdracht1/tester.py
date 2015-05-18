number = int(input('Hoe veel bier?'))

strings = []
i = 0

while i < number:
	strings.add(input())
	i = i + 1

i = 0
while i < number:
	n = len(strings[i])
	k = 0
	spaces = 0
	while k < n:
		if(strings[i][k] == ' '):
			spaces = spaces + 1
		k = k + 1
	if(spaces > 2):
		print('Crackers!')
	else:
		print(strings[i] + 'krAh!')
		
		
string = input()
			