# 2577
a = int(input())
b = int(input())
c = int(input())
d = list(str(a * b * c))
for i in range(10):
    e = d.count(str(i))
    print(e)