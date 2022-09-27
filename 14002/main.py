import sys
n = int(sys.stdin.readline().strip())
lst = [0]
lst.extend(list(map(int, sys.stdin.readline().split())))
dp = [0] * (n+1)
table_lst = [-1000000001]
table_dp = [0]

def binSearch(n):
    left = 0
    right = len(table_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if table_lst[mid] == n:
            break
        elif table_lst[mid] > n:
            right = mid - 1
        else:
            left = mid + 1
    if max(table_lst) > n and table_lst[mid] < n:
        mid += 1
    return mid

for i in range(1, n+1):
    if table_lst[-1] < lst[i]:
        table_lst.append(lst[i])
        table_dp.append(max(table_dp)+1)
        dp[i] = max(table_dp)
    else:
        idx = binSearch(lst[i])
        table_lst[idx] = lst[i]
        dp[i] = table_dp[idx]

max_val = max(dp)
order = max_val
answer = []
for i in range(n, 0, -1):
    if dp[i] == order:
        answer.append(lst[i])
        order -= 1
answer.reverse()
print(max_val)
print(*answer)

