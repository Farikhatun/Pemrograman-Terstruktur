import random
def shuffleString(x, n):
    list = []
    i = 0
    while i < n:
        acak = ''.join(random.sample(x,len(x)))
        if acak not in list:
            list += [acak]
            i += 1
    print(list)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)

