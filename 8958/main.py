import re

p = re.compile('O+')

case = int(input())

for i in range(case):
    string = input()
    lst = p.findall(string)
    score = 0
    for j in lst:
        for k in range(1, len(j)+1):
            score = score + k
    print(score)