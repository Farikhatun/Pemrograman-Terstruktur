file = open('E:\datamahasiswa.txt', 'r')

search = input('Masukkan NIM yang mau dicari : ')
result = False

for data in file:
    data2 = data.split('|').copy()
    nim = data.split('|')[0]
    if(nim == search):
        result = data2
        break

if(result):
    print()
    print('Data Mahasiswa')
    print('NIM    :', result[0])
    print('Nama   :', result[1])
    print('Alamat :', result[2])
else:
    print('Data mahasiswa tidak ditemukan')

file.close()
