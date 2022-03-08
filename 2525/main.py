h, m = map(int, input().split())
time = int(input())

h = (h + (time // 60)) % 24
m = m + time % 60

if m > 59:
    m = m - 60
    h = h + 1
    h = h % 24

print(h, m)