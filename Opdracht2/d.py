
string = input()
codeword = input()[0]

i = 0
read = 0
mod = len(codeword)
stop = len(string)
result = []

while(i < stop):
	x = ord(string[i]) - 97
	offset = ord(codeword[read]) - 97
	result.append(chr((x + offset) % 26 + 97))
	i = i + 1
	read = read + 1 % mod
str = ""
print(str.join(result))
