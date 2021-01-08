# 3052
l = []
for i in range(10): l.append(int(input()))
s = set()
for n in l: s.add(n % 42)
new_s = list(s)
print(len(new_s))
