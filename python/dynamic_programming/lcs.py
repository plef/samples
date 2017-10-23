"""
Longest Common Subsequence problem
----------------------------------
See:
    http://www.geeksforgeeks.org/longest-common-subsequence/
    http://www.geeksforgeeks.org/printing-longest-common-subsequence/
    https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""

# A sort of naive solution...
# - 1st, I have redundant results being found while looking for the solution
#   so I have to check for presence not to include those more than once...
# - 2nd, we have also shorter than only the longest commons subsequences being
#   pu tmaong results...
# => apparently, there should a dynamic programming way how to optimize the algorithm
#
# Some dyn prog solution is at https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#Code_for_the_dynamic_programming_solution
def lcs(A, B):
    R = []
    def _lcs(A, B, Si):
        nonlocal R
        if len(A) == 0 or len(B) == 0:
            if len(Si) and not Si in R: R.append(Si) # 
            return
        if A[0] == B[0]:
            Si.append(A[0])
            _lcs(A[1:], B[1:], Si)
            return
        Sa = [] + Si
        _lcs(A, B[1:], Sa)
        Sb = [] + Si
        _lcs(A[1:], B, Sb)
        if len(Sa) and not Sa in R: R += [Sa] # 
        if len(Sb) and not Sb in R: R += [Sb] # 
        return
    
    _lcs(A, B, [])
    print (R)
    return R

# Testcases. In each tuple, t[0] and t[1] are input sequences, t[2] is the correct solution
T = {
    1:([],[], []),
    2:([],[1], []),
    3:([1],[], []),    
    4:([1],[1], [[1]]),
    5:([1,2],[1], [[1]]),
    6:([1],[1,2], [[1]]),
    7:([1,2],[1,2], [[1,2]]),
    8:([1,2],[], []),
    9:([1,1],[2,2], []),
    10:([1,2],[2,1], [[1],[2]]),
    11:([1,4,2],[2,1], [[1],[2]]),
    12:([1,3,4,2],[2,1,3], [[1,3]]),
    13:([1,3,2],[1,2], [[1,2]]),
    14:(["a","c","b"],["a","b"], [["a","b"]]),
    15:(list("AGGTAB"),list("GXTXAYB"),[list("GTAB")]),    
    16:([3,6,8,2,5,8,0,2],[1,4,3,7,5,9,6,0,3,6], [[3,6,0], [3,5,0]]),
    17:(list("XMJYAUZ"),list("MZJAWXU"),[list("MJAU")])
    }

for t in T:
    tx = T[t]
    R = lcs(tx[0], tx[1])
    for r in tx[2]:
        if not r in R:
            raise Exception(T[t], "Test %d failed" % t)
            break
    else:
        print (t, "OK")

    
