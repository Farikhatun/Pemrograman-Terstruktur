def dataStat(x):
    if(isinstance(x, list)):
        tuplex = tuple(x)
        a = sum(tuplex)/len(tuplex)
        b = max(tuplex)
        c = min(tuplex)

        return [a, b, c]
    else:
        print('Data yang dimasukkan salah')

def listUser():
    try:
        count = int(input('Ingin memasukkan berapa bilangan? '))
        loop = 0
        data = []
        while loop < count:
            number = int(input('Masukkan bilangan bulat ke-{0} : '.format(loop+1)))
            data.append(number)
            loop +=1

        return data
    except ValueError:
        print('Data yang dimasukkan salah')
        return False

dataList = listUser()
if(dataList):
    result = dataStat(dataList)
    print('\nRata-rata data dari list  : {1}'.format(dataList, result[0]))
    print('Nilai tertinggi dari list : {1}'.format(dataList, result[1]))
    print('Nilai terendah dari list  : {1}'.format(dataList, result[2]))



