m = [
    [1, 0, 0, 0],
    [8, 4, 0, 0],
    [2, 6, 9, 0],
    [8, 5, 9, 3]]

def nonPrime(sayi):
    if sayi > 1:
        for i in range(2,sayi):
            if (sayi % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

toplam = 0
j = 0
for i in range(len(m)):
    i1 = m[i][j]
    i2 = m[i][j+1]
    if(i1 > i2 and nonPrime(i1) == False):
        mmax = i1
        j = m[i].index(mmax)
        toplam += mmax
    elif(i2 > i1 and nonPrime(i2) == False):
        mmax = i2
        j = m[i].index(mmax)
        toplam += mmax
    elif(nonPrime(i1) == False):
        mmax = i1
        j = m[i].index(mmax)
        toplam += mmax
    elif(nonPrime(i2) == False):
        mmax = i2
        j = m[i].index(mmax)
        toplam += mmax
    else:
        j = m[i].index(max(i1, i2))
        toplam += 0


print(toplam)