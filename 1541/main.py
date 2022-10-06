expression = input().split('-')

lst = []
for exp in expression:
    if '+' in exp:
        val = 0
        temp = exp.split('+')
        for num in temp:
            val += int(num)
    else:
        val = int(exp)
    lst.append(val)

min_val = lst[0]
for i in range(1, len(lst)):
    min_val -= int(lst[i])

print(min_val)