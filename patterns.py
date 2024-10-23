# a=int(input('enter the range'))
# for i in range(a):                                                                #incrementing pyrmaid 
#     for j in range(i+1):
#         print('*',end=' ')
#     print()    
        

# a=int(input('enter the range'))                                                   #decrementing pyramid
# for i in range(a):      
#     for j in range(a-i):
#         print('*',end=' ')
#     print()

# a=int(input('enter the range'))                                                     #square pyramid                  
# for i in range(a):      
#     for j in range(a):
#         print('*',end=' ')
#     print()

# a=int(input('enter the range'))                                                        #number pyramid
# for i in range(a):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# n=int(input('enter the range'))                                                          #hollow square
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or i==0 or j==n-1:
#            print('*',end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# a=int(input('enter the range'))
# for i in range(1,a+1):                                                                #star pyramid
#     spaces=' '*(a-i)
#     stars='*'*(2*i-1)
#     print(spaces+stars)

a=int(input('enter the range'))                                                        #L shaped pattern
for i in range(a-1):
    print('*',end=' ')
    print()  
print("* " *a)







