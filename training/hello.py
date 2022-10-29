s = "hello world"
for i in range(len(s)):
    print(" " * i + s[:i + 1])

for i in range(len(s) - 1, -1, -1):
    print(" " * i + s[::-1][i:] + (" " * (len(s) - 1)) + s[i:])