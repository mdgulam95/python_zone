b=int(input('enter a base value'))
p=int(input('enter the exponent'))
res=1
for i in range(0,p,1):
    res*=b
    print(f'{b}topower{p}={res}')