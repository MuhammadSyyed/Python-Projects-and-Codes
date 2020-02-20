def log(number):
    x=(number)**(1/32768)
    y=(x-1)
    z=(y/0.000070271)
    return(z)
    
def antilog(number):
    
    x=(number*(0.000070271))
    y=(x+1)
    z=y**(32768)
    return(z)
    
def ln(number):

    x=(number)**(1/32768)
    y=(x-1)
    z=(y/0.000070271)

    a=(2.71828188)**(1/32768)
    b=(a-1)
    c=(b/0.000070271)

    Ln=z/c
    return(Ln)
