def bintang(n):
    space = n
    if n % 2 == 0:
        print('Jumlah baris harus ganjil')
    else:
        for i in range(n//2+1):
            print(('*'*(2*i+1)).center(space))
        for i in range(n//2, 0, -1):
            print(('*'*(2*i-1)).center(space))

bintang(7)

