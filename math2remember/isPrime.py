from math import sqrt
from .extendedEuclidian import isCoprime
def isPrime(n):
    '''
    Checks if n is a prime number or not.
    
    Args:
        n: Positive integer (> 1)
        
    Returns:
        True if n is a prime number False otherwise.
    '''
    
    if n == 2:
        return True
    # 2 is the smallest prime number and every even number except from 2 is not prime.
    if n<2 or n%2==0:
        return False
    # We test from 2 to √n.
    # We only need to test to √n because we have two options:
    # Option 1. n∈ℕ is a combined number n=a*b and therefore not an prime.
    # We say a≤b and therefore a²≤a*b=n. We see: a²≤n and therefore a≤√n.
    # It is clear that n has an factor a that is less/equal than √n.
    # So we only have to look to √n  to find the factor a for n.
    # If we found that factor a the other factor b is not important anymore because
    # we already can evenly divide n by a and can see that n is not prime.
    # If we check further than √n and n is not prime we will find the factor b 
    # that also divide n. 
    # But b is only complementary to the already found a.
    # Option 2. If option 1 is false n∈ℕ must be a prime number.
    #
    # The + 1 is needed to test inclusive to √n.
    for i in range(2, int(sqrt(n)) + 1):
        if n%i==0:
            return False
    return True

def isPrimeFermat(n, bases=[2]):
    '''
    Checks if n is a prime number or not.
    It uses little fermat. It is important to know, that
    if isPrimeFermat return True it means that n is most likely a prime.
    It is based on the following equation
        a^(n-1)≡1 mod n
    that is an specification of a^n≡a mod n for n is prime.
    In the first equation gcd(a,n) must be 1. We come from
    the second to the first equation by dividing the equation
    by the modular inverse a^-1.
    To come to a^(n-1)≡1 mod n we look at a example with
    n=7 and a=3.
    First we write all elements of the rest classes mod n.
    That are 1,2,3,4,5,6. 
    If we multiply every representative of the rest classes with a=3 we have:
        1*3      ≡ 3 mod 7
        2*3      ≡ 6 mod 7
        3*3 = 9  ≡ 2 mod 7
        4*3 = 12 ≡ 5 mod 7
        5*3 = 15 ≡ 1 mod 7
        6*3 = 18 ≡ 4 mod 7 (0)
    We see that every number from the rest classes still appears.
    Lets write this down as an product:
        (1*3)*(2*3)*(3*3)*(4*3)*(5*3)*(6*3) mod 7 
        = 3*6*2*5*1*4 mod 7 (1)
    In other words: (1·2·3·4·5·6) * 3^6  ≡  (1·2·3·4·5·6)  (mod 7)
    Now we have the equation (1). We can shorten (1).
    First we cancel 1: 
        3*(2*3)*(3*3)*(4*3)*(5*3)*(6*3) mod 7 = 3*6*2*5*4 mod 7
    After this we can cancle 2:
        3*3*(3*3)*(4*3)*(5*3)*(6*3) mod 7 = 3*6*5*4 mod 7
    and so on.
    We can cancle every representative of the rest classes.
    After this we get:
        3*3*3*3*3*3 mod 7 = 1 mod 7 = 3^6 ≡ 1 mod 7
    This only works because n=7 is prime. If n is not prime
    (0) would add/remove some representative. The final 
    euation would be ≠ 1.
    
    Args:
        n: Positive integer (> 1)
        bases: A list of positive integers > 1. 
        
    Returns:
        True if n is most likely a prime number False otherwise.
    '''
    if n < 2:
        return False
    # Since a is 2 in this case we make a fallback and auto return 
    # True if n is 2. If we would not do this gcd(a,n)=2 if n=2.
    if n == 2:
        return True
    
    #pow(2,n-1,n) == 1
    return all([isCoprime(base,n) and pow(base,n-1,n) == 1 for base in bases]) 
    