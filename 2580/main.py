import sys

board = []
elements = set(range(10))

for _ in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))

def sudoku(row):
    if row == 9:
        for i in board:
            print(*i)
        exit(0)

    # 빈 숫자
    blank_nums = elements - set(board[row])
    col = board[row].index(0)
    for i in blank_nums:
        board[row][col] = i
        if promising(row, col):
            if 0 not in board[row]:
                sudoku(row+1)
            else:
                sudoku(row)

        board[row][col] = 0

def promising(row, col):
    check = set()
    for i in range(9):
        if board[i][col] != 0 and board[i][col] in check:
            return False
        check.add(board[i][col])
    check.clear()

    for i in range(row//3*3, row//3*3 + 3):
        for j in range(col//3*3, col//3*3 + 3):
            if board[i][j] != 0 and board[i][j] in check:
                return False
            check.add(board[i][j])

    return True

sudoku(0)
