try:
    count = int(input('Ingin memasukkan bilangan berapa kali? '))
    loop = 0
    data = []
    while loop < count:
        number = int(input('Masukkan bilangan bulat ke-{0} : '.format(loop+1)))
        data.append(number)
        loop +=1

    data.sort(reverse=True)
    print('\nHasil data dengan urutan bilangan dari besar ke kecil :\n', data)
except ValueError:
    print('Data yang dimasukkan salah')

