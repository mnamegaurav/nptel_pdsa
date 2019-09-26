#program for reversing a number
def intreverse(n):
    num = str(n)
    num = num[::-1]
    return num


#program for matching brackets in given string
def matched(s):
    counter = 0
    for bracket in s:
        if bracket == ')':
            counter -= 1
            if counter < 0:
                return False
            
        elif bracket == '(':
            counter += 1
    return counter == 0


#program for sum of prime in a given list of numbers
def sumprimes(l):
    
    def factor(n):
        factors = []
        for i in range(1,n+1):
            if n%i == 0:
                factors.append(i)
        return factors

    def isprime(n):
        f = factor(n)
        if f == [1,n]:
            return True
    
    sum = 0
    for num in l:
        if isprime(num):
            sum += num
    return sum