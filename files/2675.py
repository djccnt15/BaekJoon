# 2675
t = int(input())
for i in range(t):
    a, b = input().split()
    r = ''
    for i in b:
        r += int(a) * i
    print(r)
