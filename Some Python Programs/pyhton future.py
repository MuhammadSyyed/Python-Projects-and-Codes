x=int(input("Enter Any Number For Range: "))
for i in range(2,x+1):
    y=0
    for j in range(2,i//2+1):
        if(i%j==0):
            y=y+1
    if(y<=0):
        print(i)
