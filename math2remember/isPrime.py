from math import sqrt
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
