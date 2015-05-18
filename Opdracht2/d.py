
string = input()
codeword = input()

i = 0
read = 0
mod = len(codeword)
stop = len(string)
result = []

while(i < stop):
	x = (ord(string[i]) - ord(codeword[i % mod])) % 26 + ord('a')
	i = i + 1
	result.append(chr(x))

	
str = ""
print(str.join(result))
