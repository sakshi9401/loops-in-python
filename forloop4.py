#to find factorial of any number
num = int(input("Enter the value of num"))
f=1
if num <0:
    print("factorial of negative numbers is not possible")
elif num == 0:
    print("factorial of 0 is 1")
else :
    for i in range(1,num + 1):
        f = f*i
    print("factorial of",num,"is",f)