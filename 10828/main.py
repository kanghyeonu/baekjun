from collections import deque
import sys

N = int(sys.stdin.readline())

q = deque()
for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if ' ' in cmd:
        cmd, val = map(str, cmd.split())

    if cmd == 'push':
        q.append(val)

    elif cmd == 'pop':
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)

    elif cmd == 'size':
        print(len(q))

    elif cmd == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif cmd == 'top':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)