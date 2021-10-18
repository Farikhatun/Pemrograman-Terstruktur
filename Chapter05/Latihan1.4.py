kodeKaryawan = input('Masukkan Kode Karyawan : ')
namaKaryawan = input('Masukkan Nama Karyawan : ')
golongan = input('Masukkan Golongan      : ')

if(golongan == 'A'):
    gajiPokok = 10000000
    potongan = 2.5
elif(golongan == 'B'):
    gajiPokok = 8500000
    potongan = 2.0
elif(golongan == 'C'):
    gajiPokok = 7000000
    potongan = 1.5
elif(golongan == 'D'):
    gajiPokok = 5500000
    potongan = 1.0
else:
    golongan = False
    print('Tidak Masuk Golongan')

potonganGaji = int(gajiPokok*potongan/100)
gajiBersih = gajiPokok - potonganGaji

if(golongan != False):
    print('========================================')
    print('STRUK GAJI KARYAWAN')
    print('----------------------------------------')
    print('Nama Karyawan     :',namaKaryawan, '(Kode :',kodeKaryawan,')')
    print('Golongan          :',golongan)
    print('----------------------------------------')
    print('Gaji Pokok        : Rp',gajiPokok)
    print('Potongan (',potongan,'%) : Rp',potonganGaji)
    print('---------------------------------------- -')
    print('Gaji Bersih       : Rp',gajiBersih)
