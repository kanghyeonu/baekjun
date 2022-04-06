case = int(input())
lst = []
for i in range(case):
    lst.append(tuple(map(int, input().split())))

score = [1 for i in range(case)]

for i in range(case):
    for j in range(case):
        if i == j:
            continue
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            score[i] += 1

for i in score:
    print(i, end=' ')
