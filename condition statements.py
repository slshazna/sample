# a=20
# if a>=20:
#     print('yes')
# else:
#     print('no')


# a=int(input('enter a number'))
# if a>10:
#     print('a greater is than 10')
# else:
#     print('a is less than 10')

# a=input('enter username')
# b=int(input('enter password'))
# if a=='Shazna123' and b==12345:
#     print('Welcome')
# else:
#     print('Access Denied')

# a=int(input('enter a number'))
# if a>18:
#     print('adult')
# elif a>15:
#     print('young')
# elif a>10:
#     print('boy')
# else:
#     print('not eligible')

name=input('enter the name')
a=int(input('enter mark in physics'))
b=int(input('enter mark in chem'))
c=int(input('enter mark in bio'))
d=a+b+c
print('total',d)
if d>290:
    print('A+')
elif d>280:
    print('A')
elif d>270:
    print('B+')
elif d>260:
    print('B')
elif d>250:
    print('C+')
else:
    print('failed')
