# membuka dan mau membaca file e:/data.txt
try:
    file = open('e:/data.txt', 'r')

# baca baris pertama dan kedua dari file
# simpan ke dalam variabel bil1 dan bil2 sebagai integer
    bil1 = int(file.readline())
    bil2 = int(file.readline())

# hitung dan tampilan hasil bagi
    hasil = bil1/bil2
    print(bil1, ' dibagi ', bil2, ' sama dengan ', hasil)
    
except FileNotFoundError:
    print('File tidak ditemukan')
except ZeroDivisionError:
    print('tidak boleh pembagian dengan nol')

