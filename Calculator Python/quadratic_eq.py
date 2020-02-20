def quad(a,b,c):
    x1=(-b+(b**2-(4*a*c))**0.5)/(2*a)
    x2=(-b-(b**2-(4*a*c))**0.5)/(2*a)
    return (x1,x2)
