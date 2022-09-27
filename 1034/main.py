import sys
N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    temp = list(sys.stdin.readline().strip())
    board.append(list(map(int, temp)))

K = int(sys.stdin.readline().strip())
max_val = 0
for row in range(N):
    zeros = board[row].count(0)

    dup_rows = 0
    if zeros <= K and zeros%2 == K%2:
        for row2 in range(N):
            if board[row] == board[row2]:
                dup_rows += 1
    max_val = max(dup_rows, max_val)

print(max_val)
