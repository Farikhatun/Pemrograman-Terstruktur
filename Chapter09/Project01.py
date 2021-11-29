def ubahHuruf(teks, a, b):
    listTeks = list(teks)
    for i in listTeks:
        if(i == a):
            i = b
    return teks.replace(a, b)

print(ubahHuruf('MATEMATIKA','T','S'))

