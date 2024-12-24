def alphabet_pattern_list_comprehension(n):
    [print(" " * (n - i) * 2 + 
           " ".join(chr(64 + x) for x in range(1, i + 1)) + 
           " " + 
           " ".join(chr(64 + x) for x in range(i - 1, 0, -1))) 
     for i in range(1, n + 1)]

n = int(input("Enter the number of lines: "))
alphabet_pattern_list_comprehension(n)
