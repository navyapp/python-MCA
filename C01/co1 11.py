n1=int(input("enter the number n1:"))
n2=int(input("enter the number n2"))
n3=int(input("enter the number n3:"))
if n1>n2:
    if n1>n3:
        print("the biggest number is ",n1)
    else:
        print("te biggest number is ",n3 )
elif n2>n3:
    print("the biggest number is",n2)
else:
    print("the biggest number is ",n3)
