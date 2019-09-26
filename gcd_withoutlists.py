m = int(input('First Number '))
n = int(input('Second Number '))

def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
        gcf = i
    return gcf

print(gcd(m,n))
