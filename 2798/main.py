import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

best = [10000000000]

for i in range(N-2):
    for j in range(i + 1, N-1):
        for k in range(j + 1, N):
            compare = [lst[i], lst[j], lst[k]]
            if sum(compare) == M:
                print(sum(compare))
                break
            elif abs(M - sum(best)) > (M - sum(compare)) and M - sum(compare) > 0:
                best = [lst[i], lst[j], lst[k]]
        if sum(compare) == M:
            break
    if sum(compare) == M:
        break

if sum(compare) != M:
    print(sum(best))

