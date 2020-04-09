# 10996
n = int(input())
for i in range(1, n+1):
    if n % 2 == 1:
        print('* '*(n-n//2))
        print(' *'*(n//2))
    else:
        print('* '*(n//2))
        print(' *'*(n-n//2))