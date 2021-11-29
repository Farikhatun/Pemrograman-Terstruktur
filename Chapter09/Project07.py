mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*65)
print('NIM'.ljust(9), 'NAMA MAHASISWA'.ljust(25), 'TGL LAHIR'.ljust(14), 'TEMPAT LAHIR'.ljust(14))
print('-'*65)

for i in mhs:
    dataList = i.split(':')
    nim      = dataList[0]
    nama     = dataList[1]
    tglLahir = dataList[2]
    dataTglLahir      = tglLahir.split('-')
    newFormatTglLahir = '{0}/{1}/{2}'.format(dataTglLahir[2], dataTglLahir[1], dataTglLahir[0])
    tempatLahir       = dataList[3]
    
    print(nim.ljust(9), nama.ljust(25), newFormatTglLahir.ljust(14), tempatLahir.ljust(14))

print('-'*65)

