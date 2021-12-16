def main():
    num=int(input('enter the number to check if it is perfect or not'))
    _perfect= is_perfect(num)
    print_perfect_or_not(_perfect,num)

def is_perfect(num):
    if num == sum_of_factors(num):
        return True
    return False

def sum_of_factors(num):
    res=0
    for div in range(1,num):
        if num % div ==0:
            res=add(res,div)
    return res

def add(num1,num2):
    return num1 + num2

def print_perfect_or_not(flag,num):
    if flag is True:
        print('perfect number')
    else:
        print('not an perfect number')

main()
