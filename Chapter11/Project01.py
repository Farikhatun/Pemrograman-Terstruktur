from datetime import *

def diffDate(x):
    sekarang = datetime.date(datetime.now())
    x = datetime.strptime(x, '%Y-%m-%d').date()
    return (sekarang-x)

y = diffDate('2018-12-30')
print('selisih {0} hari'.format(y.days))
