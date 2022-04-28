case = int(input())


def fac(n):
    val = 1
    for i in range(n):
        val *= (i + 1)
    return val


for _ in range(case):
    a, b = map(int, input().split())
    print(fac(b) // (fac(a) * fac(b - a)))
