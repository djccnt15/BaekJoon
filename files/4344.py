# 4344
a = int(input())
for i in range(a):
    b = list(map(int, input().split()))[1:] # 입력된 인풋을 int타입으로 리스트화
    mean = sum(b)/len(b)
    c = 0
    for j in b:
        if j > mean: c += 1
    print('%0.3f%%' %(c / len(b) * 100))
