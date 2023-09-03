# 시험감독

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

supervisor = 0

for i in range(N):
    supervisor += 1
    if A[i] > B: student = A[i]-B 
    else: continue # 시험장에 있는 응시자보다 감독관이 볼 수 있는 사람이 많은 경우 제외
    if student % C:
        semi_supervisor = student // C + 1
    else:
        semi_supervisor = student // C
    supervisor += semi_supervisor
    
print(supervisor)