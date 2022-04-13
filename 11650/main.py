case = int(input())

lst = []
for _ in range(case):
    x, y = map(int, input().split())
    lst.append((x, y))

lst.sort()

for i in range(case):
    print(lst[i][0], lst[i][1])