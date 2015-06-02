horizontal = [2,6,5, 1]
horizontalindex = 1
vertical = [1, 4, 6, 3]
verticalindex = 2
target = 6

n = int(input())

for t in range(0,n):
	string = input()
	if(string == 'omhoog'):
		verticalindex = (verticalindex - 1) % 4
		target = vertical[verticalindex]
		horizontal[horizontalindex] = target
	if(string == 'omlaag'):
		verticalindex = (verticalindex + 1) % 4
		target = vertical[verticalindex]
		horizontal[horizontalindex] = target
	if(string == 'rechts'):
		horizontalindex = (horizontalindex - 1) % 4
		target = horizontal[horizontalindex]
		vertical[verticalindex] = target
	if(string == 'links'):
		horizontalindex = (horizontalindex + 1) % 4
		target = horizontal[horizontalindex]
		vertical[verticalindex] = target
		
print(target)