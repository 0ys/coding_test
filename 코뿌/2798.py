# 블랙잭
from itertools import *

n, m = map(int, input().split())
card = list(map(int, input().split()))

selected_card = list(combinations(card, 3))

sumlist = []
for s in selected_card:
    a = sum(s)
    if a <= m : sumlist.append(a)

result = max(sumlist)
print(result)