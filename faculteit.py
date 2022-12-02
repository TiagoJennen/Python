def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n - 1))
a = 6
print("Factorial of", a, "=", fact(a))