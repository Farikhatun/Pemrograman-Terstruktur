try:
    buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
    print('Daftar Buah :')
    
    number = 1
    for x, y in buah.items():
        print('{0}. {1} - {2}'.format(number, x, y))
        number += 1
        
    print('-' * 30)
    choose = input('Buah yang dibeli : ')
    if(choose in buah):
        kg = float(input('Berat (Kg)       : '))
        print('-' * 30)
        print('Total Harga      : Rp',buah[choose] * kg)
    else:
        print('\n{0} tidak ada didalam daftar'.format(choose))
except ValueError:
    print('Data yang dimasukkan salah')

