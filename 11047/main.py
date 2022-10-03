import sys

N, K = map(int, sys.stdin.readline().split())

lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

cnt = 0
idx = N - 1
while K > 0:
    cnt += K // lst[idx]
    K = K % lst[idx]
    idx -= 1

print(cnt)