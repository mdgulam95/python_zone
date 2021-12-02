num=int(input('enter a given number'))
res=0
for factor in range(1,num+1):
    if num  % factor==0:
        res+=factor
print(res)