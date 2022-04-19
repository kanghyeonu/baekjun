N, M = map(int, input().split())

visited = []


def dfs():
    if len(visited) == M:
        print(' '.join(map(str, visited)))
        return

    for i in range(1, N + 1):
        visited.append(i)
        dfs()
        visited.pop()
