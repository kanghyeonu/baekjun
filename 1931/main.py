import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    t = (s, e)
    lst.append(t)
lst.sort()

ans = [lst[0]]
for i in range(1, N):
    if ans[-1][1] > lst[i][1]:
        ans[-1] = lst[i]
    elif ans[-1][1] <= lst[i][0]:
        ans.append(lst[i])

print(len(ans))