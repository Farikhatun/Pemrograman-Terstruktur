def starFormation1(n):
    kolom = 1
    i = 0
    while(i < n):
        j = 0
        while(j < kolom):
            print('* ', end='')
            j += 1
        kolom += 1
        print('')
        i += 1

def starFormation2(n):
    kolom = n
    i = 0
    while(i < n):
        j = 0
        while(j < kolom):
            print('* ', end='')
            j += 1
        kolom -= 1
        print('')
        i += 1

def starFormation3(n):
    if(n % 2 == 0):
        starFormation1(n//2)
    else:
        starFormation1(n//2 + 1)
    starFormation2(n//2)
        
starFormation1(4)
starFormation2(4)
starFormation3(7)

