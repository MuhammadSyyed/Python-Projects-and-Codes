t=[(1,2),(2,3),(3,4)]
print(t)
s=[]
for i in t:
    i=list(i)
    s.append(i)
p=[]
for j in s:
    j[-1]=30
    p.append(j)
q=[]
for a in p:
    a=tuple(a)
    q.append(a)
print('the replaced tuple will be',q)
