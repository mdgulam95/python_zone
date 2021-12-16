def main():
    print('this is a program to print 1st n prime numbers')
    n=int(input('enter a value of n'))
    print_n_prime_numbers(n)

def print_n_prime_numbers(n):
    count_of_prime_numbers=0
    num=2
    while count_of_prime_numbers <n:
        if is_prime(num) is True:
            print(f'{num} is a prime number')
            count_of_prime_numbers=sum((count_of_prime_numbers,1))
        num=sum((num,1))

def is_prime(num):
    if count_of_factors(num) ==2:
        return True
    return False

def count_of_factors(num):
    count=int()
    for i in range (1,num+1):
        if num % i ==0: 
            count=sum((count,1))
    return(count)

main()
