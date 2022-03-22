lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()
cnt = 0

for i in lst:
    if i in string:
        cnt += string.count(i)
        print(i)
        string = string.replace(i, '')

print(cnt+len(string))
