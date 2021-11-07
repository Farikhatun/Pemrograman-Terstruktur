print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

lagi = 'y'
count = 0
total = 0
while lagi == 'y':
    try:
        bil = int(input('Masukkan bilangan bulat : '))
        total += bil
        count += 1
        lagi = input('Lagi (y/n)? ')
    except ValueError:
        print('Bukan bilangan bulat')
print()
if(count != 0):
    print('Rata-ratanya adalah ', total/count)
else:
    print('Ada data yang salah')

