import time
def myTime(f):
    start = time.time()
    f()
    end = time.time()
    return end - start

def myTimeIterations(f, ITERATIONS):
    start = time.time()

    f()
    end = time.time()
    return end - start