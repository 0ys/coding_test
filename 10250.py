T = int(input())

for _ in range(T):
  room = []
  H, W, N = map(int, input().split())
  for w in range(W):
    for h in range(H):
      room.append((h + 1) * 100 + (w + 1))
  print(room[N - 1])
