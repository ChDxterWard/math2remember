from .isPrime import isPrime

def getPrimeGenFrom(n):
    
    pass

def getPrimeGenFromBruteForce(n):
    '''
    Checks every number starting from n if it is a prime number.
    If so it is returned.
    
    Args:
        n: The starting number. It only make sense to start with n=2 (n∈ℤ)
        
    Returns:
        The next prime number.
    '''
    while True:
        if isPrime(n):
            yield n
        n += 1

def getPrimeGen():
    yield 2
    yield 3
    q = 1
    while True:
        candidate1 = 6*q-1
        if isPrime(candidate1):
            yield candidate1
        candidate2 = 6*q+1
        if isPrime(candidate2):
            yield candidate2
        q += 1

def sieve(ceil):
    '''
    Create prime numbers with the upper bound of ceil (inclusive).
    
    Args:
        ceil: Positive integer (> 1)
        
    Returns:
        A list of prime numbers [2,3,...] where the last prime is ceil 
        (if ceil is a prime number)  or the the last prime number before 
        ceil.
    '''
    if ceil < 2:
        return []
    # Create an array from 0 to ceil+1. Init all with true.
    maybePrimes = [True] * (ceil+1)
    # 0, 1 are not prime.
    maybePrimes[0] = maybePrimes[1] = False
    # 2 is the first prime number.
    prime = 2
    
    # We take m with m <= ceil.
    # We write m=a*b<=ceil with a <= b.
    # Since a<=b <=> a*a<=a*b=m <=> a^2<=m<=ceil <=> a<=ceil**.5.
    # So every m has an factor a with a<=ceil**.5. 
    # a has an primefactor q with q<=a<=ceil**.5. We must have 
    # discovered q and its multiplies allready because q<=a<=ceil**.5.
    # So we discovered q and its multiples that are a and therefore m.
    # If all primes <= ceil**.5 are discovered all combined numbers 
    # are also discovered.
    while prime <= ceil**.5:
        if maybePrimes[prime]:
            # Now we know the current prime number.
            # In the next step we have to mark the multiplies of that number 
            # as false since these multiplies cant be primes.
            # To do so we start with prime^2 add prime in each step to
            # the current counter. With every step wir mark the current number 
            # as not prime until we reach the end.
            # We start with prime^2 beacause every multiple of prime < prime^2 
            # was already visitied. E.g.: prime is 5. 5*5 = 25. 
            # We look on 1*5,2*5,3*5,4*5. We see that the factors (1,2,3,4) 
            # are all smaller then 5. So we surely visited them earlier when 
            # we marked the multiples of 2 (and therefore 4) and 3.
            for multiple in range(prime*prime,ceil+1,prime):
                maybePrimes[multiple] = False
        prime += 1
        
    return [idx for idx in range(2, ceil+1) if maybePrimes[idx]]

if __name__ == '__main__':
    print(sieve(14))