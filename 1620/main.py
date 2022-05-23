import sys

N, M = map(int, sys.stdin.readline().split())

dic1 = dict()

for i in range(1, N + 1):
    dic1[str(i)] = sys.stdin.readline().strip()

dic2 = {v:k for k, v in dic1.items()}

for _ in range(M):
    val = sys.stdin.readline().strip()
    if val in dic1.keys():
        print(dic1.get(val))
    elif val in dic2.keys():
        print(dic2.get(val))