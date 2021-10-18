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

if(golongan != False):
    status = int(input('Masukkan Status (1.Menikah, 2.Belum Menikah) : '))
    if(status == 1):
        tunjanganNikah = gajiPokok*10/100
        anak = int(input('Masukkan Jumlah Anak   : '))
        tunjanganAnak = gajiPokok*5/100*anak
    elif(status == 2):
        tunjanganNikah = 0
        tunjanganAnak = 0
    else:
        print('Input Tidak Valid')

    gajiKotor = gajiPokok+tunjanganNikah+tunjanganAnak
    potonganGaji = int(gajiKotor*potongan/100)
    gajiBersih = gajiKotor - potonganGaji
    
    if(status != False):
        print('========================================')
        print('STRUK GAJI KARYAWAN')
        print('----------------------------------------')
        print('Nama Karyawan         :',namaKaryawan, '(Kode :',kodeKaryawan,')')
        print('Golongan              :',golongan)
        if(status == 1):
            print('Status                : Menikah')
            print('Jumlah Anak           :',anak)
        else:
            print('Status                : Belum Menikah')
        print('----------------------------------------')
        print('Gaji Pokok            : Rp',gajiPokok)
        print('Tunjangan Istri/Suami : RP',tunjanganNikah)
        print('Tunjangan Anak        : Rp',tunjanganAnak)
        print('---------------------------------------- +')
        print('Gaji Kotor            : Rp',gajiKotor)
        print('Potongan (',potongan,'%)     : Rp',potonganGaji)
        print('---------------------------------------- -')
        print('Gaji Bersih           : Rp',gajiBersih)
