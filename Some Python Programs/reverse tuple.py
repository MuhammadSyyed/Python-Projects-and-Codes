t=[]
x=int(input('entries:'))
for i in range(x):
    y=int(input('enter any num..'))
    t.append(y)
print(tuple(t))
t.reverse()
print(tuple(t))
