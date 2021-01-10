from matplotlib import pyplot as plt
import math
'''
a. comoute the sum of the first n natural numbers
b. check if prime
c. gcd between a and b
d. first prime number greater that a given n
e. first k prime numbers greater than n
'''
def f(x):
    return x ** 3 - 2 * x ** 2 + x - 5

def gauss(n):
    return n * (n + 1) / 2

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True;

def first_prime_after(n):
    p = n + 1;
    while (not prime(p)):
        p += 1
    return p

def first_k_primes_after(n, k):
    primes = []
    for i in range(k):
        n = first_prime_after(n)
        primes.append(n)
    return primes

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

if __name__ == '__main__':
    '''n = int(input("Enter a number: "))
    print("Sum of first ", n, " numbers is: ", gauss(n))
    if prime(n):
        print(n, " is prime.")
    else:
        print(n, " is NOT prime.")
    a = n
    b = int(input("Enter a second number: "))
    print("Greatest common divisor between ", a, " and ", b, " is ", gcd(a, b))
    n = int(input("Enter a third number: "))
    print("The first prime number after ", n, " is ", first_prime_after(n))
    k = int(input("How many primes do you want? "))
    print(first_k_primes_after(n, k))

    plt.plot(range(k), first_k_primes_after(n, k))
    plt.show()'''
    print(gcd(-12, 6))