from collections import deque
import sys

q = deque()
K = int(sys.stdin.readline().strip())
for _ in range(K):
    val = int(sys.stdin.readline().strip())
    if not val:
        q.pop()
    else:
        q.append(val)

print(sum(q))