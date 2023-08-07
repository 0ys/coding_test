# h, m = map(int, input().split())

# if h == 0: h = 24

# tm = h * 60 + m
# tm -= 45

# hour = tm // 60
# minute = tm % 60

# print(hour, minute)
# 반례: 0 50 -> 24 5로 출력됨

h, m = map(int, input().split())

if m < 45 and h == 0: h = 24

tm = h * 60 + m
tm -= 45

hour = tm // 60
minute = tm % 60

print(hour, minute)
