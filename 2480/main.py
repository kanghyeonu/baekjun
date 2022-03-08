a, b, c = map(int, input().split())

lst = [0 for i in range(6)]

lst[a] = lst[a]+1
lst[b] = lst[b]+1
lst[c] = lst[c]+1

cnt = lst.count(0)

