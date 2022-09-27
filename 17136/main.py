import sys

board = []

for _ in range(10):
    board.append(list(map(int, sys.stdin.readline().split())))

min_val = 10000


def sol(row):
    global min_val
    if row == 9:
        return
    col = board[row].index(1)
    # size
    for i in range(4):
        if isPromising(row, col, size):
            for j in range(row, row + i):
                board[j][col:col + i] = 0


def isPromising(row, col, size):
    for i in range(size):
        if board[row][col + i] == 0 or board[row + i][col] == 0 or board[row + i][col + i] == 0:
            return False
    return True


sol(0)