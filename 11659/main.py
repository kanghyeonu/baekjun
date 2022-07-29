import sys

N, M = map(int, sys.stdin.readline().split())
lst = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, N+1):
    lst[i] = lst[i-1] + lst[i]

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(lst[e]-lst[s-1])