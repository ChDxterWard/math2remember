import sys
sys.path.append('../math2remember')

from math2remember.getPrimeGen import getPrimeGen, getPrimeGenFromBruteForce, sieve

def testGetPrimeGenFromBruteForce():
    g = getPrimeGenFromBruteForce(-2)
    assert next(g) == 2
    assert next(g) == 3
    assert next(g) == 5
    assert next(g) == 7

def testGetPrimeGen():
    g = getPrimeGen()
    assert next(g) == 2
    assert next(g) == 3
    assert next(g) == 5
    assert next(g) == 7
    assert next(g) == 11
    
def testGetPrimeGenTo():
    assert [2]==sieve(2)
    assert [2,3]==sieve(4)
    assert [2,3, 5]==sieve(5)
    assert [2,3, 5]==sieve(6)
    assert [2,3,5,7]==sieve(7)


