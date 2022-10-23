import sys
n = int(sys.stdin.readline().strip())

stack = []
sol = []
cur = 1
flag = 1
for i in range(n):
    num = int(sys.stdin.readline().strip())
    while cur <= num:
        stack.append(i)
        sol.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        sol.append('-')
    else:
        print('NO')
        flag = 0
        break

if flag:
    print(*sol)

