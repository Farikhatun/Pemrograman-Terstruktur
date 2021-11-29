mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*65)
print('NIM'.ljust(9), 'NAMA MAHASISWA'.ljust(25),
      'TGL LAHIR'.ljust(14), 'TEMPAT LAHIR'.ljust(14))
print('-'*65)

for i in mhs:
    dataList = i.split(':')
    nim      = dataList[0]
    nama     = dataList[1]
    tglLahir = dataList[2]
    TglLahir2   = tglLahir.split('-')
    TglLahir3   = '{0}/{1}/{2}'.format(TglLahir2[2], TglLahir2[1], TglLahir2[0])
    tempatLahir = dataList[3]
    
    print(nim.ljust(10), end='')
    print(nama.ljust(26), end='')
    print(TglLahir3.ljust(15), end='')
    print(tempatLahir.ljust(14))

print('-'*65)
