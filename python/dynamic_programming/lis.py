"""
Longest Increasing Subsequence problem
----------------------------------
See:
    http://www.geeksforgeeks.org/longest-increasing-subsequence/
"""

# Here I would like to print all the longest increasing sequence(s) present in the list,

# It's kind of nasty solution, as it

# 1 - does find all the longest increasing sequences, but still keeps also some shorter ones
# as candidates found on the way. So, the algorithm is half way to it:)

# 2 - sometimes it finds identical results, although the items of those are not
# the same items always (they came form respective indeces in the input list, when
# there are redundant items in it) ... see testcase 3 for example. Not a bug.
#
# Maybe there's a faster way. Indeed, running this on G4G
# http://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
# they tell me this :( ...
#
#    Your program took more time than expected.
#    Expected Time Limit < 0.7sec
#    Hint : Please optimize your code and submit again.
#

def lis(S):
    """
Walk through sequence S, to collect a sequence Ri such that it is increasing.
E.g. [1,2,3]: iterating, compare 1 and 2, to see result can be [1,2],
then seeing that 2 < 3, so result can be appended with 3 to make [1,2,3].
With e.g. [1,3,2,4], do a split at 2 (trigger look for another result)
and continue collecting first result by comparing its last item to
next item, i.e. from result [1,3], skipping 2 (which is used in splitted search) 
compare 3 to 4 to see 4 can be appended to make [1,2,4].
The split: When a S[i] item is not greater than the last item in so-far collected
result Ri (item Ri[-1]), let's initiate another result lookup: this new result Ri'
may or may not partially overlap with the current result Ri: in S[1,2,4,5,3,4,5,6], the split
finds out that at 3, the Ri of [1,2,4,5] can be split to [1,2] and appended with 3
to form Rinit result as [1,2,3] and continue looking for further increasing items
in the rest of the input where the split has begun, i.e. in [4,5,6] to finally
find the longest increasing sequence, [1,2,3,4,5,6]. This includes also the case,
when the position for the non-greater item is 0, i.e. Rinit is empty. So it can find
also LIS e.g. in [3,4,1,2,3] - the sequence [1,2,3].

Note that generally, some sequences can have more than one LIS, e.g. [2,1] has [2] and [1] etc.

"""
    R = []
    totO = 0
    def split(x, si, Ri, Si):
        # 'x' is not greater than R[-1], so find out where it cna be put inside Ri
        # and trigger lookup for another increasing sequence with that.
        Rinit = []
        nonlocal totO
        for i in range(len(Ri)-1, -1, -1):
            totO += 1
            if x > Ri[i]:
                # start looking for next possible result with Ri[:i+1] + [x] in S[si:]
                Rinit = Ri[:i+1]
                break
        lookres(Si[si:], Rinit)
                
    def lookres(Si, Rinit):
        # Walk through S and collect items into result Ri, so that they increase.
        # If >= item found, do split() to trigger paralel search which will collect
        # the items into Ri'.
        Ri = Rinit + Si[0:1]
        nonlocal totO
        for i in range(0, len(Si)-1):
            totO += 1
            if Ri[-1] < Si[i+1]:
                Ri.append(Si[i+1])
            else:
                split(Si[i+1], i+1, Ri, Si)
        if len(Ri):
            R.append(Ri)
    
    # Empty or single item sequence is simple 
    if len(S) < 2:
        R.append(S)
    else:
        lookres(S[0:], [])
            
    print(R, "tot iterations", totO)
    return R

# G4G version (via Tabulation, opposed to a version with 2^(N-1)-1 complexity, the tabulated has O((N^2-N)/2))
# - this is for finding just the LIS length, not the sequence(s) specifically.
def g4gLisTab(S):
    n = len(S)
    tab = [1]*n
    totO = 0
    for i in range(1, n):
        for j in range(0, i):
            totO += 1
            if S[j] < S[i] and tab[i] < tab[j] + 1:
                tab[i] = tab[j] + 1
    print("Len by G4G:", (max(tab) if n > 0 else 0), tab, "tot iterations", totO)

# Testcases. In each tuple, t[0] is input sequences, t[1] is the correct solution
T = {
    1:([], [[]]),
    2:([1], [[1]]),
    3:([1,2,4,5,3,4,5,6], [[1,2,3,4,5,6]]),
    4:([10, 22, 9, 33, 21, 50, 41, 60, 80], [[10, 22, 33, 50, 60, 80]]),
    5:([3,4,1,2,3], [[1,2,3]]),
    6:([4,3,2,1,0], [[4]]),
    7:([1,2], [[1,2]]),
    9:([1,1], [[1],[1]]),
    10:([2,1], [[2],[1]]),
    11:([1,4,2], [[1,4],[1,2]]),
    13:([1,4,2,3], [[1,2,3]]),
    8:([4,3,1,2,3], [[1,2,3]]),
    14:(["b","c","b"], [["b","c"]])
    }

for t in T:
    tx = T[t]
    R = lis(tx[0])
    for r in tx[1]:
        if not r in R:# or not len(R) == len(tx[1]):
            raise Exception(T[t], "Test %d failed" % t)
            break
        else:
            g4gLisTab(tx[0])
            print (t, "OK")


if False and "runing_on_g4g":
    # Note: to test the lis() on G4G (see link at the head of this file), attach this beneath lis() code
    # to read G2G testcases from them:

    import sys
    try:
        tc = int(sys.stdin.readline())
        for t in range(0, tc):
            lsz = sys.stdin.readline()
            l = list(sys.stdin.readline())
            print(len(max(lis(l))))
    except Exception as e:
        print ("Exception:", e)
    except:
        print ("Exception occured")

