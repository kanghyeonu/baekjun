a, b, c = map(int, input().split())
lst = [0 for i in range(6)]
lst[a-1] = lst[a-1]+1
lst[b-1] = lst[b-1]+1
lst[c-1] = lst[c-1]+1
cnt = lst.count(0)

if cnt == 5:
    print(10000 + (lst.index(3)+1) * 1000)

elif cnt == 4:
    print(1000 + (lst.index(2)+1) * 100)

else:
    idx = [i for i, x in enumerate(lst) if x == 1]
    print((idx[-1] + 1) * 100)