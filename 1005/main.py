import sys


def dfs(start):


T = int(sys.stdin.readline().strip())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    lst = []
    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        lst.append((X, Y))
    obj = int(sys.stdin.readline().split())

    dfs()

