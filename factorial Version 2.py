import time
import sys
sys.setrecursionlimit(30_002)

def factorial_v2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_v2(n-1)

start = time.time()
factorial_v2(30000)
end = time.time()

print((end-start)*1000, " ms")

