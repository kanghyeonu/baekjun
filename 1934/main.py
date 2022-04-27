import math
case = int(input())

for _ in range(case):
    a, b = map(int, input().split())
    print(math.lcm(a, b))