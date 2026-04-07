m, n = map (int, input("Input your two numbers (space separated): ").split())

a = m
b = n

while m != n:
    if m > n:
        m -= n
    elif n > m:
        n -=m

print("The GCD of ", a, "and", b, "is:", m)