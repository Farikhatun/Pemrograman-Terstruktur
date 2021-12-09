from datetime import *

def pengembalian(x):
    sekarang = datetime.date(datetime.now())
    x = datetime.strptime(x, '%Y-%m-%d').date()
    lamaPinjam = sekarang - x
    return lamaPinjam.days

search = input('Masukkan Kode Member   : ')
file = open('E:\Peminjaman.txt', 'r')
result = False

for data in file:
    data2 = data.split('|').copy()
    kode = data.split('|')[0]
    if(kode == search):
        result = data2
        break

if(result):
    maksPinjam = result[4].rstrip('\n')
    terlambat = pengembalian(maksPinjam) 
    if(terlambat > 0):
        telat = str(terlambat) + ' hari'
        denda = 'RP ' + str(terlambat * 2000)
    else:
        telat = 'Tidak Terlambat'
        denda = 'Tidak Ada Denda'
    
    print('Data Peminjaman Buku')
    print('Kode Member              : ', result[0])
    print('Nama Member              : ', result[1])
    print('Judul Buku               : ', result[2])
    print('Tanggal Mulai Peminjaman : ', result[3])
    print('Tanggal Maks Peminjaman  : ', maksPinjam)
    print('Tanggal Pengembalian     : ', datetime.date(datetime.now()))
    print('Terlambat                : ', telat)
    print('Denda                    : ', denda)
else:
    print('Data Mahasiswa Tidak Ditemukan')

