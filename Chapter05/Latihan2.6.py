from random import randint

print('Hai..nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
angkaTebakan = randint(0,100)
score = 100
while True:
    if(score < 1):
        print('Anda sudah tidak boleh bermain karena score anda sudah habis')
        break
    tebakan = int(input('Tebakan Anda : '))
    if(tebakan < angkaTebakan):
        print('Hehehe... Bilangan tebakan anda terlalu kecil')
    elif(tebakan > angkaTebakan):
        print('Hehehe... Bilangan tebakan anda terlalu besar')
    else:
        print('Yeee... Bilangan tebakan anda BENAR :-)')
        print('Score Anda :',score)
        break
    score -= 2
