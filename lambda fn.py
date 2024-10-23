
# A lambda function is a small anonymous function. 
# A lambda function can take any number of arguments, but can only have one expression


# a=lambda x,y:x+y
# print(a(3,4))

# a=[1,2,3,4,5,6,7,8,9,10]                                   #filter()
# b=filter(lambda x:x%2==0,a)
# print(list(b))

# a=[1,2,3,4,5]
# b=map(lambda x:x*x,a)                                       #map()
# print(list(b))


# from functools import reduce                               #reduce()

# a=[1,2,3,4,5,6,7,8,9]
# b=reduce(lambda x,y:x*y,a)
# print(b)


# 132
# 1+3+2=6
# 1*3*2=6                                                     #spy numbers
# sum==product

# a=int(input('enter the number'))
# sum=0
# product=1
# while a>0:
#     digit=a%10
#     sum=sum+digit
#     product=product*digit
#     a=a//10
# if sum==product:
#     print("spy number")
# else:
#     print("not a spy number")


