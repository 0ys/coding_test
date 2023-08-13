while(True):
    number = list(map(int, input().split()))
    number.sort()
    
    a = number[0]
    b = number[1]
    c = number[2]
    
    right = ''
    
    if a ==0 and b ==0 and c==0: break
    if c*c == a*a + b*b: result = 'right'
    else: result = 'wrong'
    
    print(result)