lstx = []
lsty = []

for i in range(3):
    a, b = map(int, input().split())
    lstx.append(a)
    lsty.append(b)

for i, j in zip(lstx, lsty):
    if lstx.count(i) == 1:
        a = i
    if lsty.count(j) == 1:
        b = j

print(a, b)