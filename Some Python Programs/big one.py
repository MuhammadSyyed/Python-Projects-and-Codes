M=[]
count=0
x=int(input('How many rows you want...?'))
while count<x:
    r1=[]
    y=int(input('how many columns you want...?'))
    count1=0
    while count1<y:
        z=int(input('element'))
        r1.append(z)
        count1+=1
    r2=[]
    a=y
    count2=0
    while count2<a:
        b=int(input('element'))
        r2.append(b)
        count2+=1
    r3=[]
    p=y
    count3=0
    while count3<p:
        q=int(input('element'))
        r3.append(q)
        count3+=1
    M.append(r1)
    M.append(r2)
    M.append(r3)
    count+=1
print(M)
