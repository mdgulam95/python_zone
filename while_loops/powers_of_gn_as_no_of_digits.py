num=int(input('enter avalue'))
temp=num
res=1
count=0
while temp:
    temp//=10
    count+=1
temp=num
while temp:
    digit=temp%10
    print(f'{digit}  powers are {count}={digit**count}')
    temp//=10