#Menghitung BBM yang Dibutuhkan untuk Perjalanan
print('Komsumsi BBM : 12Km/Liter')
perLiter = 12
jarak = int(input('Jarak Tempuh : '))
banyakBBM = jarak/perLiter
print('BBM yang dibutuhkan :', banyakBBM, 'Liter')

#Menghitung Minimal Pengisian BBM yang Dibutuhkan
kapasitas = 50
pengisian = banyakBBM//kapasitas
print('Minimal Pengisian yang Diperlukan : ', pengisian, 'Kali')
