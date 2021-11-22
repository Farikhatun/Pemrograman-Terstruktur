buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}

def showData(data):
    print('-' * 30)
    print('Daftar Buah :')
    number = 1
    for x, y in data.items():
        print(' {0}. {1} - {2}'.format(number, x, y))
        number += 1
    print('-' * 30)
    
showData(buah)
lagiPilihan = 'y'
while lagiPilihan == 'y':
    print('A. Tambah Data Buah')
    print('B. Beli Buah')
    pilihan = input('\nPilihan Menu : ')
    if(pilihan == 'A'):
        dataBaru= input('Masukkan nama buah    : ')
        if(dataBaru in buah):
            print('Buah sudah terdaftar')
        else:
            while True:
                try:
                    hargaDataBaru = int(input('Masukkan harga satuan : '))
                    buah[dataBaru] = hargaDataBaru
                    showData(buah)
                    break
                except ValueError:
                    print('Data yang dimasukkan salah')

    elif(pilihan == 'B'):
        showData(buah)
        total = 0
        lagiBeli = 'y'
        while lagiBeli == 'y':
            choose = input('Buah yang dibeli : ')
            if(choose in buah):
                while True:
                    try:
                        kg = float(input('Berat (Kg)       : '))
                        total += (buah[choose] * kg)
                        lagiBeli = input('\nBeli buah yang lain (y/n)? ')
                        break
                    except ValueError:
                        print('Data yang dimasukkan salah')
                            
            else:
                print('\n{0} tidak ada didalam daftar'.format(choose))
                        
        print('-' * 30)        
        print('Total Harga      : Rp',total)
        print('-' * 30)
    
    else:
        break
