n, r = map(int, input().split())

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def bino_coef_factorial(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

result = bino_coef_factorial(n, r)
print(result)

# 참고: https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients