import sys
sys.path.append('../math2remember')
from math2remember.extendedEuclidian import extendedEuclidian

def testExtendedEuclidian():
    gcd, x, y = extendedEuclidian(4,2)
    assert gcd == 2
    assert x == 0
    assert y == 1
    gcd, x, y = extendedEuclidian(173,11)
    assert gcd == 1
    gcd, x, y = extendedEuclidian(64,128)
    assert gcd == 64
    assert x == 1
    assert y == 0
    gcd, x, y = extendedEuclidian(24,412)
    assert gcd == 4
    assert x == -17
    assert y == 1


