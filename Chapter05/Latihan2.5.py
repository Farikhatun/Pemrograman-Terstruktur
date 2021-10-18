from random import randint

print('Hai..nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
angkaTebakan = randint(0,100)
while True:
    tebakan = int(input('Tebakan Anda : '))
    if(tebakan < angkaTebakan):
        print('Hehehe... Bilangan tebakan anda terlalu kecil')
    elif(tebakan > angkaTebakan):
        print('Hehehe... Bilangan tebakan anda terlalu besar')
    else:
        print('Yeee... Bilangan tebakan anda BENAR :-)')
