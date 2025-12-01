import sys
import time
from myTime import myTime
sys.path.append('../math2remember')
from math2remember.getPrimeGen import getPrimeGen, getPrimeGenFromBruteForce


g1 = getPrimeGenFromBruteForce(2)
g2 = getPrimeGen()
for ITERATIONS in [100_000]:#range(10,1000,10):

    f = lambda: [next(g1) for _ in range(ITERATIONS)]
    t1 = myTime(f)

    print(f'time passed for bruteforce {t1} in {ITERATIONS} iterations')


    
    f = lambda: [next(g2) for _ in range(ITERATIONS)]
    t2 = myTime(f)
    print(f'time passed for wheel {t2} in {ITERATIONS} iterations')
    print(f'diff: {t1-t2}')
    print('####################')
