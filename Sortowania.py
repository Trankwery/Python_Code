import random as rnd # importowanie modułu/biblioteka do geneowania liczb przypaskowych

a = 10
b = []
while a > 0:
    x = rnd.randint(0,100)
    b.append(x)
    a -= 1
print(b)

c = []
a = 10
for i in range(a):
    x = rnd.randint(0,100)
    c.append(x)
print(c)

d = [ rnd.randint(0,100) for i in range(a) ] # generator list
d1 = [ i**2 for i in range(a) ] # generuje listę kwadratów licz od zera do a
print(d)
print(d1)

def rndlst(l, a, b):
    ''' Ta funkcja generuje liczby losowe.
    l - długość listy; a,b - zakres'''
    c = []
    for i in range(l):
        x = rnd.randint(a,b)
        c.append(x)
    return c

# Miałeś rację co do None!
# Tylko trzeba dodać warunek który by pomijał
# wszystkie wartości None.

def sort_wstawianie(dane):
    out = []
    # Powiedzmy że dane mają długość 10.
    # Wtedy pętla for i ... (zewnętrzna) oznacza że będziemy
    # szukali maksymalnej wartosci 10 razy
    # Maksymalną wartość szukamy w
    # drugiej pętli for j in ... (wewnętrznej)
    for i in range(len(dane)):  
        x = None  
        max_id = None
        for j in range(len(dane)):
            # Wiemy że będziemy usuwali z listy danych elementy
            # więc sprawdzamy czy bieżąca wartość jest liczbą
           if dane[j] != None:
                # Jak znajdziemy liczbę to mamy dwie możliwości:
                if x == None:  # znaleźliśmy liczbę ale x jest jeszcze
                                    # pusty i nie możemy go z niczym porównywać 
                   x = dane[j]
                   max_id = j
                else: # Albo w x już coś włożyliśmy i
                      #  szukamy wartości maksymalnej 
                    if x < dane[j]:
                        x = dane[j]
                        max_id = j
        #Po zakończeniu pętli wewnętrznej dodajemy maksymalny
        # element do listy wynikowej 
        out.append(x)
        # oraz usuwamy tą liczbę z danych wejściowych
        dane[max_id] = None
    return out

def sortowanie_usuwanie(dane):
    out = []
    while len(dane)>0:
        x = dane[0]
        for i in range(len(dane)):
            if x < dane[i]:
                x = dane[i]
        out.append(x)
        dane.remove(x)
    return out

def sortowanie_bombelkowe(dane):
    #Idea jest taka - sprawdzamy dwie liczby obok siebie,
    # jeżeli po prawej liczba jest większa to zamieniamy tę dwie
    # liczby miejscami.
    # Więc po przejściu wewnętrznej pętli na końcu listy
    # będziemy mieli najmniejszą liczbę.
    # Za każdym kolejnym powtórzeniem będziemy dodawać na koniec listy kolejne liczby.
    for i in range(len(dane)):
        for j in range(1,len(dane)):
            if dane[j-1] < dane[j]:
                a = dane[j-1]
                dane[j-1] = dane[j]
                dane[j] = a
    return dane

def rekurencyjne_szybkie(dane):
    # O tym pogadamy na następnej lekcji 
    if len(dane) <= 1:
        return dane
    left = []
    right = []
    for i in range(1, len(dane)):
        if dane[i] < dane[0]:
            right.append(dane[i])
        else:
            left.append(dane[i])
    return rekurencyjne_szybkie(left) + [dane[0]] + rekurencyjne_szybkie(right)
    
dane = rndlst(10, 0, 100)
print('sort_wstawianie')
w = sort_wstawianie(dane.copy()) # dane.copy() - tworzy kopie listy.
# Jak tego nie zrobimy to nasza funkcja sortująca usunie
# wszystkie dane z listy  i nie będziemy mogli  jej wykorzystać
# do innej funkcji sortującej. Trzeba by było wygenerować nową.
# A tak możemy sprawdzić czy sortuje tak samo.
print(w,'\n')

print('sortowanie_usuwanie')
w = sortowanie_usuwanie(dane.copy())
print(w,'\n')

print('sortowanie_bombelkowe')
w = sortowanie_bombelkowe(dane.copy())
print(w,'\n')

print('rekurencyjne_szybkie')
w = rekurencyjne_szybkie(dane.copy())
print(w,'\n')
