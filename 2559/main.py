N, K = map(int, input().split())

lst = list(map(int, input().split()))
sum_lst = [sum(lst[:K])]

for i in range(N-K):
     sum_lst.append(sum_lst[-1] - lst[i] + lst[i+K])

print(max(sum_lst))