# 2920
l = list(map(int, input().split())) # 입력된 인풋을 int타입으로 리스트화
if l == [1, 2, 3, 4, 5, 6, 7, 8]: print('ascending')
elif l == [8, 7, 6, 5, 4, 3, 2, 1]: print('descending')
else: print('mixed')