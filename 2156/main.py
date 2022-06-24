import sys

n = int(sys.stdin.readline().strip())
lst = [0]
for i in range(n):
    lst.append(int(sys.stdin.readline().strip()))

if n < 3:
    print(sum(lst))

else:
    dp = [0] * (n+1)
    dp[1] = lst[1]
    dp[2] = lst[2] + lst[1]
    dp[3] = max(lst[1]+lst[3], lst[2] + lst[3], dp[2])

    for i in range(4, n+1):
        dp[i] = max(lst[i]+dp[i-2], lst[i]+lst[i-1]+dp[i-3], dp[i-1])

    print(dp[n])
