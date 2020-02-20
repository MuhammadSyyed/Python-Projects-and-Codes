x=input('Enter Your Name')
y=len(x)
z=50
if y%2==0:
    for i in range(z+1):
        if i%2==0:
            print(i)
else:
    for j in range(z+1):
        if j%2!=0:
            print(j)
