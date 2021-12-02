num=int(input('enter the value'))
copy=num
while copy:
    digit=copy%10
    fact=1
    for n in range(digit,1,-1):
        fact*=n
    print(f'each digit of {num}is {fact}')
    copy//=10    