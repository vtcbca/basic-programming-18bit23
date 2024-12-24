from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

num = int(input("Enter a number: "))
print(f"Factorial using reduce: {factorial_reduce(num)}")
