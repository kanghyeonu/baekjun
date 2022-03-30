def check(n):
    if n == 1:
        return 0
    for i in range(2, round(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

M, N = map(int, input().split())

for i in range(M, N+1):
    if check(i) == 1:
        print(i)