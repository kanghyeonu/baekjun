def binSearch(n, table):
    left = 0
    right = len(table) - 1

    while left <= right:
        mid = (left + right) // 2
        if table[mid] == n:
            break
        if table[mid] > n:
            right = mid - 1
        else:
            left = mid + 1

    if table[-1] > n and n > table[mid]:
        mid += 1

    return mid

N = int(input())
lst = [0]
lst.extend(list(map(int, input().split())))

table_dp_inc = [0]
table_dp_desc = [0]
dp_inc = [0] * (N+1)
dp_desc = [0] * (N+1)
for i in range(1, N+1):
    if table_dp_inc[-1] < lst[i]:
        table_dp_inc.append(lst[i])
        dp_inc[i] = len(table_dp_inc)-1
    else:
        idx = binSearch(lst[i], table_dp_inc)
        table_dp_inc[idx] = lst[i]
        dp_inc[i] = table_dp_inc.index(table_dp_inc[idx])

    if table_dp_desc[-1] < lst[(N+1)-i]:
        table_dp_desc.append(lst[(N+1)-i])
        dp_desc[i] = len(table_dp_desc)-1
    else:
        idx = binSearch(lst[(N+1)-i], table_dp_desc)
        table_dp_desc[idx] = lst[(N+1)-i]
        dp_desc[i] = table_dp_desc.index(table_dp_desc[idx])

dp_inc.remove(0)
dp_desc.remove(0)
dp_desc.reverse()

print(max([x+y for x, y in zip(dp_inc, dp_desc)])-1)