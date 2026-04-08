def multiplicative_fibonacci(n):
    if n <= 0:
        return 2
    elif n == 1:
        return 3
    else:
        return multiplicative_fibonacci(n-1) * multiplicative_fibonacci(n-2)

"""
For anyone reading this, my function begins with 2, 3, leading to much larger values faster, compared to 1,2.
If I were to set the first numbers to 1, 1 or 1,0 as I tried, it would always return 1 or 0 respectively.
"""


n = int(input("n: "))
print(multiplicative_fibonacci(n))