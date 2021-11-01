def faktorial(n):
    result = n
    while(n > 1):
        n -= 1
        result *= n
    return result

def C(n, r):
    return faktorial(n) / (faktorial(n - r) * faktorial(r))

def P(n, r):
    return faktorial(n) / faktorial(n - r) 

print(C(5,3))
print(P(10,7))

