# 1157
s = list(str(input()).upper())
b = list(set(s))
b.sort()

l = []
for i in b:
    l.append(s.count(i))

if l.count(max(l)) >= 2: print('?')
else: print(b[l.index(max(l))])