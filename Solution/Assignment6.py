def pattern_recursion(rows, current=1):
    if current > rows:
        return
    print("* " * current)
    pattern_recursion(rows, current + 1)

rows = int(input("Enter the number of rows: "))
pattern_recursion(rows)
