import sys
N = sys.stdin.readline()
set1 = set(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
lst = list(map(int, sys.stdin.readline().split()))

for i in lst:
    if i in set1:
        print(1, end=" ")
    else:
        print(0, end=" ")
