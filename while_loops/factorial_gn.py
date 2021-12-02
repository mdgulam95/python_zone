num=int(input('enter the factorial number'))
n=1
factorial=1
while n<=num:
    factorial*=n
    n+=1
print(f'{num}! is {factorial}')
