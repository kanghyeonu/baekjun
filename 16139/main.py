import sys

###-------------------------------------------------------------------###
# string = sys.stdin.readline().strip()
# q = int(sys.stdin.readline().strip())
# for _ in range(q):
#     char, s, e = map(str, sys.stdin.readline().split())
#     s, e = int(s), int(e)
#
#     print(string[s:e + 1].count(char))
###-------------------------------------------------------------------###
word = sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())
dic = {}
for _ in range(q):
    cha, s, e = map(str, sys.stdin.readline().split())
    if cha not in dic:
        dic[cha] = [0]
        for i in range(len(word)):
            if word[i] == cha:
                dic[cha].append(dic[cha][i] + 1)
            else:
                dic[cha].append(dic[cha][i])
    s, e = int(s), int(e)
    print(dic[cha][e+1] - dic[cha][s])
