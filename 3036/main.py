import math
case = int(input())
lst = list(map(int, input().split()))

for i in range(1, case):
    gcd = math.gcd(lst[0], lst[i])
    print(str(lst[0]//gcd)+'/'+str(lst[i]//gcd))