dial = input()

lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for i in dial:
    for j in lst:
        if i in j:
            time += lst.index(j) + 3

print(time)
