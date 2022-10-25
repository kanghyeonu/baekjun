import sys
from collections import deque
N = int(sys.stdin.readline().strip())

q = deque()
for _ in range(N):
    command = sys.stdin.readline().strip()
    if ' ' in command:
        command, val = command.split()

    if command == 'push':
        q.append(int(val))

    elif command == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(q))

    elif command == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif command == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)

    elif command == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)