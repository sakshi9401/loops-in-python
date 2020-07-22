#find factorial using while
n = int(input("enter value of n"))
f = 1
i = 1
if n <0:
    print("factorial of negative number is not possible")
elif n ==0:
    print("factorial of 0 is 1")
else:
    while i<=n:
        f = f*i
        i = i+1
    print("fact of",n,"is",f)
