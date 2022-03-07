score = int(input())
share = str(score // 10)

grade = {'10':'A', '9':'A', '8':'B', '7':'C', '6':'D'}.get(share, 'F')

print(grade)