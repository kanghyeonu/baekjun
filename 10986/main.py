N, M = map(int, input().split())
lst = [0]
lst.extend(list(map(int, input().split())))
table = [0] * M

for i in range(1, N+1):
    lst[i] += lst[i-1]
    table[lst[i] % M] += 1

cnt = table[0]

for i in table:
    cnt += i * (i-1) // 2

print(cnt)