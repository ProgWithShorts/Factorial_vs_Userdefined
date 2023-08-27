import time

def factorial_v1(n):
    if n < 0:
        return "Negative Number"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

start = time.time()
factorial_v1(30000)
end = time.time()

print((end-start)*1000, " ms")
