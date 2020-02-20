x=[]
y=int(input('How many integers you want..?'))
for i in range(y):
    z=int(input('Number'))
    x.append(z)
print(x)
a=sum(x)
b=a/y
print(b)

