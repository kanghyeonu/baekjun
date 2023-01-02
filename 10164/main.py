N, M, K = map(int, (input().split()))
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
cnt = 0

for row in range(1, N+1):
    for col in range(1, M+1):
        dp[row][col] = max(1, dp[row][col-1] + dp[row-1][col])
        cnt += 1
        if cnt == K:
            px = row
            py = col

if K == 0:
    print(dp[-1][-1])
else:
    print(dp[px][py]*dp[N-px+1][M-py+1])

    # N, M, K = map(int, (input().split()))
    #
    # dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    # cnt = 0
    # result = 1
    # for row in range(1, N + 1):
    #     for col in range(1, M + 1):
    #         dp[row][col] = max(1, dp[row][col - 1] + dp[row - 1][col])
    #         cnt += 1
    #         if cnt == K:
    #             break
    #     if cnt == K:
    #         obj_row = row
    #         obj_col = col
    #         result = dp[row][col]
    #         break
    #
    # if K != 0:
    #     dp = [[0 for _ in range(M - obj_col + 1 + 1)] for _ in range(N - obj_row + 1 + 1)]
    #     for row in range(1, N - obj_row + 1 + 1):
    #         for col in range(1, M - obj_col + 1 + 1):
    #             dp[row][col] = max(1, dp[row][col - 1] + dp[row - 1][col])
    #
    # print(result * dp[-1][-1])
