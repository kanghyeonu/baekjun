from collections import deque
import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    PS = sys.stdin.readline().strip()
    q = deque()
    for ps in PS:
        if ps == '(':
            q.append('(')
        else:
            if q:
                q.pop()
            else:
                q.append(')')
                break
    if q:
        print('NO')
    else:
        print('YES')
