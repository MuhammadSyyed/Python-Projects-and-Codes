x=[]
y=int(input('How many number you want?'))
for i in range(y):
    z=int(input('Number'))
    x.append(z)
print(x)
a=y
if a%2!=0:
    b=(a+1)//2
    c=int(b-1)
    print(x[c])
else:
    b=(a+1)//2
    b=b//2
    c=int(b)
    d=int(b+1)
    print('The Median is Between two numbers',x[c],'and',x[d],'which is',(x[c]+x[d])/2)
