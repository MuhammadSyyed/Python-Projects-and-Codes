def factorial(x):
    c=1
    for b in range (1,x):

        x=x*b
    if x<0:
            return('please enter positive number!!')
    elif x==0:
        return 1
    else:
        return (x)
def nPr(n,r):
    
    if n<0 or r<0:
        return 'error'
    elif r>n:
        return 'error'
    else:
        return factorial(n)/factorial(n-r)
def nCr(n,r):
    
    if n<r and n<0 and n==0 and r<0:
        return 'Error'
    else:
        x=factorial(n)/(factorial(r)*factorial(n-r))
        return x
    
