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
sum = 0
middle_idx = 0
for i in dic.keys():
    sum += i * dic.get(i)

for i in dic.keys():
    middle_idx += dic.get(i)
    if middle_idx >= case / 2:
        middle = i
        break
dic2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)

print(round(sum/case))
print(middle)
if len(dic2) > 1 and dic2[0][1] == dic2[1][1]:
    print(dic2[1][0])
else:
    print(dic2[0][0])
print(max(dic.keys()) - min(dic.keys()))
