lst = [0 for i in range(1000001)]
lst[1] = 1
lst[2] = 2

def fibo(n):
    for i in range(3, n+1):
        lst[i] = (lst[i-1] + lst[i-2])%15746

    return lst[n]

N = int(input())

print(fibo(N))
