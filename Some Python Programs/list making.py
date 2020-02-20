l=[]
z=int(input("Input numbers for entries"))
count=0
while count<z:
    x=int(input('enter any numer'))
    l.append(x)
    count=count+1
print("list is",l)
for x in [0,z-1]:
    
    l.sort()
    if l[x]==l:
        print('there are duplicate item in the list')
    elif l[x]==l[-1]:
        print('thera are duplicate item in the list')
    else:
        print()
