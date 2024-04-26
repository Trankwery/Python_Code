def fib (F):
    a=[]
    a.append(0)
    if F==0:
        return a[0]
    a.append(1)
    if F==1:
        return a[1]
    b=len(a)
    while b-1<F:
        a.append(a[b-2]+a[b-1])
        b=len(a)

    print (a)
    print (a[b-1])
    
        
    return a[b-1]

def fib_2(F):
    a_n_1=0
    a_n=1
    if F==0:
        return a_n_1
    if F==1:
        return a_n
    n=1

    while n<F:
        new_a_n_1=a_n
        a_n=a_n+a_n_1
        a_n_1=new_a_n_1
        n+=1

    return a_n
