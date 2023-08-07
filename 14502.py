from itertools import *

# 데이터 입력받기
N, M = map(int, input().split())

lab = []
for _ in range(N):
  lab.append(list(map(int, input().split())))

temp = [[0] * M for _ in range(N)]

# 테스트 데이터
# N, M = 7, 7
# lab = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0],
#        [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0, 0, 0]]
# temp = [[0] * 7 for _ in range(7)]

# for i in range(N):
#   print(lab[i])
# print("-----------------")


def dfs(x, y):  # 상하좌우로 전염
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  if temp[x][y] == 0:
    temp[x][y] = 2
    dfs(x, y + 1)
    dfs(x, y - 1)
    dfs(x - 1, y)
    dfs(x + 1, y)
    return True
  return False


def mapCopy(N, M):
  # temp = [[0]*M for _ in range(N)]
  for n in range(N):
    for m in range(M):
      temp[n][m] = lab[n][m]


# 벽을 세우는 조합 찾기
empty = []
for n in range(N):
  for m in range(M):
    if lab[n][m] == 0:
      empty.append([n, m])
# print(f'empty: {empty}')

wall = list(combinations(empty, 3))
# print(f'wall: {wall[0][0]}')

result = 0
# 벽을 세우는 조합마다 바이러스 전염시키고 확인
for w in wall:
  mapCopy(N, M)
  # 벽 세우기
  for i in range(3):
    temp[w[i][0]][w[i][1]] = 1

  # 바이러스 전염시키기
  for n in range(N):
    for m in range(M):
      if temp[n][m] == 2:
        dfs(n, m + 1)
        dfs(n, m - 1)
        dfs(n - 1, m)
        dfs(n + 1, m)

  safe = 0
  # 안전 영역 확인
  for i in range(N):
    safe += temp[i].count(0)

  if safe > result: result = safe

# 지도 확인
# for i in range(N):
#   print(lab[i])
# print("=================")

print(result)
