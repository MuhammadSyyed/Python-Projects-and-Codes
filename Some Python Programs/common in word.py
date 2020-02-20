x=input('Enter something')
lower=0
upper=0
for i in x:
    s=ord(i)
    if s>96 and s<123:
        lower=lower+1
    else:
        upper=upper+1
print(lower)
print(upper)
        
