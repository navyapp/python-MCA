#cos 6
string=input("enter any string:")
c=input("enter te character to the string")
count =0
for i in string:
  if i == c:
    count = count +1
print(c,"occurs",count,"times")