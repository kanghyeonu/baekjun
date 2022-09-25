import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    temp = list(sys.stdin.readline().strip())
    board.append(list(map(int, temp)))
input()

print(board)

