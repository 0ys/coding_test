# 소수 판별
n = int(input())
number = list(map(int, input().split()))

count = 0

for num in number:
    prime = True
    if num<2: continue
    for i in range(2, num//2+1):
        if num%i == 0: prime = False
    if prime: count += 1
    
print(count)