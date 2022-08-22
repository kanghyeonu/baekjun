import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

def minus(n):
    global K
    return n - K

lst = list(map(minus, lst))

visited = []
cnt = 0
weight = 0

def dfs(weight):
    global cnt
    if len(visited) == N:
        cnt += 1
        return
    for i in range(N):
        if i not in visited:
            weight += lst[i]
            if weight >= 0:
                visited.append(i)
                dfs(weight)
                visited.pop()
            weight -= lst[i]

dfs(weight)
print(cnt)