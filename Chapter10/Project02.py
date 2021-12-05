dataFile = open('E:\datamahasiswa.txt', 'a')

while True:
    nim = input('Masukkan data NIM    : ')
    nama = input('Masukkan data nama   : ')
    alamat = input('Masukkan data alamat : ')

    myString = nim+'|'+nama+'|'+alamat+'\n'

    dataFile.write(myString)

    ans = input('\nIngin input data lagi (y/n)? ')
    print()
    if ans in ('N','n'):
        break

dataFile.close()
