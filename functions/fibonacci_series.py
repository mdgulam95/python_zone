def fibonacci():
    x=0
    y=1
    z=0
    num=int(input('enter the nuimber'))
    while (z<=num):
        print(z,end='\t')
        x=y
        y=z
        z=x+y
    
fibonacci()