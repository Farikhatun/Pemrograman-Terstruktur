#list a dan b
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print('a :',a)
print('b :',b)
print()

#menyisipkan nilai 10 ke dalam indeks ke 3 dari a
#menyisipkan nilai 15 ke dalam indeks ke 2 dari b
a.insert(2, 10)
b.insert(1, 15)
print('a :',a)
print('b :',b)
print()

#menyisipkan nilai 4 ke indeks terakhir dari a
#menyisipkan nilai 8 ke indeks terakhir dari b
a.append(4)
b.append(8)
print('a :',a)
print('b :',b)
print()

#melakukan sorting secara ascending pada list a dan b
a.sort()
b.sort()
print('a :',a)
print('b :',b)
print()

#membuat list c dengan elemen sublist dari a (indeks ke 0 s/d 7)
#membuat list d dengan elemen sublist dari b (indeks ke 2 s/d 9)
c = a [0 : 7]
d = b [2 : 9]
print('c :',c)
print('d :',d)
print()

#membuat list e dengan elemen yang merupakan hasil penjumlahan
#penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya
e = []
for i in range(len(c)):
    e += [c[i] + d[i]]
print('e :',e)
print()

#mengubah list e ke dalam tuple
tuple_e = tuple(e)
print('e (tuple) :',tuple_e)
print()

#mencari nilai min, max, dan jumlahan seluruh elemen dari e
print('Nilai minimum dari tuple e', tuple_e, 'adalah', min(tuple_e))
print('Nilai maximum dari tuple e', tuple_e, 'adalah', max(tuple_e))
print('Jumlah seluruh elemen tuple e', tuple_e, 'adalah', sum(tuple_e))
print()

#mendefinisikan variabel myString
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)
print()

#menentukan karakter huruf penyusun myString
huruf = set(myString)
print('Huruf penyusun =', huruf)
print()

#mengurutkan himpunan karakter huruf myString berdasarkan alfabet
listHuruf = list(huruf)
listHuruf.sort()
print('Urutan secara alfabet', listHuruf)
print()
