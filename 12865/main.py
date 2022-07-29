import sys

N, K = map(int, sys.stdin.readline().split())

lst = [[0, 0]]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for _ in range(K):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1):
    w = lst[i][0]
    v = lst[i][1]
    for j in range(1, K + 1):
        if j >= w:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
        for l in dp:
            print(l)

print(dp[-1][-1])