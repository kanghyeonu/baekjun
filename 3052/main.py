lst = []

for i in range(10):
    lst.append(int(input()))

r = []
for i in lst:
    if r.count(i%42) == 0:
        r.append(i%42)

print(len(r))