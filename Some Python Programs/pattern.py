x=input('Input any string')
a=int(input('any number for domain'))
b=int(input('range for number of lines'))
for i in range(a,b):
    print("\t",i*x)
for i in range(b,a-1,-1):
    print("\t",i*x)
