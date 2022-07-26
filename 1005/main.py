import sys
from collections import deque

def topology_sort():
    dp = [0] * (N+1)
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] += D[i]

    while q:
        start = q.popleft()
        for i in graph[start]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[start]+D[i])
            if indegree[i] == 0:
                q.append(i)
    return dp[obj]

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X].append(Y)
        indegree[Y] +=1
    obj = int(sys.stdin.readline().strip())
    sol = topology_sort()
    print(sol)