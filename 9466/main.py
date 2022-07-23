import sys, copy

N = int(sys.stdin.readline().strip())
for i in range(N):
    num  = int(sys.stdin.readline().strip())
    nodes = list(map(int, sys.stdin.readline().split()))
    nodes.insert(0, 0)

    visited = set()
    for j in range(1, num+1):
        if j in visited:
            continue
        temp_visited = []
        start = j
        while True:
            temp_visited.append(start)`
            if nodes[start] not in set(temp_visited) and nodes[start] not in visited:
                start = nodes[start]
            elif nodes[start] in temp_visited:
                idx = temp_visited.index(nodes[start])
                lst = list(temp_visited[idx:])
                visited = visited.union(lst)
                break
            else:
                break
    print(num-len(visited))