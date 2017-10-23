for x in map(lambda a,b: a+" "+b, "abc", "123"):
    t = (a,b) = x.split()  # Huh, not only I cna store tuple into entire object, I can also use temporary, unnamed object for it, to assign only into individual variables 
    print (a, b)
    
    