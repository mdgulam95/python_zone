num=int(input('enter the given number'))
copy=num
count=0
res=0
while copy:
    copy//=10
    count+=1

copy=num
while copy:
    digit=copy % 10
    copy//=10
    copy=num
    while copy:
            digit=copy % 10
            copy//=10
            res=res+digit**count
    if res==num:
        print('amstrong number')
    else:
        print('not amstrong number')