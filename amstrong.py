a=int(input('enter number'))
b=a
s=0
while a>0:
    n=a%10
    s=s+(n*n*n)
    a=a//10
if s==b:
    print(' this is armstrong number')
else:
    print('not')
    