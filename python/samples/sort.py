def sort(S):
    def swap(a,b):
        tmp = S[a]
        S[a] = S[b]
        S[b] = tmp
    def qs(l,r):
        if r-l < 2:
            return
        m = (l+r)//2
        li = l
        ri = r
        while li < m and ri > m:
            for li in range(l, m+1):
                if S[m] < S[li]: break;
                #li += 1
            for ri in range(r,m-1,-1):
                if S[m] > S[ri]: break;
                #ri += 1
            if li < ri:
                swap(li,ri)
        if li < r: qs(li,r)
        if ri > l: qs(l,ri)
    qs(0,len(S)-1)
    
    
L = [4,3,2,1,0,34,67,78,4,3,35,7]
sort(L)
print(L)
       

            