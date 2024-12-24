def fibonacci_generator(max_value=None, terms=None):
    a, b = 0, 1
    count = 0
    while True:
        if max_value is not None and a >= max_value:
            break
        if terms is not None and count >= terms:
            break
        yield a
        a, b = b, a + b
        count += 1

choice = input("Generate by (terms/max): ").strip().lower()
if choice == "terms":
    num_terms = int(input("Enter the number of terms: "))
    print(f"Fibonacci sequence (up to {num_terms} terms): {list(fibonacci_generator(terms=num_terms))}")
elif choice == "max":
    max_val = int(input("Enter the maximum value: "))
    print(f"Fibonacci sequence (less than {max_val}): {list(fibonacci_generator(max_value=max_val))}")
