import time
import math

start = time.time()
math.factorial(30000)
end = time.time()

print((end-start)*1000, " ms")
