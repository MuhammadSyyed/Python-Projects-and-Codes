l=[]
x=int(input('Enter total Entries'))
count=0
while count<x:
    z=int(input('Enter number for list'))
    l.append(z)
    count=count+1
print('list',l)
l.sort()
print(l)
for i in l:
    if l[0]<i:
        l[0]=i
print('The greatest integer is',l[0])
