#co1 7a
l1=(2,4,6,7,8  )
l2=[6,8,9,0,4,9,9]
print("length of l1",len(l1))
print("length of l2",len(l2))
total=sum(l1)
print("sum of l1",total)
total=sum(l2)
print("sum of l2",total)
l3=[]
for number in l1:
    if number in l2:
        if number not in l3:
            l3.append(number)
print(l3)

