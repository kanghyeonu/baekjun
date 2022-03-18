num = int(input())

for i in range(num):
    cnt, string = map(str, input().split())
    for j in range(int(cnt)):
        for k in string:
            print(k, sep='')
print('\n')
