from sympy import isprime

num = int(input("Enter a number: "))
print(f"{num} is {'a prime' if isprime(num) else 'not a prime'} number.")
