num=int(input('enter a given number to sum'))
temp=num
res=0
while temp:
    last=temp%10
    temp//=10
    res+=last
print(f'sum of {num}is {res}')