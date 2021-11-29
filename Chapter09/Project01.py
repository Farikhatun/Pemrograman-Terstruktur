def ubahHuruf(teks, a, b):
    listTeks = list(teks)
    for char in listTeks:
        if(char == a):
            char = b
    return teks.replace(a, b)

print(ubahHuruf('MATEMATIKA','T','S'))

