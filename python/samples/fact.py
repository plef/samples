def fact(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    print (f)
    
for i in range(0,6):
    fact(i)