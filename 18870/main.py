import sys

case = int(input())
lst = list(map(int, sys.stdin.readline().split()))

lst2 = list(set(lst))
lst2.sort()
dic = {}
idx = 0
for i in lst2:
    dic[i] = idx
    idx += 1

for i in lst:
    print(dic[i], end=' ')