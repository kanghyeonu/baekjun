def check(n):
    if n == 1:
        return 0
    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

num = int(input())
lst = list(map(int, input().split()))
cnt = 0

for i in lst:
    cnt += check(i)

print(cnt)