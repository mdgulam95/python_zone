num=int(input('enter a number to reverse it'))
temp=num
res=0
while temp:
    last_digit=temp%10
    temp//=10
    res=res*10+last_digit
print(f'reverse of {num} is {res}')