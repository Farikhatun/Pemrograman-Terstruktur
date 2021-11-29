nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*52)
print('NIM'.ljust(8), 'NAMA'.ljust(14), 'N.MID'.rjust(8), 'N.UAS'.rjust(10))
print('-'*52)

for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(9), end='')
    print(nilai[i]['nama'].ljust(14), end='')
    print(str(nilai[i]['mid']).rjust(9), end='')
    print(str(nilai[i]['uas']).rjust(11))

print('-'*52)

