def oct_dec(y):
    y=str(y)
    list1=[]
    c=len(y)-1
    b=0
    for a in y:
        x=int(a)*(8**c)
        list1.append(x)
        c=c-1
    d=sum(list1)
    return(str(d)+'₁₀')

#=============================================#

def bin_dec(y):
    y=str(y)
    list1=[]
    c=len(y)-1
    b=0
    for a in y:
        x=int(a)*(2**c)
        list1.append(x)
        c=c-1
    d=sum(list1)
    return(str(d)+'₁₀')

#============================================#

def hex_dec(y):
    y=str(y)
    list1=[]
    c=len(y)-1
    b=0
    for a in y:
        if a=='A':
            a='10'
        elif a=='B':
            a='11'
        elif a=='C':
            a='12'
        elif a=='D':
            a='13'
        elif a=='E':
            a='14'
        elif a=='F':
            a='15'
            
        x=int(a)*(16**c)
        list1.append(x)
        c=c-1
    d=sum(list1)
    return(str(d)+'₁₀')
#=====================#

def dec_bin(y):
    a=""
    while y>0:
        i=y%2
        b=str(i)
        b=b[0]
        a=a+b
        y=y//2
    a=a[::-1]
    return(a+'₂')
#==============================#
def dec_oct(y):
    a=""
    while y>0:
        i=y%8
        b=str(i)
        b=b[0]
        a=a+b
        y=y//8
    a=a[::-1]
    return(a+'₈')
    
#=====================================#
def dec_hex(y):
    a=""
    while y>0:
        i=y%16
        b=str(i)
        b=b[0]
        if i==10:
            b='A'
        elif i==11:
            b='B'
        elif i==12:
            b='C'
        elif i==13:
            b='D'
        elif i==14:
            b='E'
        elif i==15:
            b='F'
        a=a+b
        y=y//16
    a=a[::-1]
    print(a+'₁₆')


    




    
    
    
