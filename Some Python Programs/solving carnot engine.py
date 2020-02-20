t1=int(input('Enter temperature of source or heat reservoir in degree centigrate.'))
t2=int(input('Enter temperature of sink or cold rservoir in degree centigrate'))
T1=t1+273
T2=t2+273
n=(1-T2/T1)*100
print('efficiency of carnot engine is',n,"%")

