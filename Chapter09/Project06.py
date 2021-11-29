nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*75)
print('NIM'.ljust(8), 'NAMA'.ljust(15), 'N.MID'.ljust(12), 'N.UAS'.ljust(12),
      'N.AKHIR'.ljust(14), 'STATUS'.rjust(4))
print('-'*75)

for i in nilai:
    nAkhir = (i['mid'] + (2 * i['uas'])) / 3
    status = 'LULUS'
    if(nAkhir < 60):
        status = 'TIDAK LULUS'
    print(i['nim'].ljust(9), end='')
    print(i['nama'].ljust(17), end='')
    print(str(i['mid']).ljust(13), end='')
    print(str(i['uas']).ljust(13), end='')
    print(str(round(nAkhir,2)).ljust(14), end='')
    print(status.rjust(4))

print('-'*75)

