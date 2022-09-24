import sys

N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))

visited = []
max_val = 0

def sol():
    global max_val
    if len(visited) == N:
        val = 0
        for i in range(1, N):
            val += abs(lst[visited[i]] - lst[visited[i-1]])
        max_val = max(val, max_val)
        return

    for i in range(N):
        if i not in visited:
            visited.append(i)
            sol()
            visited.pop()
sol()
print(max_val)