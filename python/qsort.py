def quick_sort(seq, exmed = False):
    global tot, rmedtot, lmedtot
    rmedtot, lmedtot, tot = 0, 0, 0
    def _swp(a,b):
        x = seq[a]
        seq[a] = seq[b]
        seq[b] = x
    def _med(l,r):
        global rmedtot, lmedtot
        m = int((l+r)/2)
        if exmed:
            if seq[l] < seq[m] and seq[l] > seq[r]:
                lmedtot += 1
                return l
            if seq[r] < seq[m] and seq[r] > seq[l]:
                rmedtot += 1
                return r
        return m
    def _partition(l,r):
        m = _med(l,r)
        #print ("part", l, r, m)
        piv = seq[m]
        il, ir = l, r
        while True:
            while seq[il] < piv and il < r:
                il += 1
            while seq[ir] > piv and ir > l:
                ir -= 1
            if il <= ir:
                _swp(il, ir)
                il += 1
                ir -= 1
            if il >= ir: return (il,ir)
    def _qs(l,r, depth):
        global tot
        ld, rd = depth, depth
        if (l < r):
            tot += 1
            (il,ir) = _partition(l,r)
            if (l < ir): rd = _qs(l,ir, depth+1)
            if (il < r): ld = _qs(il,r, depth+1)
            return ld if ld > rd else rd
    
    depth = _qs(0,len(seq)-1, 0)
    print ("depth: {0} tot: {1} lmed: {2} rmed: {3}".format(depth, tot, lmedtot, rmedtot))
    return seq
    
import copy    
l = [4,1,3,7,49,17,9,26,33,86,27,18,0,53,54,9,5,13,37,6,8,91,23,22,2,17,8]
m = copy.copy(l)
print (l)
print (quick_sort(l))
print (m)
print (quick_sort(m, True))