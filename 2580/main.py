import sys

board = []
numbers = set([i for i in range(1, 10)])

for _ in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))

def sudoku(row):
    if row == 9:
        return
    #현재줄에 빈칸이 없을 경우 다음 줄로
    if 0 not in board[row]:
        sudoku(row + 1)
    #빠진 숫자만 가져오기
    temp = list(numbers - set(board[row]))
    #한 줄에 0이 여러개
    while 0 in board[row]:
        #첫 0의 위치
        pos = board[row].index(0)
        #빈 칸에 숫자 넣고 조건 체크
        for i in temp:
            board[row][pos] = i
            if promising(row, pos):
                break
    sudoku(row + 1)

def promising(row, col):
    #행
    if len(set(board[row])) != 9:
        return False
        # 열
    for i in range(9):
        if row == i:
            continue
            # 열확인
        if board[row][col] == board[i][col]:
            return False
    # 9칸
    partition_row = row // 3
    partition_col = col // 3
    sec1 = board[3 * partition_row + 0][partition_col * 3:partition_col * 3 + 3]
    sec2 = board[3 * partition_row + 1][partition_col * 3:partition_col * 3 + 3]
    sec3 = board[3 * partition_row + 2][partition_col * 3:partition_col * 3 + 3]
    cnt = sec1.count(0) + sec2.count(0) + sec3.count(0)
    print(sec1)
    print(sec2)
    print(sec3)+-
    check = set(sec1) | set(sec2) | set(sec3)
    if len(check) != 9 - cnt + 1:
        return False

    return True 


sudoku(0)

for i in board:
    for j in i:
        print(j, end=' ')
    print()

