n = input()
s = ""

for i in range(int(n)):
  for j in range(i + 1):
    s += "*"
  print(s)
  s = ""
