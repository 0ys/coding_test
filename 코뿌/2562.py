# import numpy as np

# n = []
# for _ in range(9):
#   n.append(int(input()))

# print(max(n))
# print(np.argmax(n) + 1)
# 런타임 에러

n = []
maxnum = 0
for _ in range(9):
  n.append(int(input()))

maxnum = max(n)

print(maxnum)
print(n.index(maxnum) + 1)
