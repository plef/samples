'''
    Playing with dynamic programming examples.
    
    See http://www.geeksforgeeks.org/dynamic-programming-set-1/
'''

def fibonacci(val, use_cache = False):
    # memoization, pattern of dyn, prog.: store values that would otherwise
    # have to be computed again. A sort of cache.
    # Without, it T() is O(2^n), more exactly it is equal to F(n) itself, as the
    # treee is not balanced given by O(n-2) in one branch and O(n-1) in the other,
    # so its actually about O(1.6^n). With cache, it's maybe O(2n-1) 
    global _cache, _totcalls
    _cache = [None]*(val+1)
    _totcalls = 0
    def _memoized(n):
        if n < len(_cache): return _cache[n]
        else: raise Exception("Cache get miss", n)  # shold not happen, see we need val+1 entries always
    def _memoize(n, val):
        global _cache
        if use_cache:
            if n < len(_cache): _cache[n] = val
            else: raise Exception("Cache set miss", n) # shold not happen, see we need val+1 entries always
        return val
    def _fib(n):
        global _cache, _totcalls
        _totcalls += 1
        # recursion stop condition
        if n <= 1:
            return _memoize(n, n)        
        # check cache 
        if not None == _memoized(n):
            return _memoized(n)
        #return _memoize(n-2, _fib(n-2)) + _memoize(n-1, _fib(n-1)) # or
        return _memoize(n, _fib(n-2) + _fib(n-1))
    return (_fib(val), _totcalls)

def fibonacci_tabulated(val):
    # Tabulating is anothe approach of dyn.prog. to optimize the calculation of problem
    # Seems to provide tiny tiny slightly better time complexity than memoization for Fibonacci,
    # compare http://code.geeksforgeeks.org/Z94jYR and http://code.geeksforgeeks.org/12C5bP
    # ... despite it's apparently O(n)
    # (basic version http://code.geeksforgeeks.org/vHt6ly)
    if val <= 1: return val
    tab = [None]*(val+1)
    tab[0] = 0
    tab[1] = 1
    for x in range(2,val+1):
        tab[x] = tab[x-2] + tab[x-1]
    return tab[val]

#   -----------------------------------------------------------------------------

def uglynumber(n):
    """http://www.geeksforgeeks.org/?p=753"""
    # Ugly numbers is a number which's prime factors are only 2, 3 or 5.
    # By convenience, 1 is included among ugly numbers. Orders, ugly numbers
    # are as follows:
    # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...
    # For exmaple, 7th ugly number is 8, so we count them from 1.
    if n < 1:
        return None  # sanity check
    
    # Ok, basic solution os to generate some amount of ugly numbers,
    # based that each such number is calculated as 2^x*3^y*5^z for
    # a range of x, y, z.
    seq = {2:[],3:[],5:[]}
    all = []
    # ... let generate some powers of 2, 3, and 5 into separate lists
    for a in (2,3,5):    
        for x in range(0,int(n)):
            val = a**x
            if not val in seq[a]: seq[a] += [a**x]
            # ... put them into the overall lists of all ugly numbers
            # (must obey already present numbers in each of the lists) 
            if not val in all: all += [val]
    #print(all)
    # ... then we yet need to also calculate all multiplications of
    # the previsouly collected powers of 2, 3 and 5, add them into
    # the list of all ugly numbers (must obey already present numbers
    # in the overall list)
    for x in range(0, len(seq[2])):
        for y in range(0, len(seq[3])):
            for z in range(0, len(seq[5])):
                val = seq[2][x]*seq[3][y]*seq[5][z]
                #print(val,x,y,z)
                if not val in all: all += [val]
    # ... finally, to obtain the correct n-th ugly number, we got to
    # sort the list of all so-far collected unique ugly numbers
    all = sorted(all)
    
    # Apparently, this method is quite complex, see we have
    # O(3n) + O(n*n*n) + O() of the sorted() routine (suppose some
    # enhancd quicksort, so let's say it'd be O(m log m) where 'm'
    # is somewhere up to 3n+n*n*n). Deadly bad.
    return (all[n-1], all[:n])

def uglynumber2(n):
    # Another, less brutal approach: iterate 1..x numbers, for each
    # inspect whether it is ugly number, if so, add it into list of
    # uglies, and do this all until the list reaches 'n' in size, so
    # that the last item is the searched result.
    def maxdivby(n, d):
        while (n % d == 0):
            n = n / d
        return n
    def isugly(i):
        return  maxdivby(maxdivby(maxdivby(i, 2), 3), 5) == 1

    if n < 1: return None
    all = [1]    
    i = 2
    while len(all) < n:
        if isugly(i) and not i in all: all += [i]
        i += 1
        
    return (all[-1], all[:n])
    
######################################################################    

def main():
    print (__doc__)
    print ("""1.
Fibonnaci(x), without and with Memoization, and with Tabulation. You can
see as of F(4), the use of memoization makes spare of tot recursive calls,
with F(9) REALLY GREAT spare.""")
    for x in range(0,12):
        print ("Fibonacci(%d):" % (x))
        print (fibonacci(x))
        print (fibonacci(x, True))
        print (fibonacci_tabulated(x))
    print ("The cache after last call:\n", _cache)
    
    print ("\n--------------------------------------------\n")
    
    print ("""2.
The Ugly Numbers, ugly(x) and list of ugly numbers up to it. First, a brutal solution
where we precalculate unique powers of 2,3,5 and their unique multiplications, order
the list and return n-1th item. Second, for each 2..x we inspect it for being ugly number
and if so, add it into the list, until the list has n items, returning the last one as
the result.""")
    for x in range(0,12):
        print ("Ugly(%d): %s " % (x, uglynumber(x)))
        print ("Ugly2(%d): %s " % (x, uglynumber2(x)))

if __name__ == "__main__":
    main()
