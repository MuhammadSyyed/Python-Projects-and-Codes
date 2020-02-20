#DecToBinary
def dec_bin(dec):
    a=""
    while dec>0:
        i=dec%2
        b=str(i)
        b=b[0]
        a=a+b
        
        if dec%2==0:
            dec=dec/2
        else:
            dec=(dec-1)/2
    a=a[::-1]
    print(a)
    


