case = int(input())

for i in range(case):
    a = int(input())
    b = int(input())
    lst = [list(v for v in range(1, b+1))]
    for j in range(a):
        lst.append([sum(lst[j][:w+1]) for w in range(b)])
    print(lst[-1][-1])