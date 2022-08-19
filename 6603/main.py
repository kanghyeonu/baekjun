import sys

visited = []

def dfs(lotto, s):
    if len(visited) == 6:
        print(*visited)
        return

    for i in range(s, len(lotto)):
        if lotto[i] not in visited:
            visited.append(lotto[i])
            dfs(lotto, i + 1)
            visited.pop()

while True:
    lotto = list(map(int, sys.stdin.readline().split()))
    if 0 in lotto:
        break
    k = lotto[0]
    del lotto[0]
    for i in range(len(lotto)-k+1):
        dfs(lotto, i)
    print()
    visited.clear()
