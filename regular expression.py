# sequence of characters that specifies a match pattern in text.


# import re                                                                                  #match
# pattern="good"                                                                             #matches only first string
# if re.match(pattern,"good evening,how are you "):
#     print('yes')
# else:
#     print("sorry")


# import re                                                                                  #search
# pattern='good'
# if re.search(pattern,'hi good eve,how are you'):
#     print('yes')
# else:
#     print('sorry')


# import re                                                                                  #findall
# pattern='shazna' 
# b=re.findall(pattern,'dygkuhcijlkcshaznawgyutfeyghijklshaznaiugy7yuhshazna')
# print(b)
# c=len(b)
# print(c)   


# import re                                                                            #to substitute / edit /change
# str="hey prabhu shazna who are you"
# pattern='prabhu'
# b=re.sub(pattern,'hari ram',str)
# print(b)


# import re
# a='hi adarsh who are you'
# pattern='who'
# c=re.sub(pattern,'how',a)
# print(c)

# import re
# a=input('enter the pattern')
# if re.search(a,'good mrng,hi'):
#     print('found')
# else:
#     print('not')

# import re
# a=input('enter the pattern')
# b=re.findall(a,'gdhcuyshaznajchgfdhejshazna')
# print(b)
# print(len(b))

# import re
# a='my name is shazna'
# b='shazna'
# c=re.sub(b,'arshu',a)
# print(c)

import re
a=input("enter the string")
b=input('enter the string to be changed')
c=input('enter the new string')
d=re.sub(b,c,a)
print(d)