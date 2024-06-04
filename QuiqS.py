def qiuqS(dane, key=1):
    # key kierunek sortowania
    if len(dane) <= 1:
        return dane
    
    a = dane[0]
    left = []
    right = []
    for i in range(1,len(dane)):
        if key == 1:
            if a >= dane[i]:
                left.append(dane[i])
            else:
                right.append(dane[i])
        else:
            if a <= dane[i]:
                left.append(dane[i])
            else:
                right.append(dane[i])
    return qiuqS(left,key) + [a] + qiuqS(right,key)

def  bobleSort(dane):
    for j in range(len(dane)):
        for i in range(len(dane)-1-j):
            if dane[i]>=dane[i+1]:
                dane[i],dane[i+1] = dane[i+1],dane[i]
    return dane

print(bobleSort([-11,3,12,5,-8]))
