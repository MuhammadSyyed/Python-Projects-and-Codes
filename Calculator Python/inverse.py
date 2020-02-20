from permutation import factorial
pi=3.1415926535897932384650288
def com(x):
    com=factorial(2*x)/(factorial(x)*factorial(x))
    return com

def arcsin(x):
    if x<1:
        a=0
        for n in range(1,11):
            a=a+(com(n)*(x**(2*n+1))/((4**n)*(2*(n)+1)))

        b=x+a
        c=b*180/pi
        return c
    elif x==1:
        return 90
    else:
        retutn ('Math error')
        
        
def arccos(x):
    if x<1:
        a=((pi/2)-(arcsin(x))*pi/180)
        b=a*180/pi
        return b
    elif x==1:
        return 0
    else:
        return ('Math error')

def arctan(x):
    a=arcsin(x/((x**2)+1)**(1/2))
    atan=a*180/pi
    return atan
