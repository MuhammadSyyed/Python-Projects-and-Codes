l1=[]
x=int(input('enter total entries'))
count=0
while count<x:
    y=int(input('enter any number'))
    l1.append(y)
    count=count+1
l1.sort()
print("l1 is",l1)

l2=[]
z=int(input('enter total entries'))
count=0
while count<z:
    w=int(input('enter any number'))
    l2.append(w)
    count=count+1
l2.sort()
print("l2 is",l2)
for i in l1:
    if i in l2:
        print(i,'is common')
    if i not in l2:
        print(i, 'is in l1 but not present in l2')
