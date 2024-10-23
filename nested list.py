# a=[1,2,3,[4,5],6]
# b=a[3][1]
# print(b)

# for i in range(1,30):
#     print(i)

for i in range(1,31):
    if (i%3==0 and i%5==0):
        print('hihello')    
    elif (i%3==0): 
        print('hi')
    elif (i%5==0):
        print('hello') 
    else:
        print(i)
        