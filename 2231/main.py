num = int(input())

for i in range(1, num+1):
    #작은 수부터
    num_sum = i + sum(map(int, str(i))) #분해합
    if num_sum == num:
        print(i)
        break
    elif num == i:
        print(0)