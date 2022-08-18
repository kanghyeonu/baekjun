import sys

N, M = map(int, sys.stdin.readline().split())

lst = [[0 for _ in range(N+1)]]
for _ in range(N):
    temp = [0]
    temp.extend(list(map(int, sys.stdin.readline().split())))
    lst.append(temp)

for i in range(1, N+1):
    for j in range(1, N + 1):
        lst[i][j] = lst[i][j-1] + lst[i-1][j] - lst[i-1][j-1] + lst[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = lst[x2][y2] - lst[x2][y1-1] - lst[x1-1][y2] + lst[x1-1][y1-1]
    print(ans)
