num = int(input())

honeycomb = 1
cnt = 1

while num > honeycomb:
    honeycomb += 6 * cnt
    cnt += 1
print(cnt)