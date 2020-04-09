# 10039
scores = []
for i in range(5):
    score = int(input())
    if score >= 40: scores.append(score)
    else: scores.append(40)
print(round(sum(scores)/5))