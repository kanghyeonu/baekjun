N = int(input())
crane = list(map(int, input().split()))
M = int(input())
weight = list(map(int, input().split()))

crane.sort(reverse=True)
weight.sort(reverse=True)

cnt = 0
if crane[0] < weight[0]:
    print('-1')

else:
    while weight:
        cnt += 1
        for i in range(N):
            for j in range(len(weight)):
                if crane[i] >= weight[j]:
                    weight.pop(j)
                    break
    print(cnt)