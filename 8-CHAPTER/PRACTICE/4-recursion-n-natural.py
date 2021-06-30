def sum_recursion(n):
    if n == 1 or n == 0:
        return 1
    return sum_recursion(n-1) + n


a = sum_recursion(5)
print(a)