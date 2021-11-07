doc = input('Masukkan nama file : ')

try:
    file = open(doc, 'r')
    print('Isi file ', doc, 'adalah : ')
    print(file.read())
except:
    print('File tidak ada/salah penulisan')
