def isPythagoras(a, b, c):
    if(a**2 + b**2 == c**2):
        return True
    else:
        return False

print('a = 3, b = 4, c = 5 ', '->', isPythagoras(3, 4, 5))
print('a = 5, b = 9, c = 12', '->', isPythagoras(5, 9, 12))
print('a = 8, b = 6, c = 10', '->', isPythagoras(8, 6, 10))
print('a = 7, b = 8, c = 11', '->', isPythagoras(7, 8, 11))
