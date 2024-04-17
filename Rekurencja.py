
def sumaliczb(x):
    sx = str(x) # zamiania liczby na tekst

    suma = 0

    for i in range(len(sx)):
        suma += int( sx[i] )
    return suma

def sumaliczb_2(x):
    suma = 0
    while x>0:
        suma += x%10 # reszta z dzielenia
        x = x //10 # dzielenie całkowitoliczbowe  (wynik dzielenia zaokrąglony w dół) 
    return suma

def suma_3(x):
    if x<=0:
        return 0
    return x%10 + suma_3(x//10)

def fib( n ):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)
    
print(suma_3(100500))
 
