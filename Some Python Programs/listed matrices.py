M=[]
count=0
x=int(input('How many rows you want for first matrix ...?'))
y=1
while count<x:
    r=list(input('Enter elements for row w.r.t your desired columns..'))
    M.append(r)
    count+=1
    y=y+1
print('First matrix is',M)
    
N=[]
count=0
X=x
y=1
while count<X:
    r=list(input('Enter elements for row w.r.t your desired columns in second matrix..'))
    N.append(r)
    count+=1
    y=y+1
print('Second Matrix is',N)

P=[]
a=[int(M[0][0])+int(N[0][0]),int(M[0][1])+int(N[0][1]),int(M[0][2])+int(N[0][2])]
b=[int(M[1][0])+int(N[1][0]),int(M[1][1])+int(N[1][1]),int(M[1][2])+int(N[1][2])]
c=[int(M[2][0])+int(N[2][0]),int(M[2][1])+int(N[2][1]),int(M[2][2])+int(N[2][2])]
P.append(a)
P.append(b)
P.append(c)
print(P)










    
