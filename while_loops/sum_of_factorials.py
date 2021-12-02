from typing_extensions import runtime


num=int(input('enter the value'))
temp=num
res=0
while temp:
    digit=temp % 10
    fact=1
    for n in range(digit,1,-1):
        fact *=n
    res+=fact
    temp//=10
    print(res)
    if num==res:
        print('strong number')
    else:
        print('not strong number')

