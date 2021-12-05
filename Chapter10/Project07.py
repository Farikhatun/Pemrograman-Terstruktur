data = open('E:\soal06.txt', 'r')
hasil = open('E:\soal06Hasil.txt', 'a')

myFile = data.read()
mySet = set(myFile)
mySet.remove(' ')
myList = list(mySet)
myList.sort(reverse=True)

n = 2

file = myFile.replace(myList[0], chr(ord(myList[0])-n))

i = 1
while True:
    file = file.replace(myList[i], chr(ord(myList[i])-n))
    i += 1

    if(i == 10):
        break

file = file.replace(chr(63), chr(89))
file = file.replace(chr(64), chr(90))

print(file)
data.close()
hasil.close()

