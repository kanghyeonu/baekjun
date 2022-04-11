import sys

case = int(sys.stdin.readline())
dic = {}

for _ in range(case):
    num = int(sys.stdin.readline())
    if num not in dic.keys():
        dic[num] = 1
    else:
        dic[num] += 1

dic = dict(sorted(dic.items()))

for i in dic.keys():
    for j in range(dic.get(i)):
        print(i)
