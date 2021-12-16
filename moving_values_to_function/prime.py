#function to control everything using main
def main():
    num=int(input('Enter the number'))
    _prime=is_prime(num)
    print_prime_or_not(_prime,num)

    #function to check prime or not
def is_prime(num):
    if count_of_factors(num)==2:
        return True
    return False


    #function to count all the factors
def count_of_factors(num):
    count=int()
    for i in range(1,num+1):
        if num % i==0:
            count=add(count,1)  
    return count

    #functions to add two integer
def add(num1,num2):
    return num1+num2

    #to display the result
def print_prime_or_not(flag,num):
    if flag is True:
        print(f'{num} is prime number')
    else:
        print(f'{num} is not prime number')
main()  
