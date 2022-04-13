num = input()
lst = []
for i in num:
    lst.append(i)

lst.sort(reverse=True)
string=''
for i in lst:
    string += str(i)

print(string)