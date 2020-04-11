# 1316
n = 0
for i in range(int(input())):
    w = input()
    if list(w) == sorted(w, key=w.find): n += 1
print(n)
