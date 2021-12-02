num1=int(input('enter the starting point'))
num2=int(input('enter the end point'))
_=num1
res=1
while _<=num2:
    res*=_
    _+=1
print(f'sum of all the numbers in range from {num1} to {num2} is {res}')