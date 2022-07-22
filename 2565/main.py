import sys


def binSearch(n):
    l = 0
    r = len(table_dp) - 1
    while l <= r:
        m = (l + r) // 2
        if table_dp[m] == n:
            break
        elif table_dp[m] < n:
            l = m + 1
        else:
            r = m - 1
    if n > table_dp[m]:
        m += 1
    return m


N = int(sys.stdin.readline())
lst = []
table_dp = [0]
for _ in range(N):
    t = tuple(map(int, sys.stdin.readline().split()))
    lst.append(t)

lst.insert(0, (0, 0))
lst.sort()
for i in range(1, N + 1):
    if table_dp[-1] < lst[i][1]:
        table_dp.append(lst[i][1])

    else:
        idx = binSearch(lst[i][1])
        table_dp[idx] = lst[i][1]

print(N - (len(table_dp) - 1))