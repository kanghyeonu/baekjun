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

def makeTable(string, cha):
    dp = [0]
    for i in range(len(string)):
        if string[i] == cha:
            dp.append(dp[i] + 1)
        else:
            dp.append(dp[i])
    return dp

string = sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())
dic = {}
for _ in range(q):
    cha, s, e = map(str, sys.stdin.readline().split())
    if cha not in dic.keys():
        dic[cha] = makeTable(string ,cha)
    s, e = int(s), int(e)
    print(dic[cha][e+1] - dic[cha][s])