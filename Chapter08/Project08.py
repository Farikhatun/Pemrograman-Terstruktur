def average(data):
    tupleData = tuple(data.values())
    sumData = sum(tupleData)
    count = len(tupleData)
    return sumData / count

buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
result = average(buah)
if(result):
    print('Rata-rata harga satuan semua buah yang ada adalah Rp {0}'.format(result))

