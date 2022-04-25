import sys
from collections import deque
case = int(input())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(case)]
visited = deque()

min_gap = 100000000

def getGap(A):
    B = list(set(range(case)) - set(A))
    sum_A = 0
    sum_B = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            sum_A += table[A[i]][A[j]] + table[A[j]][A[i]]
            sum_B += table[B[i]][B[j]] + table[B[j]][B[i]]
    return abs(sum_A - sum_B)


def dfs(start):
    global min_gap
    if len(visited) == case//2:
        min_gap = min(min_gap, getGap(visited))
        return

    for i in range(start, case):
        if i not in visited:
            visited.append(i)
            dfs(i+1)
            visited.pop()

dfs(0)
print(min_gap)
