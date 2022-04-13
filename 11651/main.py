import sys
case = int(input())
lst = []
for _ in range(case):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((y, x))
lst.sort()

for i in range(len(lst)):
    print(lst[i][1], lst[i][0])