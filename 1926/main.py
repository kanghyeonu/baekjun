import sys
sys.setrecursionlimit(10000000)
n, m = map(int, sys.stdin.readline().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
max_val = 0
def sol():
    global max_val, cnt
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            cnt += 1
            max_val = max(max_val, get_area(i, j))

def get_area(row, col):
    global n, m
    size = 0
    q = [(row, col)]
    while q:
        tmp_q = []
        for r, c in q:
            if paper[r][c] == 0:
                continue
            paper[r][c] = 0
            size += 1
            if r < n - 1 and paper[r + 1][c] == 1:
                tmp_q.append((r + 1, c))
            if c < m - 1 and paper[r][c + 1] == 1:
                tmp_q.append((r, c + 1))
            if r > 0 and paper[r - 1][c] == 1:
                tmp_q.append((r - 1, c))
            if c > 0 and paper[r][c - 1] == 1:
                tmp_q.append((r, c - 1))
        q = tmp_q

    return size

sol(0)
print(cnt)
print(max_val)
