#from isPrime import isPrime 
from .isPrime import isPrime
def getPrimeGenFromBruteForce(n):
    while True:
        if isPrime(n):
            yield n
        n += 1

'''
a = m*q+r
a = 6*q+r with r ∈ [0,1,2,3,4,5]
a0 = 6*q+0 ... 6 | a0 -> not prime
a1 = 6*q+1 ... maybe prime
a2 = 6*q+2 ... 2 | a2 -> not prime
a3 = 6*q+3 ... 3 | a3 -> not prime
a4 = 6*q+4 ... 2 | a4 -> not prime
a5 = 6*q+5 ≡ 6*q-1 ... maybe prime

as we take m=6=2*3 we exclude all pultiples of 2 and 3 as prime candidates.
'''
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
    while prime <= ceil**.5:
    #while prime*prime <= ceil:
        # If maybePrimes[prime] is true it was not marked as an multiply
        # of another number -> prime!
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

def getPrimeGenTo(n):
    return sieve(n)

if __name__ == '__main__':
    print(sieve(14))