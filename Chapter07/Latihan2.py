doc = input('Masukkan nama file : ')
try:
    file = open(doc, 'r')
    lagi = 'y'
    while lagi == 'y':
        file = open(doc, 'a')
        append = input('Data yang mau ditambahkan : ')
        file.write(append)
        lagi = input('Mau lagi (y/n) : ')
        file.close()
except:
    print('File tidak ada/Salah penulisan')
