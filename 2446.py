# 2446
n = int(input())
for i in range(1, n*2):
    if i <= n: print(' '*(i-1)+'*'*((n-i)*2+1))
    else: print(' '*(n*2-i-1)+'*'*((i-n)*2+1))