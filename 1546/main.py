num = int(input())
lst = list(map(int, input().split()))
max_ = max(lst)
sum = 0

for i in lst:
    sum = sum + (i / max_) * 100

print(sum / num)

