# 1193
n = int(input())

l = 1
while l < n:
    n -= l
    l += 1

if l % 2 == 0:
    a = n
    b = l - n + 1
else:
    a = l - n + 1
    b = n

print('%s/%s' %(a, b))
