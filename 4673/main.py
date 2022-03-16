all_num = set(range(1, 10001))
not_self_num = set()

for i in range(1, 10001):
    for j in str(i):
        i = i + int(j)
    not_self_num.add(i)

self_num = list(all_num - not_self_num)
self_num.sort()
for i in self_num:
    print(i)