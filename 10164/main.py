N, M, K = map(int, (input().split()))

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for row in range(1, N+1):
    for col in range(1, M+1):
        dp[row][col] = dp[row][col-1] + dp[row-1][col]

for i in dp:
    print(*i)
