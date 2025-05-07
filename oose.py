def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print("Factorial (iterative) of 5:", factorial_iterative(5))
