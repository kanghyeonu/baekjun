def check(n):
    if n == 1:
        return 0
    for i in range(2, n//2+1):
        if n % i == 0:
            return 0
    return 1

M = int(input())
N = int(input())
lst = []

for i in range(M, N+1):
    if check(i) == 1:
        lst.append(i)

if len(lst)==0:
    print(-1)

else:
    print(sum(lst))
    print(min(lst))