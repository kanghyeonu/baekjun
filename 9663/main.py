N = int(input())

cnt = 0
board = [0 for _ in range(N)]

#row[i] = j -> (i=row, j=col)
def n_queen(row):
    global cnt
    if row == N:
        cnt += 1
        return
    # row 별 0~7(1~8)열 위치에 퀸 가능 위치 체크
    for i in range(N):
        board[row] = i #(0, 0), (0, 1) ~ (0, N), (1, 0), (1, 1) ~ (N, N) 위치에 하나씩 두는 과정
        if promising(row):
            n_queen(row+1)

def promising(row):
    #체크해야 할것
    #같은 행, 열, 대각선에 퀸이 존재하면 안됨
    for i in range(row): #어차피 row 행 이상으론 아직 퀸이 둬지지 않음
        # 행은 board 인덱스이기 때문에 하나밖에 두지못함 체크 불필요
        if board[i] == board[row] or abs(i - row) == abs(board[i] - board[row]): #같은 열 퀸 존재, 대각선 좌표는 (i, j)에서 (+1,+1) (+1,-1), (-1,-1), (-1,+1)
            return False
    return True

n_queen(0)
print(cnt)