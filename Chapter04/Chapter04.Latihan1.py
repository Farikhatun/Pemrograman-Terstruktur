print('-----------------Rental Mobil-----------------')
# harga Rental Mobil
print('Harga Sewa Mobil 12 jam Pertama :Rp 200000')
hargaUtama = 200000
print('Harga Tambahan Sewa Mobil       :Rp 10000/jam')
hargaTambahan = 10000
print('----------------------------------------------')

# Waktu Rental Mobil
print('Waktu Peminjaman')
jam1 = int(input('Jam   : '))
menit1 = int(input('Menit : '))
print('Waktu Pengembalian')
jam2 = int(input('Jam   : '))
menit2 = int(input('Menit : '))

dAwal = jam1*3600 + menit1*60
dAkhir = jam2*3600 + menit2*60
if dAwal < dAkhir:
    selisih = dAkhir - dAwal
else:
    selisih = (dAkhir+24*3600)-dAwal
selisihJam = selisih//3600
selisihMenit = (selisih % 3600)/60

print('----------------------------------------------')
print('Total Waktu Peminjaman :', round(selisihJam),
      'jam', round(selisihMenit), 'Menit')
print('----------------------------------------------')

# Pembayaran rental Mobil
if(selisihJam <= 12):
    totalHarga = hargaUtama
    print('Total Harga Sewa       : Rp', round(totalHarga))
elif(selisihJam > 12):
    totalHarga = hargaUtama+hargaTambahan * \
    (selisihJam-12)+hargaTambahan/60*(selisihMenit)
    print('Total Harga Sewa       : Rp', round(totalHarga))
    
bayar = float(input('Pembayaran             : Rp '))
print('Kembalian              : Rp', round(bayar-totalHarga))
print('-----------------Terima Kasih-----------------')
