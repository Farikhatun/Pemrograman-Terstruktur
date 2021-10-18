print('PERNYATAAN KELULUSAN')
bindo = float(input('Nilai Bahasa Indonesia : '))
ipa   = float(input('Nilai IPA              : '))
mtk   = float(input('Nilai Matematika       : '))

if(bindo < 60) or (ipa < 60) or (mtk < 70):
    print('Status Kelulusan       : TIDAK LULUS')
else:
    print('Status Kelulusan       :LULUS')
