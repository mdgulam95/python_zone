num=int(input('enter the value'))
copy=num
square=num*num
flag=True
while copy:
    if copy % 10!=square % 10:
        flag=False
        break
    copy//=10
    square=square//10
    if flag is true:
        print(f'{num}iscan automorphic number')
        else:
            print(f'{num} is not automorphic number')