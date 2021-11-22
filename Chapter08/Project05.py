def kuadrat(bil):
    if(isinstance(bil, list)):
        for i in range(len(bil)):
            bil[i] **= 2
        return bil
    return False

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
    print('\nHasil kuadrat dari list')
    print('Bil   =',dataList)
    result = kuadrat(dataList)
    print('Hasil =',result)

