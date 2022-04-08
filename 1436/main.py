num = int(input())

string = '666'

lst = [666]

for i in range(1, 2500):
    for j in range(len(str(i))+1):
        doom = str(i)[:j] + string + str(i)[j:]
        if int(doom) not in lst:
            print(doom)
            lst.append(int(doom))

lst.sort()
print(len(lst))
print(lst[num-1])

