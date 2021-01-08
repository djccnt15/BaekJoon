# 1065
a = int(input())
han = 0
for i in range(1, a + 1):
    if i < 100: han += 1
    else:
        b = list(map(int, str(i)))
        if b[0] - b[1] == b[1] - b[2]: han += 1
print(han)
