# 2231
n = int(input())

a = 0
for i in range(1, n+1):
    d = list(map(int, str(i)))
    s = i + sum(d)
    if s == n:
        a = i
        break

print(a)