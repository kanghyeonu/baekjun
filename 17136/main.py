import sys

board = []
for _ in range(10):
    board.append(list(map(int, sys.stdin.readline().split())))

papers = [5, 5, 5, 5, 5]
min_val = 30
def sol(row):
    global min_val, papers
    if row == 10 :
        min_val = min(min_val, 25 - sum(papers))
        return

    if 1 in board[row]:
        col = board[row].index(1)
        for i in range(4):
            if isPromising(row, col, i+1):
                papers[i] -= 1
                if -1 in papers:
                    papers[i] += 1
                    continue

                for row2 in range(row, row+i + 1):
                    for col2 in range(col, col+i + 1):
                        board[row2][col2] = 0

                sol(row)

                for row2 in range(row, row+i + 1):
                    for col2 in range(col, col+i + 1):
                        board[row2][col2] = 1
                papers[i] += 1
    else:
        sol(row + 1)

def isPromising(row, col, size):
    for i in range(size):
        if row+i > 9 or col+i > 9 or board[row][col + i] == 0 or board[row + i][col] == 0 or board[row + i][col + i] == 0:
            return False
    return True

sol(0)
if min_val == 30:
    print('-1')
else:
    print(min_val)