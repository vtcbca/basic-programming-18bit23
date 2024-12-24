def triangle_pattern_list_comprehension(n):
    [print(" " * (n - i) * 2 + " ".join(str(x) for x in range(1, 2 * i))) for i in range(1, n + 1)]

n = int(input("Enter the number of lines: "))
triangle_pattern_list_comprehension(n)
