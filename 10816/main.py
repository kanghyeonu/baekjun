import sys
N = sys.stdin.readline().strip()
dic = dict()

lst = list(map(str, sys.stdin.readline().split()))

for i in lst:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1
M = sys.stdin.readline().strip()

lst = list(map(str, sys.stdin.readline().split()))

print(" ".join(map(str, [dic[i] if i in dic.keys() else 0 for i in lst])))
# for i in lst:
#     if i in dic.keys():
#         print(dic[i], end = " ")
#     else:
#         print(0, end = " ")