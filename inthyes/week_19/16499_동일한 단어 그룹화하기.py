n = int(input())
x = []
for _ in range(n):
    word = sorted(list(input()))
    word = ''.join(word)
    if word not in x:
        x.append(word)
print(len(x))