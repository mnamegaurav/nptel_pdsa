def perfect(n):
    factor_sum = 0
    for cn in range(1,(n//2)+1):
        if n%cn == 0:
            factor_sum+=cn
#             print(factor_sum)
    
    if factor_sum == n:
        return True
    else:
        return False

perfect(28)