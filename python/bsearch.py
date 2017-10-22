def binary_search(x, seq):
    def _bs(l,r):        
        if l == r: return False
        m = int((l+r)/2);
        #print (l, r, m)
        if seq[m] == x: return True
        return _bs(l,m) if x < seq[m] else _bs(m+1,r)
    
    return _bs(0,len(seq));

l = list(range(0,10))

for x in l:
    print ("Searching %d: %s" % (x, binary_search(x, l)))
x = -1
print ("Searching %d: %s" % (x, binary_search(x, l)))
x = 11
print ("Searching %d: %s" % (x, binary_search(x, l)))