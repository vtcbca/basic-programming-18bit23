def reverse_string_list(s):
    str_list = list(s)
    str_list.reverse()
    return ''.join(str_list)

input_str = input("Enter a string: ")
print(f"Reversed string (using list and join): {reverse_string_list(input_str)}")
