num=int(input('enter a number'))
temp=num
res=0
while temp>0:
    res=res*10+temp%10
    temp//=10
if(num==res):
    print("palindrome number")
else:
    print("not palindrome")