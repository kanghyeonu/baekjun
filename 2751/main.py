import sys
case = int(input())

lst = [int(sys.stdin.readline()) for _ in range(case)]

lst.sort()

for i in lst:
    print(i)