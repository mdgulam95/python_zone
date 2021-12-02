def greaterof3():
    a=input('enter a value')
    b=input('enter b value')
    c=input('enter c value')
    if (a>b) & (a>c):
        print("a is bigger,a")
    elif (b>a) & (b>c):
        print("b is bigger,b")
    else:
        print("c is bigger,c")
greaterof3()           