# 7568
i = int(input())

p = []
for i in range(i):
    l = list(map(int, input().split()))
    p.append(l)

for a in p:
    r = 1
    for b in p:
        if p.index(a) != p.index(b):
            if a[0] < b[0] and a[1] < b[1]: r += 1
    print(r, end=' ')