# 2798
n, m = map(int, input().split())
l = list(map(int, input().split()))

result = 0
for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n):
            s = l[a] + l[b] + l[c]
            if s <= m: result = max(result, s)

print(result)