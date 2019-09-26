m = int(input('First Number '))
n = int(input('Second Number '))

if m<n:
    m,n = n,m

def gcd(m,n):
#    while m%n != 0:
#        diff = m-n
#        m,n = max(n,diff) , min(n,diff)
#    return n
    if m%n == 0:
        return n
    else:
        return gcd(n,m%n)

print(gcd(m,n))
