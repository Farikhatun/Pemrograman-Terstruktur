def sum(*allNumber):
    total = 0
    for number in allNumber:
        total += number
    return total

def average(*allNumber):
    count = 0
    for number in allNumber:
        count += 1
    return sum(*allNumber) / count

def maks(*allNumber):
    max = allNumber[0]
    for number in allNumber:
        if(number > max):
            max = number
    return max

def min(*allNumber):
    min = allNumber[0]
    for number in allNumber:
        if(number < min):
            min = number
    return min
