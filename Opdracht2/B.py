

string = input().split()
first = int(string[0])
second = int(string[1])
third = string[2]

if(third == '+'):
	result = first + second
if(third == '-'):
	result = first - second
if(third == '*'):
	result = first * second
if(third == '/'):
	result = first / second

print("{0:.3f}".format(result)) 