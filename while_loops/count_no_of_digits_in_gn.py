num=int(input('enter a value'))
count=0
copy=num
while copy:
    copy//=10
    count+=1
    print(f'{num} has {count} number of digits')