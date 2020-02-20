l=input('enter ')
m=list(l)
s=0
for i in m:
    s=s+(int(i)**3)

if s==int(l):
    print(s ,'is an amstrong number')
else:
        print(int(l),'is not an amstrong number')
