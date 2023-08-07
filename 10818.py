n = int(input())
number = list(map(int, input().split()))
#print(number)

# min_num = 1000000
# max_num = -1000000

# for i in range(n):
#   if min_num > number[i]: min_num = number[i]
#   if max_num < number[i]: max_num = number[i]

# print(min_num, max_num) # 672ms

print(min(number), max(number))  # 392ms

# 비교문 반복으로 쓰는 것보다 min, max 함수 사용하는 것이 훨씬 빠름
