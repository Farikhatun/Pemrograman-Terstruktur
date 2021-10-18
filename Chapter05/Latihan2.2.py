from random import randint
bilBulat = 0
count = 0

while(bilBulat <= 100):
    if(bilBulat % 2 == 1):
        count += 1
        print(bilBulat)
    bilBulat += 1
print('Banyaknya bilangan ganjil :', count)

