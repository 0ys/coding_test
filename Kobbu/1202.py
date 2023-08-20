# 보석 도둑
# import heapq

# N, K = map(int, input().split())
# gem = []
# bag = []

# for _ in range(N):
#     M, V = map(int, input().split())
#     gem.append((M, V))

# for _ in range(K):
#     C = int(input())
#     bag.append(C)

# gem.sort(key=lambda x:-x[1])
# bag.sort()

# print(gem)
# print(bag)

# result = 0
# for v, m in gem:
#     print(f'weight:{m}, value:{v}')
#     for c in bag:
#         print(f'bag:{c}')
#         if m<=c:
#             result += v
#             print(result)
#             bag.remove(c)
#             break

import sys
import heapq
input=sys.stdin.readline
n,k = map(int,input().split())
gems = [[*map(int,input().split())] for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort();bags.sort()
result = 0;tmp = [] 
 
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp, -gems[0][1])
        heapq.heappop(gems)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)

