m = [
    [215, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [193, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [117, 237, 442, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [218, 935, 347, 235, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [320, 804, 522, 417, 345, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [229, 601, 723, 835, 133, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [248, 202, 277, 433, 207, 263, 257, 0, 0, 0, 0, 0, 0, 0, 0],
    [359, 464, 504, 528, 516, 716, 871, 182, 0, 0, 0, 0, 0, 0, 0],
    [461, 441, 426, 656, 863, 560, 380, 171, 923, 0, 0, 0, 0, 0, 0],
    [381, 348, 573, 533, 447, 632, 387, 176, 975, 449, 0, 0, 0, 0, 0],
    [223, 711, 445, 645, 245, 543, 931, 532, 937, 541, 444, 0, 0, 0, 0],
    [330, 131, 333, 928, 377, 733, 17 ,778, 839, 168, 197, 197, 0, 0, 0],
    [131, 171, 522, 137, 217, 224, 291, 413, 528, 520, 227, 229, 928, 0, 0],
    [223, 626, 34, 683, 839, 53, 627, 310, 713, 999, 629, 817, 410, 121, 0],
    [924, 622, 911, 233, 325, 139, 721, 218, 253, 223, 107, 233, 230, 124, 233]]

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