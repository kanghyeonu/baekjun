lst = [0] * 101

def padovan(n):
    for i in range(4, n+1):
        lst[i] = lst[i-2] + lst[i-3]

lst[1] = 1
lst[2] = 1
lst[3] = 1

inputs = []

case = int(input())
for _ in range(case):
    inputs.append(int(input()))
Max = max(inputs)

padovan(Max)

for i in inputs:
    print(lst[i])
