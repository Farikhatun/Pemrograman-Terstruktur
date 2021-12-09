file = open('E:\Peminjaman2.txt', 'a')

from datetime import*

def pengembalian(now):
    return now + timedelta(days=7)

teks = ''
while True:
    kode = input('Masukkan Kode Member   : ')
    nama = input('Masukkan Nama Member   : ')
    judul = input('Masukkan Judul Buku    : ')

    now = datetime.date(datetime.now())
    teks += '{0}|{1}|{2}|{3}|{4}|\n'.format(kode,nama,judul,now,pengembalian(now))
    ans = input('\nUlangi lagi (y/n)? ')
    print()
    if ans in ('N', 'n'):
        break

file.write(teks)
file.close()

