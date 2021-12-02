num=int(input('enter a value'))
n=1
factorial=1
while n<=num:
    factorial*=n
    n+=1
print(f'{num}!={factorial}')