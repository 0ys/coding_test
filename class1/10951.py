import sys

for line in sys.stdin:
  a, b = map(int, line.split())
  print(a + b)

# sys.stdin 라이브러리에 대해서 공부

# 태정이 풀이
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break