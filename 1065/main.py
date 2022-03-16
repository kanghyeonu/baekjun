num = int(input())
cnt = 0

for i in range(1, num + 1):
    lst = [int(j) for j in str(i)]
    if len(lst) == 1:
        cnt += 1
        continue
    gap = set()
    for j in range(len(lst)-1):
        gap.add(lst[j] - lst[j+1])
    if len(gap) == 1:
        cnt += 1
print(cnt)