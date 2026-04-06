def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
n = 5
pyramid(n)
