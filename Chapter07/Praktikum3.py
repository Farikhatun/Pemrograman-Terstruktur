file = open('e:/data2.txt', 'r')
sum = 0
for data in file:
    try:
        sum += int(data)
    except:
        print('Tidak dapat dikonversikan ke tipe data integer') 
print('\nTotal : ' + str(sum))
