# 10871
a, b = map(int, input().split())
c = list(map(int, input().split())) # 입력된 인풋을 int타입으로 리스트화
for i in range(a):
    if b > c[i]: print(c[i], end = ' ')