m = int(input('First Number '))
n = int(input('Second Number '))

def gcd(m,n):
    i = min(m,n)
    while i > 0: 
        if m%i==0 and n%i==0:
            return i
        else:
            i = i-1

print(gcd(m,n))
