from collections import deque
import sys

N = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
visited = set()

def dfs(s):
    q = deque([s])
    visited[s] = -1

    while q:
        node = q.popleft()
        for i in graph[node]:
            q.append(i)
            visited

for _ in range(N-1):
    s1, s2 = map(int, sys.stdin.readline().split())
    graph[s1].append(s2)
    graph[s2].append(s1)

dfs(1)
for i in range(2, N+1):
    print(parent[i])


