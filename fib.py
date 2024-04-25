def fib (F):
    a=[]
    a.append(0)
    if F==0:
        return a
    a.append(1)
    if F==1:
        return a
    b=len(a)
    while b-1<F:
        a.append(a[b-2]+a[b-1])
        b=len(a)

    print (a)
    print (a[b-1])
    
        
    return a[b-1]


    

