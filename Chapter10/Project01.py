file = open('E:\soal01.txt', 'r')
read = file.readlines()
read2 = []

for i in range(len(read)):
    hasil = read[i].replace('\n', '')
    read2 += [int(hasil)]

ganjil = 0
genap = 0

for data in range(len(read2)):
    if(int(read2[data])%2 == 0):
        ganjil += 1
    else:
        genap += 1
              
print('Banyaknya bilangan genap  :', genap)
print('Banyaknya bilangan ganjil :', ganjil)
file.close()
