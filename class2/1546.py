N = int(input())
score = list(map(int, input().split()))
new_score = []
m = max(score)
result = 0

for s in score:
    new_s = s / m * 100
    new_score.append(new_s)
    result += new_s

result /= N
print(result)