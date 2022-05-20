import sys

N, M = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N):
    lst.append(sys.stdin.readline().strtip())
set1 = set(lst)
cnt = 0
for _ in range(M):
    string = sys.stdin.readline().strtip()
    if string in set1:
        cnt += 1

print(cnt)