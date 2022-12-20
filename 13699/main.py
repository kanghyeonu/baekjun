n = int(input())

dp = [1] * (n+1)
for i in range(2, n+1):
    ans = 0
    for j in range(i):
        ans = ans + dp[(i-1)-j] * dp[0+j]
    dp[i] = ans

print(dp[n])