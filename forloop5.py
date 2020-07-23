#program to find sum of digit
n = int(input("enter the value of n"))
s = 0
i = n
for i in range(int(i/10)):
    r =i%10
    s = s+r
print("sum of digits",s)