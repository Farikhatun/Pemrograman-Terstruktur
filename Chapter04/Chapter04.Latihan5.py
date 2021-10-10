import matplotlib.pyplot as plt

#Menjelaskan Isi Plot
plt.figure(figsize=[10, 5])
mahasiswa=['Laki-laki', 'Perempuan']
jumlah=[100, 150]
plt.barh(mahasiswa, jumlah, color = 'purple', edgecolor='black')

#Menjelaskan Label Plot
plt.title('Presentase Mahasiswa PTIK UNS')
plt.xlabel('Jumlah Mahasiswa')
plt.ylabel('Mahasiswa')

plt.show()
