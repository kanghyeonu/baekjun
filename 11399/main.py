N = int(input())
lst = list(map(int, input().split()))
lst.sort()

for i in range(1, N):
    lst[i] = lst[i - 1] + lst[i]

print(sum(lst))