l='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
m='0123456789'
x=input('Enter Any Thing')
a=0
b=0
for i in x:
    if i in l:
        a=a+1
print('Total Alphabets are:',a)
for s in x:
    if s in m:
        b=b+1
print('Total integers are:',b)


        
