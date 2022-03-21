case = int(input())

sol = ''

for i in range(case):
    num, string = map(str, input().split())
    for j in string:
        for k in range(int(num)):
            sol += j
    print(sol)
    sol = ''