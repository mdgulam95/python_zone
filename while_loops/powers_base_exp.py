num1=int(input('enter a base value'))
num2=int(input('enter a exponent'))
_=num2
res=1
while _!=0:
    res*=num1
    _-=1
print(f'{num1} power of {num2} is {res}')