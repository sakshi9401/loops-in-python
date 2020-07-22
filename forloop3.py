#range increment sequence with 2 i.e., table of 2
for x in range(2,21,2):
    print(x)

#table of 3 else in for loop
for x in range(3,31,3):
    print(x)
else:
    print("\t\tfinally finished\t\t")

#nested for loop
a = {"john","nick","alex"}
b = {82,92,90}
for x in a:
    for y in b:
        print(x ,"secured",y,"marks")

#pass statement
for x in range(5):
    pass
