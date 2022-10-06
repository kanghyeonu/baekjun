N = int(input())
crane = list(map(int, input().split()))
M = int(input())
weight = list(map(int, input().split()))

crane.sort(reverse=True)
weight.sort(reverse=True)

for i in range(M):
    for j in range(N):
        if crane[j] >= weight[i]:
            break
        elif j == N-1:
            