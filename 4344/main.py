import sys

num = int(input())

for i in range(num):
    lst = list(map(int, sys.stdin.readline().split()))
    del lst[0]
    avg = sum(lst)/len(lst)
    highscore = list(filter(lambda x: x > avg, lst))
    print('{:.3f}%'.format((round(len(highscore)/len(lst)*100, 3))))