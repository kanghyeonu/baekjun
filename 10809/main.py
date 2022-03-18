string = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lst = [-1 for i in range(26)]

for i in string:
    pos1 = alphabet.find(i)
    pos2 = string.find(i)
    lst[pos1] = pos2

print(*lst, sep =' ')