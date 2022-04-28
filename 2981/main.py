import math

case = int(input())
lst = []
for i in range(case):
    lst.append(int(input()))
lst.sort()

gap = []
for i in range(case-1):
    gap.append(lst[i+1] - lst[i])

gcd = gap[0]
for i in range(1, len(gap)):
    gcd = math.gcd(gcd, gap[i])

sol = []
for i in range(2, int(gcd**0.5)+1):
    if i not in sol and gcd % i == 0:
        sol.append(i)
        sol.append(gcd//i)
sol.append(gcd)
sol = list(set(sol))

sol.sort()
print(*sol)