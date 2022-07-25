import sys

N = int(sys.stdin.readline().strip())
for i in range(N):
    num  = int(sys.stdin.readline().strip())
    nodes = list(map(int, sys.stdin.readline().split()))
    nodes.insert(0, 0)

    visited = set()
    teams = 0
    for j in range(1, num+1):
        if j in visited:
            continue
        temp_visited = []
        start = j
        while True:
            visited.add(start)
            temp_visited.append(start)
            if nodes[start] not in visited:
                start = nodes[start]
            elif nodes[start] in temp_visited:
                idx = temp_visited.index(nodes[start])
                teams += len(temp_visited[idx:])
                break
            else:
                break

    print(num-teams)
