string = input()
s = set()

for i in range(1, len(string)+1):
    for j in range(0, len(string)):
        s.add(string[j:j + i])

print(len(s))