# from collections import defaultdict
# import sys
#
# case = int(input())
# dic = defaultdict(list)
#
# for _ in range(case):
#     string = sys.stdin.readline().rstrip()
#     if string not in dic[len(string)]:
#         dic[len(string)].append(string)
#
# dic = dict(sorted(dic.items()))
#
# for i in dic.values():
#     i.sort()
#
# for i in dic.keys():
#     for j in range(len(dic[i])):
#         print(dic[i][j])
''
import sys

case = int(input())
lst = []
for _ in range(case):
    lst.append(sys.stdin.readline().rstrip())

lst = list(set(lst))
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)