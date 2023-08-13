n = input()
p = ""

for _ in range(int(n)):
  r, string = input().split()
  # print(r, string)
  for s in string:
    for _ in range(int(r)):
      p += s
  print(p)
  p = ""