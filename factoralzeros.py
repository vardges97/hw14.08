def trailingzeros(n):

    count=0
    i =5
    while(n/i>=1):
        count +=int(n/i)
        i *= 5
    return int(count)

n=1000
print("number of trailing zeros is",trailingzeros(n))