l=[]
x=int(input('Enter total entries'))
count=0
while count<x:
    z=int(input('Enter any number'))
    l.append(z)
    count=count+1
print('list is',l)
l.sort()
print(l)
i=l[-1]
print("the greatest integer in your given list is",i)
