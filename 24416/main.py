N = int(input())

lst = [1, 1]

for i in range(2, N):
    lst.append(lst[-2] + lst[-1])

print(lst[-1], N - 2)
