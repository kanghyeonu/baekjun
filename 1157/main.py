alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
newdict = dict.fromkeys(alphabet, 0)

string = input()
string = string.upper()

for i in string:
    newdict[i] += 1

sorting = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

if sorting[0][1] == sorting[1][1]:
    print('?')
else:
    print(sorting[0][0])
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lst = [0 for i in alphabet]
#
# string = input()
# string = string.upper()
#
# for i in string:
#     lst[alphabet.find(i)] += 1
#
# lst_sort = sorted(lst, reverse = True)
#
# if lst_sort[0] == lst_sort[1]:
#     print('?')
# else:
#     print(alphabet[lst.index(max(lst))])
