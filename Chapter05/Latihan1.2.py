print('PERNYATAAN KELULUSAN')
bindo = float(input('Nilai Bahasa Indonesia : '))
ipa   = float(input('Nilai IPA              : '))
mtk   = float(input('Nilai Matematika       : '))

if(bindo>=0) and (bindo<=100) and (ipa>=0) and (ipa<=100) and (mtk>=0) and (mtk<=100):
    if(bindo < 60) or (ipa < 60) or (mtk < 70):
        print('Status Kelulusan       : TIDAK LULUS')
    else:
        print('Status Kelulusan       :LULUS')
else:
    print('Maaf input anda ada yang tidak valid')
