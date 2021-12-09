file = open('E:\Peminjaman.txt', 'a')

from datetime import*

def pengembalian(now):
    return now + timedelta(days=7)

lagi = 'y' or 'Y'
teks = ''

while lagi == 'y':
    kode = input('Masukkan Kode Member   : ')
    nama = input('Masukkan Nama Member   : ')
    judul = input('Masukkan Judul Buku    : ')

    now = datetime.date(datetime.now())
    teks += '{0}|{1}|{2}|{3}|{4}|\n'.format(kode,nama,judul,now,pengembalian(now))
    lagi = input('\nUlangi lagi (y/n)? ')
    print()

file.write(teks)
file.close()

