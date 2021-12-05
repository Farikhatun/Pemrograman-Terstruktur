file = open('E:\soal05Data.txt', 'r')
hasil = open('E:\soal05Hasil.txt', 'w')

read = file.readlines()

for i in range(len(read)):
    data1 = read[i].replace('\n', '')
    data2 = data1.split('|')
    hasil.write(str(int(data2[0])+int(data2[1]))+'\n')

file.close()
hasil.close()
