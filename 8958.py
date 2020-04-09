# 8958
a = int(input())
for i in range(a):
    b = input()
    c = b.replace('X', ' ')
    c = c.split()
    r = 0
    for i in range(len(c)):
        for j in range(len(c[i]) + 1): r += j
    print(r)