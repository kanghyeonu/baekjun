N, M = map(int, input().split())

lst = []
paint = []

for i in range(N):
    lst.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        start_B = 0
        start_W = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:  #체스판 pos check
                    if lst[k][l] != 'B':    #줄의 시작이 흰색
                        start_B += 1
                    if lst[k][l] != 'W':    #줄의 시작이 검은색
                        start_W += 1
                else:
                    if lst[k][l] != 'W':
                        start_B += 1
                    if lst[k][l] != 'B':
                        start_W += 1
        paint.append(start_W)
        paint.append(start_B)

print(min(paint))

