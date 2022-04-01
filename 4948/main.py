Max = 123456

eratos = [1 for i in range(0, 2 * Max + 1)]
eratos[0] = 0
eratos[1] = 0

for i in range(2, 2 * Max):
    if eratos[i]:
        for j in range(i + i, 2 * Max, i):
            eratos[j] = 0

while True:
    case = int(input())
    if case == 0:
        break
    else:
        print(sum(eratos[case+1:2*case+1]))