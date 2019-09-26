m = int(input('Enter first number '))
n = int(input('Enter second number '))

def factor(x):
    f=[]
    for i in range(1,x+1):
        if x%i == 0:
            f.append(i)
    return f

def gcd(m,n):
    fm = factor(m)
    fn = factor(n)

    cf = []

    for f in fm:
        if f in fn:
            cf.append(f)

    return max(cf)

gcdOfmn = gcd(m,n)
print(gcdOfmn)
