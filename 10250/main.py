import sys, math

test_case = int(input())

for i in range(test_case):
    pos = 0
    # H: 높이, W: 가로, N: 몇번째 손님
    H, W, N = map(int, sys.stdin.readline().split())
    # 층 구하기
    if N % H == 0:
        floor = H * 100
        pos = floor + N // H
    else:
        floor = (N % H) * 100
        pos = floor + N // H + 1

    print(pos)