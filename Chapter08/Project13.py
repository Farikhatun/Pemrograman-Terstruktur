def findData(data):
    nilaiAkhir = None
    result = {}
    for x in data:
        nilai = (x['mid'] + (2 * x['uas'])) / 3
        if(nilaiAkhir is None) or (nilai > nilaiAkhir):
            nilaiAkhir = nilai
            result['nim'] = x['nim']
            result['nama'] = x ['nama']
    return result

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40},]

result = findData(nilaiMhs)
if(bool(result)):
    print('Mahasiswa yang memiliki nilai akhir tertinggi yaitu \
{0} dengan NIM {1}'.format(result['nama'],result['nim']))

