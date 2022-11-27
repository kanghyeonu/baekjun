import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
position = list(map(int, sys.stdin.readline().split()))
dq = deque([i for i in range(1, N+1)])

cnt = 0
for i in position:
    while True:
        if dq[0] == i:
            dq.popleft()
            break

        if dq.index(i) < len(dq)/2:
            while dq[0] != i:
                dq.append(dq.popleft())
                cnt +=1
        else:
            while dq[0] != i:
                dq.appendleft(dq.pop())
                cnt += 1
print(cnt)