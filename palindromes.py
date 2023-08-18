def palindrome(n):
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //=10
    return (n==rev)
ls1 = []
for i in range(100000,1000000):

    if palindrome(i):
        ls1.append(i)
print(ls1)
#list isnt pretty