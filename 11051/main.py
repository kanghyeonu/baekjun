a, b = map(int, input().split())

def fac(i):
    if i == 1 or i == 0:
        return 1
    else:
        return i * fac(i-1)

print(fac(a) // (fac(a-b) * fac(b)) % 10007)