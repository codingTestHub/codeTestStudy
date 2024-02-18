n = input()
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in li:
    n = n.replace(i, '*')
print(len(n))