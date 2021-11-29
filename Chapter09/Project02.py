def bintang(n):
    space = 2*n-1
    for i in range(n):
        print(('*'*(2*i+1)).center(space))

bintang(4)

