import sys

#N: 듣도 못한 사람, M: 보도 못한 사람
N, M = map(int, sys.stdin.readline().split())
s1 = set()

for _ in range(N):
    s1.add(sys.stdin.readline().strip())
s2 = set()
for _ in range(M):
    s2.add(sys.stdin.readline().strip())

lst = sorted(list(s1 & s2))
print(len(lst))
for i in lst:
    print(i)