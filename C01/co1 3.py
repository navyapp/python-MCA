#co1 2a
list=[1,2,3,4,5,6,7,8,-3,-5]
a=[x for x in list if x>0]
print(a)

#co1 2b
n=int(input("enter the limit"))
list=[]
for x in range(n):
  x=int(input("enter the number"))
  list.append(x)
print(list)
sqrlist =[x**2 for x in list]
print(sqrlist)

#co1 2c
word="mango"
vowels="a,e,i,o,u"
list=[x for x in word if x in vowels]
print(list)

#co1 2d
word="orange"
list=[ord(x) for x in word]
print(list)