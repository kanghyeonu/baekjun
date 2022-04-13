import sys
case = int(input())
lst = []
for _ in range(case):
    age, name = sys.stdin.readline().split()
    lst.append((int(age), name))

lst = sorted(lst, key=lambda x: x[0])

for i in lst:
    print(i[0], i[1])