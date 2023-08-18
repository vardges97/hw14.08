def divisors(a,b):
    if (b==0):
        return a
    else:
        return divisors(b,a%b)

print(divisors(20,35))