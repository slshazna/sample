# a=(3,7,9,5,8,"shazna")
# b=list(a)
# # b.append(10)
# # b.insert(3,"apple")
# # b.pop(3)
# # b.remove(7)
# # c=tuple(b)
# print(b)


a=int(input('enter a number'))
b=a
s=0
while a>0:
    n=a%10
    s=s+(n*n*n)
    a=a//10
if s==b:
    print("armstrong")
else:
    print(" not")
