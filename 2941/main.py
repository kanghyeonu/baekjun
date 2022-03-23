lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()

for i in lst:
    if i in string:
        string = string.replace(i, ' ')

print(len(string))

