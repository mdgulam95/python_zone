num=int(input("enter a number to prints its table"))
lower_limit=int(input("enter from where u want table to be printed"))
upper_limit=int(input("enter till where u want the table to be printed"))
for n in range(lower_limit,upper_limit+1):
    print('{}*{}={}'.format(num,n,(num*n)))