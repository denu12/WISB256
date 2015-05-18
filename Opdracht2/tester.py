cipher = input()
key = input()
plain = ""
for i in range(len(cipher)):
        plain += chr((ord(cipher[i]) - ord(key[i % (len(key))]) + 26) % 26 + 97)
print(plain)