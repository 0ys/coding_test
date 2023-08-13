n, m = list(map(int, input().split(' ')))
tree = list(map(int, input().split()))

start = 0
end = max(tree) # 가장 높은 나무를 끝점으로 설정

# 이진 탐색
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2

    # 잘랐을 때의 나무 양 계산
    for x in tree:
        if x > mid:
            total += x - mid

    if total < m: # 원하는 양보다 적을 때
        end = mid - 1 # 나무를 더 많이 자름
    else:
        result = mid # 가장 덜 자를 때를 기록 
        start = mid + 1 # 나무를 덜 자름

print(result)