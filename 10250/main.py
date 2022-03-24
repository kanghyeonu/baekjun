import sys
test_case = int(input())

for i in range(test_case):
    pos = ''
    #H: 높이, W: 가로, N: 몇번째 손님
    H, W, N = map(int, sys.stdin.readline().split())
    pos += str(N%H)
    if N//H < 10:
        pos += '0'
    pos += str(N//H + 1)
    print(pos)