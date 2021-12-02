num=int(input('enter the value'))
count=0
for factor in range(1,num+1):
    if num % factor==0:
        count+=1
        if count==2:
            print('prime number')
        else:
            print('not prime number')