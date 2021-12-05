file = open('E:\datamahasiswa.txt', 'r')

read = file.readlines()

dataMhs = []
for i in range(len(read)):
    read2 = {}
    dataSatu = read[i].replace('\n', '')
    dataDua = dataSatu.split('|')
    read2['nim'] = dataDua[0]
    read2['nama'] = dataDua[1]
    read2['alamat'] = dataDua[2]
    dataMhs += [read2]

print('dataMhs = '+str(dataMhs))
file.close()
