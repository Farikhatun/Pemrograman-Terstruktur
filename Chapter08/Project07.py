def sortFromExpensive(data):
    listData = list(data.values())
    listData.sort(reverse=True)
    for x, y in data.items():
        if(listData[0] == y):
           return x
    return False

buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
result = sortFromExpensive(buah)
if(result):
    print('Buah yang harga satuannya paling mahal :')
    print('{0} = Rp.{1}'.format(result, buah[result]))

