number = int(input())

lst = [i for i in range(2, number//2+ 1)]
lst.append(number)

if number == 1:
    pass
else:
    while True:
        if number == 1:
            break
        for i in lst:
            if number % i == 0:
                print(i)
                number = number // i

