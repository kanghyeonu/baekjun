import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for _ in range(T):
    flag = 0
    command = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    dq = deque(sys.stdin.readline().strip().strip('['']').split(','))
    if n == 0:
        dq = []

    for c in command:
        if c == 'R':
            flag += 1
        else:
            if len(dq) == 0:
                print('error')
                flag = -1
                break
            if flag % 2 == 0:
                dq.popleft()
            else:
                dq.pop()
    if flag == -1:
        continue
    else:
        if flag % 2 == 0:
            print('['+','.join(dq)+']')
        else:
            dq.reverse()
            print('['+','.join(dq)+']')