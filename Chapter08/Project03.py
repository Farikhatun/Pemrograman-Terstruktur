try:
    count = int(input('Ingin memasukkan berapa data mahasiswa? '))
    loop = 0
    data = []
    while loop < count:
        nama = input('Masukkan nama mahasiswa ke-{0} : '.format(loop+1))
        data.append(nama)
        loop +=1

    data.sort()
    print('\nNama mahasiswa dengan urut dan banyaknya karakter:')
    for nama in data:
        print('{0} ({1} karakter)'.format(nama, len(tuple(nama))))
        
except ValueError:
    print('Data yang dimasukkan salah')

