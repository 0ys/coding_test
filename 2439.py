n = int(input())
s = ""

for i in range(1, n + 1):
  blank = n - i
  for j in range(n):
    if blank > j: s += " "
    else: s += "*"
  print(s)
  s = ""
