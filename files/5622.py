# 5622
s = list(input())
d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
t = 0

for a in s:
    for b in d:
        if b.find(a) >= 0: t += (d.index(b) + 3)
print(t)
