N = int(input())
lst = list(map(int, input().split()))
LIS = [lst[0]]

def binary_search(n, mid=0):
    left = 0
    right = len(LIS) -1
    while left <= right:
        mid = (left + right) // 2
        if LIS[mid] == n:
            break
        elif LIS[mid] > n:
            right = mid - 1
        else:
            left = mid + 1
    if LIS[-1] > n and LIS[mid] < n:
        mid += 1
    return mid


for i in range(1, N):
    if LIS[-1] < lst[i]:
        LIS.append(lst[i])
    else:
        idx = binary_search(lst[i])
        LIS[idx] = lst[i]

print(len(LIS))

