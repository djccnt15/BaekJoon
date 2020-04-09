# 1110
c = 0
n = inp = int(input())
while True:
    ten = n // 10
    one = n % 10
    new = ten + one
    new_one = new % 10
    n = one * 10 + new_one
    c += 1
    if n == inp: break
print(c)