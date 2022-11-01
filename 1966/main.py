import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    q = deque()
    for i, j in zip(range(N), lst):
        q.append((i, j))

    cnt = 0
    while q:
        priority = max(q, key=lambda x: x[1])
        val = q.popleft()
        if val[1] != priority[1]:
            q.append(val)
        else:
            cnt += 1
            if val[0] == M:
                print(cnt)
                break
