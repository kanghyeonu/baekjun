import sys

sys.setrecursionlimit(10000000)
n, m = map(int, sys.stdin.readline().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
max_val = 0
temp_size = 0
def sol(row):
    global max_val, cnt, temp_size
    if row == n:
        return

    if 1 in paper[row]:
        cnt += 1
        col = paper[row].index(1)
        temp_size = 0
        max_val = max(max_val, get_area(row, col))
        sol(row)
    else:
        sol(row + 1)

def get_area(row, col):
    global n, m, temp_size
    temp_size += 1
    paper[row][col] = 0
    if row < n-1 and paper[row + 1][col] == 1:
        get_area(row + 1, col)
    if col < m-1 and paper[row][col + 1] == 1:
        get_area(row, col + 1)
    if row > 0 and paper[row - 1][col] == 1:
        get_area(row - 1, col)
    if col > 0 and paper[row][col - 1] == 1:
        get_area(row, col - 1)
    else:
        return temp_size


sol(0)
print(cnt)
print(max_val)
