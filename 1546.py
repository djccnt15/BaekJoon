# 1546
a = int(input())
score = list(map(int, input().split())) # 입력된 인풋을 int타입으로 리스트화
new_score = []
for i in score: new_score.append(i / max(score) * 100)
r = 0
for i in new_score: r += i
print(r/len(new_score))