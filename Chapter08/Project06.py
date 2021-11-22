def sortStringByChar(myData):
    myData.sort(reverse=True, key=len)
    return(myData)

def listBuah():
    try:
        count = int(input('Ingin memasukkan berapa buah? '))
        loop = 0
        data = []
        while loop < count:
            buah = input('Masukkan buah ke-{0} : '.format(loop+1))
            data.append(buah)
            loop +=1
        return data
    except ValueError:
        print('Data yang dimasukkan salah')

dataList = listBuah()
if(dataList):
    print('\nHasil buah dari list jumlah karakter penyusun tiap string yang tersusun mulai terbesar hingga terkecil :')
    print('Buah   =',dataList)
    result = sortStringByChar(dataList)
    print('Urutan =',result)

