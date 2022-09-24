'''
import sys

N, M = map(int, sys.stdin.readline().split())
home = []
chicken = []

for row in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for col, val in zip(range(N), lst):
        if val == 1:
            home.append([row, col])
        elif val == 2:
            chicken.append([row, col])

visited = []
min_val = 10000000


def dfs(s):
    global min_val
    if len(visited) == M:
        min_val = min(calc(), min_val)
        return

    for i in range(s, len(chicken)):
        if chicken[i] not in visited:
            visited.append(chicken[i])
            dfs(i + 1)
            visited.pop()


def calc():
    distance = 0
    for i in home:
        min_d = 100000
        for j in visited:
            min_d = min(min_d, abs(i[0] - j[0]) + abs(i[1] - j[1]))
            if min_d == 1:
                break
        distance += min_d

    return distance


dfs(0)
print(min_val)
'''
import sys

N, M = map(int, sys.stdin.readline().split())
home = []
chicken = []

for row in range(N):
    lst = (list(map(int, sys.stdin.readline().split())))
    for col, val in zip(range(N), lst):
        if val == 1:
            home.append([row, col])
        elif val == 2:
            chicken.append([row, col])

weight = [[100000 for _ in range(len(home))] for __ in range(M+1)]

visited = []
min_val = 100000
def dfs(s):
    global min_val
    if len(visited) == M:
        min_val = min(sum(weight[-1]), min_val)
        return

    for i in range(s, len(chicken)):
        if chicken[i] not in visited:
            visited.append(chicken[i])
            calc(len(visited))
            dfs(i+1)
            visited.pop()

def calc(idx):
    for i in range(len(home)):
        weight[idx][i] = min(weight[idx-1][i], abs(home[i][0] - visited[idx-1][0]) + abs(home[i][1] - visited[idx-1][1]))
    return
dfs(0)
print(min_val)
