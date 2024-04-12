# x = [] -  pusta lista
# dir(x) - pokaże spis funkcji do pracy z listą
# help(x.append) -  opis co to robi
# x.append(1) - dodaje 1 na koniec listy
# range(9) -  tworzy zakres od 0 do 9 nie włączając 9 czyli [0,1,2,3,4,5,6,7,8] - dziewięć elementów
# len() - zwraca długość listy, wektora, stringu i t.d.

dane = [1, 0, 2, 3, 0, 4, 5, 0,7,85, 3,15]

x = dane[0]

for i in range(len(dane)):
    if dane[i] > x:
        x = dane[i]

print(x)

