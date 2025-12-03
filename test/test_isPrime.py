import sys
sys.path.append('../math2remember')
from math2remember.isPrime import isPrime, isPrimeFermat

def testIsPrime():
    assert isPrime(0)==False
    assert isPrime(-2)==False
    assert isPrime(1)==False
    assert isPrime(2)==True
    assert isPrime(4)==False
    assert isPrime(3)==True
    assert isPrime(20)==False
    assert isPrime(21)==False
    assert isPrime(23)==True
    
def testIsPrimeFermat():
    assert isPrimeFermat(0)==False
    assert isPrimeFermat(-2)==False
    assert isPrimeFermat(1)==False
    assert isPrimeFermat(2)==True
    assert isPrimeFermat(4)==False
    assert isPrimeFermat(3)==True
    assert isPrimeFermat(20)==False
    assert isPrimeFermat(21)==False
    assert isPrimeFermat(23)==True