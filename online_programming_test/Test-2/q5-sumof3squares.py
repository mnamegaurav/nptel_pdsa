def sumof3squares(n):
    i = 1
    while i*i <= n:
        j = 1
        while(j*j <= n):
            k=1
            while(k*k <= n):
                if (i*i + j*j +k*k == n):
                    return True
                k+=1
            j+=1
        i+=1          
    return False