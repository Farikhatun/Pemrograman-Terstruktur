#Menghitung Perjalanan Dari A ke B
jarak1 = float(input('Jarak A-B              : '))
kecepatan1 = float(input('Kecepatan              : '))
perjalanan1 = jarak1/kecepatan1
waktu1 = perjalanan1*60
print('Lama Perjalanan        :', perjalanan1)

istirahat = float(input('Lama Istirahat         : '))
waktu2 = istirahat

#Menghitung Perjalanan Dari B ke C
jarak2 = float(input('Jarak B-C              : '))
kecepatan2 = float(input('Kecepatan              : '))
perjalanan2 = jarak2/kecepatan2
print('Lama Perjalanan        :', perjalanan2)
waktu3 = perjalanan2*60

#Menghitung Total Waktu Perjalanan Dari A ke C
print('Waktu Berangkat        :')
jam = int(input('     Jam               : '))
menit = int(input('     Menit             : '))
totalWaktu = (waktu1+waktu2+waktu3)/60
menitWaktu = (waktu1+waktu2+waktu3)%60
print('Total Waktu Perjalanan :', round(totalWaktu), 'Jam', round(menitWaktu), 'Menit')

#Menghitung Waktu Sampai Tujuan
jamTiba = jam+totalWaktu
menitTiba = menit+menitWaktu%60
print('Waktu Tiba di Tujuan   :', round(jamTiba),'.', round(menitTiba))
