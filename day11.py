#While loop
# x = 1 
# while x <= 10:
#     print(x, end=' ')  # 1 infinte loop
# print()
# x = 1 
# while x <= 10:
#     print(x, end=' ')  # 1 3 5 7 9
#     x += 2
# print()
# x = 1
# while x <= 10:
#     print(x, end=' ')  # 1 2 4 8
#     x *= 2 
# print() 

# x = 10 
# while x >= 0:          
#     print(x, end=' ') #10 8 6 4 2 0
#     x -= 2 
# print() 

# x = 10 
# while x > 0:           #no = 0, because // last value is 0
#     print(x, end=' ')# 10 5  2 1    
#     x //= 2 
# print() 

# #else 
# x = 1 
# while x < 5:
#     if x % 2 == 1:
#         x += 1
#         continue 
#     print(x, end=' ') # 2 4 loop completed succesfully
#     x += 1
# else:
#     print('Loop completed successfully')
# print()

# x = 1 
# while x < 5:
#     if x == 4:
#         break 
#     print(x, end=' ') # 1 2 3 
#     x += 1
# else:
#     print('Loop completed successfully')
# print()

# #nested loops
for x in range(1,4):
    for y in range(4,7):
        print((x,y), end=' ')
print('\n')
# for x in range(1,3):
#     for y in range(3,5):
#         for z in range(5,7):
#             print((x,y,z), end=' ')

#matrix 
# matrix = [ [4,5,6], [1,2,3], [7,8,9]]
#print matrix row-wise
#print matrix col-wise