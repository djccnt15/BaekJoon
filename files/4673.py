# 4673
a = list(range(10001))

def self(n): return n + sum(map(int, str(n)))

for i in range(10001):
    if self(i) in a: a.remove(self(i))

for i in a: print(i)
