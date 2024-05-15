
def converter(x, base):
    key = '0123456789ABCDEF'
    wyn = ''
    while x>0:
        wyn = str(x%base) + wyn
        x = x // base
    return wyn

    
def r_converter(x,base):
    key = '0123456789ABCDEF'
    print(x, key[x%base])
    if x<=0:
        return ''
    return  r_converter(x//base, base) + key[x%base]

#print(r_converter(26,3))

##r_converter(26,3)
def foo(x):
    if x<=0:
        print('Koniec')
        return
    print(x,'-->a')
    foo(x-1)
    print(x,'b<--')
    
x = 4
def myfun(a,b,c,x):
    y = a*x + b*x**2+c
    return y

def myfun2(a,b,c,x):
    y = a*x**3 + b*x**5+c
    return y

    
    
