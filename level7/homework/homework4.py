
asaki = [16,42,49]

def aritmetikuli():
    total = 0
    for x in range(len(asaki)):
        total += asaki[x]
    return total / len(asaki)


print(aritmetikuli())