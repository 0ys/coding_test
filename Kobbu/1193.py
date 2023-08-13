# 분수 찾기 풀이 https://blog.naver.com/artohol/223180011350
x = int(input())

theNum = 0 # 기준값
i = 0
count = 0
while(x>theNum):
    i += 1
    theNum += i
    if i % 2 == 0: 
        a, b = i, 1
        count += 1
    else:
        a, b = 1, i
        count += 1
    
# print(theNum)
# print(f'a, b = {a, b}')
# print(f'c ={count}')

minus = theNum-x
for _ in range(minus):
    if count%2 == 0: 
        # print('up')
        a -= 1
        b += 1
    else: 
        # print('down')
        a += 1
        b -= 1
        
        
print(f'{a}/{b}')



# a, b = 1, 1
# count = 0
# list = []
# list.append(f'{a}/{b}')

# odd = False
# even = False
    

# while(x>count):
#     if a==1: 
#         b += 1
#         count += 1
#         list.append(f'{a}/{b}')
#         # moveDown once
#         a += 1
#         b -= 1
#         count += 1
#         list.append(f'{a}/{b}')
#         odd = False
#         even = True
#     elif b==1: 
#         a += 1
#         count += 1
#         list.append(f'{a}/{b}')
#         # moveUp once
#         a -= 1
#         b += 1
#         count += 1
#         list.append(f'{a}/{b}')
#         odd = True
#         even = False
#     else:
#         if odd:
#             # moveUp once
#             a -= 1
#             b += 1
#             count += 1
#             list.append(f'{a}/{b}')
#         if even:
#             # moveDown once
#             a += 1
#             b -= 1
#             count += 1
#             list.append(f'{a}/{b}')
        
        
    
        
# # print(list)
# print(list[x-1])
