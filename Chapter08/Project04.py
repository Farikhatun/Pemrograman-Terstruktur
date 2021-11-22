data = ['Bayam', 'Kangkung', 'Wortel', 'Selada']
print('=' * 30)
print('Mengolah Data Sayuran')
print('=' * 30)

lagi = 'y' or 'Y'
while lagi == 'y' or 'Y':
    print('A. Tambah Data Sayur ')
    print('B. Hapus Data Sayur')
    print('C. Tampilkan Data Sayur')

    choose = input('\nPilihan Anda : ')
    if(choose.lower() == 'a'):
        append = input('Data sayur yang ingin ditambahkan : ')
        data.append(append)
    elif(choose.lower() == 'b'):
        delete = input('Data sayur yang ingin dihapus : ')
        try:
            data.remove(delete)
            print('{0} berhasil dihapus'.format(delete))
        except ValueError:
            print('{0} tidak ada didalam data'.format(delete))
    elif(choose.lower() == 'c'):
        print('Data Sayuran : {0}'.format(data))
    else:
        print('Tidak ada pilihan {0}'.format(delete))

    lagi = input('\nIngin mengolah data sayuran lagi (y/n)? ')

